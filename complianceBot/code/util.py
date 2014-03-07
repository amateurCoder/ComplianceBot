from Message import Message
from EmailAddress import EmailAddress
from Person import Person

def extract_data(tree):
    email_address_nodes = {}
    message_nodes = {}
    person_nodes = {}
    
    #'graphml' level
    root = tree.getroot()
    #'graph' level
    for element in root:
        if element.tag == 'graph':
            print element.tag, element.attrib
            #'node' and 'edge' level
            for node in element:
                if node.tag == 'node':
                    node_id = node.get('id')
                    epoch_secs = body = email_id = subject = None
                    datetime = None
                    
                    #retrieving values from all field
                    for data in node.findall('data'):
                        
                        #Email Address related fields
                        if data.get('key') == 'address':
                            address = data.text
                        elif data.get('key') == 'fullyObserved':
                            fully_observed = data.text
                        
                        #Message related fields
                        elif data.get('key') == 'datetime':
                            datetime = data.text    
                        elif data.get('key') == 'epochSecs':
                            epoch_secs = data.text
                        elif data.get('key') == 'subject':
                            subject = data.text    
                        elif data.get('key') == 'body':
                            body = data.text
                        elif data.get('key') == 'emailID':
                            email_id = data.text
                        
                        #Person related fields
                        elif data.get('key') == 'lastName':
                            lastname = data.text    
                        elif data.get('key') == 'firstName':
                            firstname = data.text
                        elif data.get('key') == 'provenance':
                            provenance = data.text
                                
                    #Checking the message type
                    for data in node.findall('data'):
                        if data.get('key') == 'type' and data.text == 'Email Address':
                            new_node = EmailAddress(node_id, address, fully_observed)
                            #Saving into dictionary with node_id as key
                            email_address_nodes[new_node._node_id] = new_node
                        elif data.get('key') == 'type' and data.text == 'Message':
                            new_node = Message(node_id, datetime, epoch_secs, subject, body, email_id)
                            #Saving into dictionary with node_id as key
                            message_nodes[new_node._node_id] = new_node
                        elif data.get('key') == 'type' and data.text == 'Person':
                            new_node = Person(node_id, lastname, firstname, provenance)
                            #Saving into dictionary with node_id as key
                            person_nodes[new_node._node_id] = new_node    
                        
                    
                    #print new_node._node_id, new_node._epoch_secs, new_node._body, new_node._email_id, new_node._subject, new_node._datetime
                    
    return message_nodes, email_address_nodes, person_nodes