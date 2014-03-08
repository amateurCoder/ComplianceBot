import xml.etree.ElementTree as ET
import pickle

import SETTINGS

import util

def read_data():
    tree = ET.parse(SETTINGS.file_name)
    message_nodes, email_address_nodes, person_nodes, edges = util.extract_data(tree)
    
    #writing parsed objects to the file
    pickle.dump(message_nodes, open("messageObjectFile.p", "wb"))
    pickle.dump(email_address_nodes, open("emailObjectFile.p", "wb"))
    pickle.dump(person_nodes, open("personObjectFile.p", "wb"))
    pickle.dump(edges, open("edgeObjectFile.p", "wb"))

#TODO: Indexing to Solr in a specified format    
#     message_loaded_nodes = pickle.load(open("messageObjectFile.p", "rb"))
#     email_address_loaded_nodes = pickle.load(open("emailObjectFile.p", "rb"))
#     person_loaded_nodes = pickle.load(open("personObjectFile.p", "rb"))
#     
    
    #for key, value in message_loaded_nodes.iteritems():
        #print loaded_node._node_id, loaded_node._epoch_secs, loaded_node._body, loaded_node._email_id, loaded_node._subject, loaded_node._datetime
        #print key, value._epoch_secs



if __name__=="__main__":
    read_data()