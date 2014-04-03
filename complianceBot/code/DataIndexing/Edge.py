class Edge(object):
    
    def __init__(self, edge_id, source, target, label, epoch_secs, order, datetime, edge_type, start_datetime, end_datetime, evidence_type):
        self._edge_id = edge_id
        self._source = source
        self._target = target
        self._label = label
        self._epoch_secs = epoch_secs
        self._order = order
        self._datetime = datetime
        self._edge_type = edge_type 
        self._start_datetime = start_datetime
        self._end_datetime = end_datetime
        self._evidence_type = evidence_type
        
    @property
    def edge_id(self):
        return self._edge_id
    
    @edge_id.setter
    def edge_id(self, edge_id):
        self._edge_id = edge_id   

    @property
    def source(self):
        return self._source
    
    @source.setter
    def source(self, source):
        self._source = source
        
    @property
    def target(self):
        return self._target
    
    @target.setter
    def target(self, target):
        self._target = target
            
    @property
    def label(self):
        return self._label
    
    @label.setter
    def label(self, label):
        self._label = label   
        
    @property
    def epoch_secs(self):
        return self._epoch_secs
    
    @epoch_secs.setter
    def epoch_secs(self, epoch_secs):
        self._epoch_secs = epoch_secs      

    @property
    def order(self):
        return self._order
    
    @order.setter
    def order(self, order):
        self._order = order      
        
    @property
    def datetime(self):
        return self._datetime
    
    @datetime.setter
    def datetime(self, datetime):
        self._datetime = datetime      

    @property
    def edge_type(self):
        return self._edge_type
    
    @edge_type.setter
    def edge_type(self, edge_type):
        self._edge_type = edge_type    
        
    @property
    def start_datetime(self):
        return self._start_datetime
    
    @start_datetime.setter
    def start_datetime(self, start_datetime):
        self._start_datetime = start_datetime      
        
    @property
    def end_datetime(self):
        return self._end_datetime
    
    @end_datetime.setter
    def end_datetime(self, end_datetime):
        self._end_datetime = end_datetime      

    @property
    def evidence_type(self):
        return self._evidence_type
    
    @evidence_type.setter
    def evidence_type(self, evidence_type):
        self._evidence_type = evidence_type       
    