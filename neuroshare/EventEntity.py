
from Entity import *

class EventEntity(Entity):
    def __init__(self, nsfile, eid, info):
        super(EventEntity,self).__init__(eid, nsfile, info)

    @property
    def event_type(self):
        return self._info['EventType']

    @property
    def csv_desc(self):
        return self._info['CSVDesc']

    @property
    def max_data_length(self):
        return self._info['MaxDataLength']

    def get_data (self, index):
        lib = self.file.library
        data = lib._get_event_data (self, index)
        return data

