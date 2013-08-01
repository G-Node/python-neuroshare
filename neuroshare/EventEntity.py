
from Entity import *

class EventEntity(Entity):
    """Event entities represent specific timepoints with associated data,
    e.g. a trigger events. Data can be binary (8, 16 or 32 bit) values, text
    or comma separated values (cvs).
    """
    EVENT_TEXT  = 1
    EVENT_CSV   = 2
    EVENT_BYTE  = 3
    EVENT_WORD  = 4
    EVENT_DWORD = 5

    def __init__(self, nsfile, eid, info):
        super(EventEntity,self).__init__(eid, nsfile, info)

    @property
    def event_type(self):
        """The type of the event:

        * binary (8, 16, 32 bit) [``EVENT_BYTE, EVENT_WORD, EVENT_DWORD``]
        * text                   [``EVENT_TEXT``]
        * comma separated values (csv) [``EVENT_CSV``]
        """
        return self._info['EventType']

    @property
    def csv_desc(self):
        return self._info['CSVDesc']

    @property
    def max_data_length(self):
        return self._info['MaxDataLength']

    @property
    def min_data_length(self):
        """Minimum lenght of the data for the event [in bytes]"""
        return self._info['MinDataLength']

    def get_data (self, index):
        """Retrieve the data at ``index``"""
        lib = self.file.library
        data = lib._get_event_data (self, index)
        return data

