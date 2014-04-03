import sunburnt
import operator
import unicodedata


def extract_features():
    word_dict={}
    #contains the list of results
    result_list = []
    sMessage = sunburnt.SolrInterface("http://localhost:8983/solr/message/")
    for result in sMessage.query(text="*").field_limit(["body", "subject"]).paginate(start=0, rows=10).execute():
        result_list.append(result)
    
    for list_element in result_list:    
        #for body and subject type
        for key, value in list_element.iteritems():
            #Converting unicode to string
            value = unicodedata.normalize('NFKD', value).encode('ascii','ignore')
            put_ngram_word(word_dict, value)
    
    sorted_word_dict = sorted(word_dict.iteritems(), key=operator.itemgetter(1), reverse=True) 
    #TODO Need to write it to disk
    print sorted_word_dict 
    
    
def put_ngram_word(word_dict, value):
    #n = 1,2,3
    for n in range(1, 4):
        splitted_value = value.split()
        #creating list of n grams
        temp_list = [' '.join(splitted_value[x:x+n]) for x in xrange(0, len(splitted_value), n)]
        for element in temp_list:
            add_to_dictionary(word_dict, element)   

def add_to_dictionary(word_dict, element):
    if element in word_dict:
        word_dict[element]+=1
    else:
        word_dict[element]=1    


if __name__ == "__main__":
    extract_features()