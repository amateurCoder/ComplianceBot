class Message(object):
    
    def __init__(self, node_id, datetime, epoch_secs, subject, body, email_id):
        self._node_id = node_id
        self._datetime = datetime
        self._epoch_secs = epoch_secs
        self._subject = subject
        self._body = body
        self._email_id = email_id
        
        
    @property
    def node_id(self):
        return self._node_id
    
    @node_id.setter
    def node_id(self, node_id):
        self._node_id = node_id   
            
    @property
    def datetime(self):
        return self._datetime
    
    @datetime.setter
    def datetime(self, datetime):
        self._datetime = datetime   
                    
    @property
    def epoch_secs(self):
        return self._epoch_secs
    
    @epoch_secs.setter
    def epoch_secs(self, epoch_secs):
        self._epoch_secs = epoch_secs
    
    @property
    def subject(self):
        return self._subject
    
    @subject.setter
    def subject(self, subject):
        self._subject = subject
    
    @property
    def body(self):
        return self._body
    
    @body.setter
    def body(self, body):
        self._body = body   
        
    @property
    def email_id(self):
        return self._email_id
    
    @email_id.setter
    def email_id(self, email_id):
        self._email_id = email_id   
                
