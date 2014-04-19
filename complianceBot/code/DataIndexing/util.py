import re
import SETTINGS

from Message import Message
from EmailAddress import EmailAddress
from Person import Person
from Edge import Edge

def extract_data(tree):
    GRAPH = "{http://graphml.graphdrawing.org/xmlns}graph"
    NODE = "{http://graphml.graphdrawing.org/xmlns}node"
    EDGE = "{http://graphml.graphdrawing.org/xmlns}edge"
    DATA = "{http://graphml.graphdrawing.org/xmlns}data"

    email_address_nodes = {}
    message_nodes = {}
    person_nodes = {}
    edges = {}
    
    # 'graphml' level
    root = tree.getroot()

    # 'graph' level
    for element in root:
        if element.tag == GRAPH:
            
            # 'node' and 'edge' level
            for node in element:
                if node.tag == NODE:
                    node_id = node.get('id')
                    epoch_secs = body = email_id = subject = datetime = None
                    for data in node.findall(DATA):

                        # Email Address related fields
                        if data.get('key') == 'address':
                            address = data.text
                        elif data.get('key') == 'fullyObserved':
                            fully_observed = data.text
                        
                        # Message related fields
                        elif data.get('key') == 'datetime':
                            datetime = data.text    
                        elif data.get('key') == 'epochSecs':
                            epoch_secs = data.text
                        elif data.get('key') == 'subject':
#                             subject = clean_data(data.text)
                            subject = data.text    
                        elif data.get('key') == 'body':
#                             body = clean_data(data.text)
                            body = data.text
                        elif data.get('key') == 'emailID':
                            email_id = data.text
                        
                        # Person related fields
                        elif data.get('key') == 'lastName':
                            lastname = data.text
                        elif data.get('key') == 'firstName':
                            firstname = data.text
                        elif data.get('key') == 'provenance':
                            provenance = data.text
                                
                    # Checking the message type
                    for data in node.findall(DATA):
                        if data.get('key') == 'type' and data.text == 'Email Address':
                            email_new_node = EmailAddress(node_id, address, fully_observed)

                            # Saving into dictionary with node_id as key
                            email_address_nodes[email_new_node._node_id] = email_new_node
                        elif data.get('key') == 'type' and data.text == 'Message':
                            message_new_node = Message(node_id, datetime, epoch_secs, subject, body, email_id)

                            # Saving into dictionary with node_id as key
                            message_nodes[message_new_node._node_id] = message_new_node
                        elif data.get('key') == 'type' and data.text == 'Person':
                            person_new_node = Person(node_id, lastname, firstname, provenance)

                            # Saving into dictionary with node_id as key
                            person_nodes[person_new_node._node_id] = person_new_node    

                elif node.tag == EDGE:
                    edge_id = node.get('id')
                    edge_source = node.get('source')
                    edge_target = node.get('target')
                    edge_label = node.get('label')
                     
                    epoch_secs = order = datetime = edge_type = start_datetime = end_datetime = evidence_type = None
                    for data in node.findall(DATA):
                        if data.get('key') == 'epochSecs':
                            epoch_secs = data.text
                        elif data.get('key') == 'order':
                            order = data.text
                        elif data.get('key') == 'datetime':
                            datetime = data.text
                        elif data.get('key') == 'type':
                            edge_type = data.text
                        elif data.get('key') == 'startDatetime':
                            start_datetime = data.text
                        elif data.get('key') == 'endDatetime':
                            end_datetime = data.text
                        elif data.get('key') == 'evidenceType':
                            evidence_type = data.text        
                            
                                      
                    new_edge = Edge(edge_id, edge_source, edge_target, edge_label, epoch_secs, order, datetime, edge_type, start_datetime, end_datetime, evidence_type)
                    edges[new_edge._edge_id] = new_edge
                        
    return message_nodes, email_address_nodes, person_nodes, edges


def clean_data(text):
    # Removing special characters
    text = re.sub("[\n\t\-\*\+\$\"\\\(\)\_\=]+", " ", text)
    
    # Removing tags
    text = re.sub('(<[^<]+>|<<[^<<]+>>)', "", text)
    text = re.sub("<<", " ", text)
    text = re.sub(">>", " ", text)
    text = re.sub("(<|>|#)", " ", text)
    
    # Removing time
    text = re.sub('([\d]+:\d\d) (AM|PM)', "", text)
    # Removing date
    text = re.sub('([\d]+/[\d]+/[\d]+)', "", text)
    text = re.sub('([\d]+\.[\d]+\.[\d]+)', "", text)
    text = re.sub('(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday){0,1},? (January|February|March|April|May|June|July|August|September|October|November|December){0,} [\d]*,? ?[\d]*', " ", text)
    # Removing labels
    text = re.sub('(From:|To:|Sent:|Cc:|cc:|Bcc:|RE:|Re:|FWD:|Subject:|Original Message)', "", text)
    # Removing urls
    text = re.sub('https?:\/\/.*? ', '', text)
    # Removing punctuations
    text = re.sub('[;\,\?\.\:\!]', " ", text)
    # Removing numbers
    text = re.sub('(0|1|2|3|4|5|6|7|8|9){1,}', "", text)
    # Removing email address
    
    # Removing rest
    text = re.sub('[/@]', " ", text)
    text = re.sub("'s", "", text)
    text = re.sub("\'", "", text)
    text = re.sub("\|", "", text)
    text = re.sub("\[image\]", "", text)
    # Removing stop words
    f = open(SETTINGS.stop_words_file)
    stop_words = f.read().splitlines()
    text = " ".join(word for word in text.split() if word.lower() not in stop_words)

    
    return text