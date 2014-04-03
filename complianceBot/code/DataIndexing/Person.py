class Person(object):
    
    def __init__(self, node_id, last_name, first_name, provenance):
        self._node_id = node_id
        self._last_name = last_name
        self._first_name = first_name
        self._provenance = provenance
        
    @property
    def node_id(self):
        return self._node_id
    
    @node_id.setter
    def node_id(self, node_id):
        self._node_id = node_id   

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name
        
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name
            
    @property
    def provenance(self):
        return self._provenance
    
    @provenance.setter
    def provenance(self, provenance):
        self._provenance = provenance   
