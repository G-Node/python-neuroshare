
from Library import *
from Entity import *
from EventEntity import *
from AnalogEntity import *
from SegmentEntity import *
from NeuralEntity import *

class EntityProxy(object):
    def __init__(self, nsfile):
        self._nsfile = nsfile

    def __getitem__(self, key):
       return self._nsfile.get_entity(key)

    def __iter__(self):
        for x in xrange (0, self._nsfile.entity_count):
            yield self[x]

class File(object):

    def __init__(self, filename, library=None):
        self._handle = None
        self._filename = filename
        if not library:
            library = load_library_for_file (filename)

        self._lib = library
        (handle, info) = self._lib._open_file (filename)
        self._handle = handle
        self._info = info
        self._eproxy = EntityProxy(self)

    def __del__(self):
        self.close ()

    def close(self):
        if self._handle:
            self._lib._close_file (self)
            self._handle = None

    @property
    def library(self):
        return self._lib

    @property
    def file_type(self):
        pass

    @property
    def app_name(self):
        return self._info['AppName']

    @property
    def comment(self):
        return self._info['FileComment']

    @property
    def entity_count(self):
        return self._info['EntityCount']

    @property
    def time_span(self):
        return self._info['TimeSpan']

    @property
    def time_stamp_resolution(self):
        return self.info['TimeStampResolution']

    @property
    def ctime(self):
        from datetime import datetime

        year = self._info['Time_Year']
        month = self._info['Time_Month']
        day = self._info['Time_Day']
        hour = self._info['Time_Hour']
        minute = self._info['Time_Min']
        sec = self._info['Time_Sec']
        millisec = self._info['Time_MilliSec']

        msec = millisec * 1000
        ct = datetime (year, month, day, hour, minute, sec, msec)
        return ct


    def get_entity(self, entity_id):

        info = self._lib._get_entity_info (self, entity_id)
        entity_type = info['EntityType']

        if entity_type == EntityType.Event:
            entity = EventEntity(self, entity_id, info)
        elif entity_type == EntityType.Analog:
            entity = AnalogEntity(self, entity_id, info)
        elif entity_type == EntityType.Segment:
            entity = SegmentEntity(self, entity_id, info)
        elif entity_type == EntityType.Neural:
            entity = NeuralEntity(self, entity_id, info)
        else:
            return None #should not happen, throw exception?

        return entity

    def list_entities(self, start=0, end=-1):
        if end == -1:
            end = self.entity_count
        
        for x in xrange (start, end):
            yield self.get_entity(x)

    @property
    def entities(self):
        return self._eproxy

    @property
    def _get_handle(self):
        return self._handle

    def __repr__(self):
        return 'neuroshare.File(%r)' % (self._filename)
