import pickle
import sunburnt

import SETTINGS

def load_filter_words():
    drinks_words = read_file(SETTINGS.drinks_file)
    hostile_environment_words = read_file(SETTINGS.hostile_environment_file) 
    personal_words = read_file(SETTINGS.personal_file) 
    sports_words = read_file(SETTINGS.sports_file)
    #other_words = read_file(SETTINGS.others_file)
    
    return drinks_words + hostile_environment_words + personal_words + sports_words #+ other_words


def read_file(filepath):
    with open(filepath) as f:
        return f.read().splitlines()    

def read_objects_from_disk_and_index():
    # Indexing to Solr in a specified format    
    
    
    #index_person()
    #index_email_address()
    index_message()
    #index_edges()
     
    # print message_loaded_nodes, email_loaded_nodes, person_loaded_nodes, edge_loaded_nodes
#     for key, value in person_loaded_nodes.iteritems():
#         print key, value._node_id, value._last_name, value._first_name, value._provenance
    

def index_person():
    person_loaded_nodes = pickle.load(open(SETTINGS.person_object_file, "rb"))
    sPerson = sunburnt.SolrInterface("http://localhost:8983/solr/person/")
    docs = []
    for key, value in person_loaded_nodes.iteritems():
        doc = {"nodeId":key, "lastname":value._last_name, "firstname":value._first_name, "provenance":value._provenance}
        docs.append(doc)
        
    sPerson.add(docs)
    sPerson.commit()    
    
def index_email_address():    
    email_loaded_nodes = pickle.load(open(SETTINGS.email_object_file, "rb"))
    sEmail = sunburnt.SolrInterface("http://localhost:8983/solr/emailAddress/")
    docs = []
    for key, value in email_loaded_nodes.iteritems():
        doc = {"nodeId":key, "address":value._address, "fullyObserved":value._fully_observed}
        docs.append(doc)
        
    sEmail.add(docs)
    sEmail.commit()    


def index_message():    
    filter_words = load_filter_words()
    message_loaded_nodes = pickle.load(open(SETTINGS.message_object_file, "rb"))
    sPerson = sunburnt.SolrInterface("http://localhost:8983/solr/message/")
    docs = []
    for key, value in message_loaded_nodes.iteritems():
        
        #Checking if the subject or body contains filter words (non-compliant words)
        compliantFlag= True
        
        #NoneType check
        if value._subject == None:
            text = value._body
        elif value._body == None:
            text = value._subject
        else:
            text = value._subject + value._body
                    
        if is_filter_word_present(text, filter_words):
            compliantFlag = False 

        doc = {"nodeId":key, "datetime":value._datetime, "epochSecs":value._epoch_secs, "subject":value._subject, "body":value._body, "emailId":value._email_id,"compliantFlag":compliantFlag}
        docs.append(doc)
        
    sPerson.add(docs)
    sPerson.commit()    
        

#To check if the body or subject of message contains a non-compliant word         
def is_filter_word_present(text, filter_words):
    for word in filter_words:
#         if word in text:
        if word in (wordText.lower() for wordText in text):
            return True

        
def index_edges():
    edge_loaded_nodes = pickle.load(open(SETTINGS.edge_object_file, "rb"))
    sEdges = sunburnt.SolrInterface("http://localhost:8983/solr/edge/")
    docs = []
    for key, value in edge_loaded_nodes.iteritems():
        doc = {"edgeId":key, "source":value._source, "target":value._target, "label":value._label, "epochSecs":value._epoch_secs, "order":value._order, "datetime":value._datetime, "edgeType":value._edge_type, "startDatetime":value._start_datetime, "endDatetime":value._end_datetime, "evidenceType":value._evidence_type}
        docs.append(doc)
        
    sEdges.add(docs)
    sEdges.commit()  
        
if __name__ == "__main__":
    read_objects_from_disk_and_index()
