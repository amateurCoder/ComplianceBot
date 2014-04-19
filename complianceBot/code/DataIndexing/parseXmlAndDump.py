import xml.etree.ElementTree as ET
import pickle

import SETTINGS

import util

def read_and_dump_data():
    tree = ET.parse(SETTINGS.file_name)
    message_nodes, email_address_nodes, person_nodes, edges = util.extract_data(tree)
    
    #writing parsed objects to the file
    pickle.dump(message_nodes, open(SETTINGS.message_object_file, "wb"))
    pickle.dump(email_address_nodes, open(SETTINGS.email_object_file, "wb"))
    pickle.dump(person_nodes, open(SETTINGS.person_object_file, "wb"))
    pickle.dump(edges, open(SETTINGS.edge_object_file, "wb"))

    #for key, value in message_loaded_nodes.iteritems():
        #print loaded_node._node_id, loaded_node._epoch_secs, loaded_node._body, loaded_node._email_id, loaded_node._subject, loaded_node._datetime
        #print key, value._epoch_secs



if __name__=="__main__":
    read_and_dump_data()