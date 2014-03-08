class EmailAddress(object):
    
    def __init__(self, node_id, address, fully_observed):
        self._node_id = node_id
        self._address = address
        self._fully_observed = fully_observed
        
    @property
    def node_id(self):
        return self._node_id
    
    @node_id.setter
    def node_id(self, node_id):
        self._node_id = node_id   
            
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, address):
        self._address = address
        
    @property
    def fully_observed(self):
        return self._fully_observed
    
    @fully_observed.setter
    def fully_observed(self, fully_observed):
        self._fully_observed = fully_observed   
