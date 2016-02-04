
from .Entity import Entity


class EventEntity(Entity):
    """Event entities represent specific timepoints with associated data,
    e.g. trigger events. Data can be binary (8, 16 or 32 bit) values, text
    or comma separated values (cvs).
    """
    EVENT_TEXT  = 1
    EVENT_CSV   = 2
    EVENT_BYTE  = 3
    EVENT_WORD  = 4
    EVENT_DWORD = 5

    def __init__(self, nsfile, eid, info):
        super(EventEntity, self).__init__(eid, nsfile, info)

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
        """Description of the csv fields"""
        return self._info['CSVDesc']

    @property
    def max_data_length(self):
        """Maximum length of the data for the event [in bytes]"""
        return self._info['MaxDataLength']

    @property
    def min_data_length(self):
        """Minimum length of the data for the event [in bytes]"""
        return self._info['MinDataLength']

    def get_data(self, index):
        """Retrieve the data at ``index``. Returns a 2-tuple with the
        timestamp of the data at the first position (``[0]``) and the
        actual data a the second position (``[1]``)).
        Example use: ``timestamp, data = event.get_data(0)``"""
        lib = self.file.library
        data = lib._get_event_data(self, index)
        return data
