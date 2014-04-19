import sunburnt
import operator
import unicodedata
import pickle
import random

import SETTINGS
from numpy.ma.testutils import assert_equal
from _abcoll import Set


def create_ngram_dict():
    word_dict_unigram = {}
    word_dict_bigram = {}
    word_dict_trigram = {}
    # contains the list of results
    result_list = []
    sMessage = sunburnt.SolrInterface("http://localhost:8983/solr/message/")
    for result in sMessage.query(text="*").field_limit(["body", "subject"]).paginate(start=0, rows=255636).execute():
        result_list.append(result)
    
    for list_element in result_list:    
        # for body and subject type
        for key, value in list_element.iteritems():
            # Converting unicode to string
            value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
            put_ngram_word(word_dict_unigram, word_dict_bigram, word_dict_trigram, value)
    
    sorted_word_dict_unigram = sorted(word_dict_unigram.iteritems(), key=operator.itemgetter(1), reverse=True)
    sorted_word_dict_bigram = sorted(word_dict_bigram.iteritems(), key=operator.itemgetter(1), reverse=True)
    sorted_word_dict_trigram = sorted(word_dict_trigram.iteritems(), key=operator.itemgetter(1), reverse=True)
    
    return sorted_word_dict_unigram, sorted_word_dict_bigram, sorted_word_dict_trigram
    
    
def put_ngram_word(word_dict_unigram, word_dict_bigram, word_dict_trigram, value):
    # n = 1,2,3
    for n in range(1, 4):
        splitted_value = value.split()
        # creating list of n grams
        temp_list = [' '.join(splitted_value[x:x + n]) for x in xrange(0, len(splitted_value), n)]
        for element in temp_list:
            if n == 1:
                add_to_dictionary(word_dict_unigram, element)
            elif n == 2:
                add_to_dictionary(word_dict_bigram, element)
            elif n == 3:
                add_to_dictionary(word_dict_trigram, element)
                       

def add_to_dictionary(word_dict, element):
    if element.lower() in word_dict:
        word_dict[element.lower()] += 1
    else:
        word_dict[element.lower()] = 1    


def dump_unigram(sorted_word_dict_unigram):    
    out_unigram = open(SETTINGS.unigram_object_file, "wb")
    pickle.dump(dict(sorted(dict(sorted_word_dict_unigram[:5000]).iteritems(), key=operator.itemgetter(1), reverse=True)), out_unigram)
    out_unigram.close()
    
    
def dump_bigram(sorted_word_dict_bigram):    
    out_bigram = open(SETTINGS.bigram_object_file, "wb")
    pickle.dump(dict(sorted(dict(sorted_word_dict_bigram[:500]).iteritems(), key=operator.itemgetter(1), reverse=True)), out_bigram)
    out_bigram.close()
    
    
def dump_trigram(sorted_word_dict_trigram):    
    out_trigram = open(SETTINGS.trigram_object_file, "wb")
    pickle.dump(dict(sorted(dict(sorted_word_dict_trigram[:200]).iteritems(), key=operator.itemgetter(1), reverse=True)), out_trigram)
    out_trigram.close()
        


def extract_feature_map():
    unigram_dict_loaded = pickle.load(open(SETTINGS.unigram_object_file, "rb"))
    bigram_dict_loaded = pickle.load(open(SETTINGS.bigram_object_file, "rb"))
    trigram_dict_loaded = pickle.load(open(SETTINGS.trigram_object_file, "rb"))

    # Shortened dictionary
    unigram_feature_dict = {}
    bigram_feature_dict = {}
    trigram_feature_dict = {}

    # EXTRACT TOP k N-GRAMS FROM EACH DICT AND CREATE A VECTOR OUT OF IT
    
    # creating a ngram_vector_map containing keys as terms and value as index in the vector
    # count represent the index in the feature_vector
    count = 0
    feature_map = {}

    sorted_unigram = dict(sorted(unigram_dict_loaded.iteritems(), key=operator.itemgetter(1), reverse=True))
#     sorted_unigram = dict(sorted(unigram_dict_loaded.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
    # for key, value in dict(unigram_dict_loaded[:5]).iteritems():
    for key, value in sorted_unigram.iteritems():
#     for key, value in unigram_dict_loaded.iteritems():
        unigram_feature_dict[key] = value
        feature_map[key] = count
        count = count + 1
        
    sorted_bigram = dict(sorted(bigram_dict_loaded.iteritems(), key=operator.itemgetter(1), reverse=True))    
#     sorted_bigram = dict(sorted(bigram_dict_loaded.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])    
    # for key, value in dict(bigram_dict_loaded[:5]).iteritems():
    for key, value in sorted_bigram.iteritems():
#     for key, value in bigram_dict_loaded.iteritems():
        bigram_feature_dict[key] = value
        feature_map[key] = count
        count = count + 1
        
    sorted_trigram = dict(sorted(trigram_dict_loaded.iteritems(), key=operator.itemgetter(1), reverse=True))    
#     sorted_trigram = dict(sorted(trigram_dict_loaded.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])        
    # for key, value in dict(trigram_dict_loaded[:5]).iteritems():
    for key, value in sorted_trigram.iteritems():
#     for key, value in trigram_dict_loaded.iteritems():
        trigram_feature_dict[key] = value
        feature_map[key] = count
        count = count + 1
        
    print unigram_feature_dict, bigram_feature_dict, trigram_feature_dict
    print sorted(feature_map.iteritems(), key=operator.itemgetter(1))
        
    out_feature_map = open(SETTINGS.feature_map, "wb")
    pickle.dump(feature_map, out_feature_map)
    out_feature_map.close()
    

def create_feature_vector():
    feature_map = pickle.load(open(SETTINGS.feature_map, "rb"))
    
    print feature_map
    
    feature_vectors = []
    modified_feature_vectors = []
    target_values = []
    # create a list of feature vector along with a list of target value from the data set
    result_list = []
    sMessage = sunburnt.SolrInterface("http://localhost:8983/solr/message/")
#     for result in sMessage.query(text="*").field_limit(["body", "subject", "compliantFlag"]).paginate(start=0, rows=255636).execute():
    for result in sMessage.query(text="*").field_limit(["body", "subject", "compliantFlag"]).paginate(start=0, rows=255636).execute():
        result_list.append(result)
    
    # For each result
    for list_element in result_list:    
        # initialize it to the size of feature selected i.e 5000+500+200
        feature_vector = [0] * 5700
#         print "Subject:" + list_element['subject'].lower()
#         print "Body:" + list_element['body'].lower()
#         print "Compliant Flag:", list_element['compliantFlag']
        for key_feature, value_feature in feature_map.iteritems():
            words_in_feature_key = key_feature.split()
            if (len(words_in_feature_key) == 1):
                if (key_feature.lower() in list_element['subject'].lower().split() or key_feature in list_element['body'].lower().split()):
                    # Mark the value 1 at that index
                    feature_vector[value_feature] = 1
            else:
                if (key_feature.lower() in list_element['subject'].lower() or key_feature in list_element['body'].lower()):
                    # Mark the value 1 at that index
                    feature_vector[value_feature] = 1     
        if list_element['compliantFlag'] == False:
            y = 0
        else:
            y = 1
        feature_vectors.append(feature_vector)
        target_values.append(y)
        modified_feature_vector = feature_vector + list(str(y))
        modified_feature_vectors.append(modified_feature_vector)
#         print feature_vector
#         print y
#         print modified_feature_vector
    
    assert_equal(len(feature_vectors), len(target_values))
    
    #Shuffling the data for training and testing test
    random.shuffle(modified_feature_vectors)
    
    #Separating out training and testing data
    train_data = modified_feature_vectors[:178945]
    test_data = modified_feature_vectors[178945:]
    
    #For training data
    train_data_features = []
    train_data_targets = []
    
    for i in range(0,len(train_data)):
        train_data_features.append(train_data[i][:-1])
        train_data_targets.append(train_data[i][-1]) 
    
    #For testing data    
    test_data_features = []
    test_data_targets = []
            
    for i in range(0,len(test_data)):
        test_data_features.append(test_data[i][:-1])
        test_data_targets.append(test_data[i][-1]) 
    
    #Dumping 
    pickle.dump(train_data_features, open(SETTINGS.train_data_features, "wb"))
    pickle.dump(train_data_targets, open(SETTINGS.train_data_targets, "wb"))
    pickle.dump(test_data_features, open(SETTINGS.test_data_features, "wb"))
    pickle.dump(test_data_targets, open(SETTINGS.test_data_targets, "wb"))
    

if __name__ == "__main__":
    # execute locally
#     sorted_word_dict_unigram, sorted_word_dict_bigram, sorted_word_dict_trigram = create_ngram_dict()
#     dump_unigram(sorted_word_dict_unigram)
#     dump_bigram(sorted_word_dict_bigram)
#     dump_trigram(sorted_word_dict_trigram)
    
    # Execute this on remote server
#     feature_map = extract_feature_map()
    # execute locally
    create_feature_vector()
