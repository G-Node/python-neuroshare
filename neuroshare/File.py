
from .Library import Library
from .Entity import EntityType
from .EventEntity import EventEntity
from .AnalogEntity import AnalogEntity
from .SegmentEntity import SegmentEntity
from .NeuralEntity import NeuralEntity


class EntityProxy(object):
    def __init__(self, nsfile):
        self._nsfile = nsfile

    def __getitem__(self, key):
        return self._nsfile.get_entity(key)

    def __iter__(self):
        for x in range(0, self._nsfile.entity_count):
            yield self[x]

    def __len__(self):
        return self._nsfile.entity_count


class File(object):
    """Object that represents a datafile that can be open via neuroshare at
    the location given by ``filename``. The file will be opened upon object
    construction.

    Individual entities can be opened via the :func:`get_entity` function or
    the :func:`entities` property. NB: The first entity index is **0**
    """

    def __init__(self, filename, library=None):
        self._handle = None
        self._filename = filename
        if not library:
            library = Library.for_file(filename)

        self._lib = library
        (handle, info) = self._lib._open_file(filename)
        self._handle = handle
        self._info = info
        self._eproxy = EntityProxy(self)

    def __del__(self):
        self.close()

    def close(self):
        """Close the file."""
        if self._handle:
            self._lib._close_file(self)
            self._handle = None

    @property
    def library(self):
        return self._lib

    @property
    def file_type(self):
        """Text description of the file type"""
        return self._info['FileType']

    @property
    def metadata_raw(self):
        return self._info

    @property
    def app_name(self):
        """The name of the application that created the file"""
        return self._info['AppName']

    @property
    def comment(self):
        """Additional comments"""
        return self._info['FileComment']

    @property
    def entity_count(self):
        """The number of entities in this file"""
        return self._info['EntityCount']

    @property
    def time_span(self):
        """Timespan of the data in the file [in seconds]"""
        return self._info['TimeSpan']

    @property
    def time_stamp_resolution(self):
        """Minimum resolution of timestamps [in seconds]"""
        return self._info['TimeStampResolution']

    @property
    def ctime(self):
        """The time when this file was created, i.e. the data recorded.
        Returns a :py:class:`datetime.datetime` object.
        """
        from datetime import datetime

        year = self._info['Time_Year']
        month = self._info['Time_Month']
        day = self._info['Time_Day']
        hour = self._info['Time_Hour']
        minute = self._info['Time_Min']
        sec = self._info['Time_Sec']
        millisec = self._info['Time_MilliSec']

        msec = millisec * 1000
        ct = datetime(year, month, day, hour, minute, sec, msec)
        return ct

    def get_entity(self, entity_id):
        """Open the entity at the given index."""
        info = self._lib._get_entity_info(self, entity_id)
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
            return None  # should not happen, throw exception?

        return entity

    def list_entities(self, start=0, end=-1):
        """List all entities. The range can be limited
        via the ``start`` and ``end`` parameters."""
        if end == -1:
            end = self.entity_count

        for x in range(start, end):
            yield self.get_entity(x)

    @property
    def entities(self):
        """Property that returns a proxy object to allow the opening of
        entities in a via indexing, ie::

            entity = datafile.entities[10] #retrieve the entity with at 10
        """
        return self._eproxy

    @property
    def _get_handle(self):
        return self._handle

    @property
    def handle(self):
        return self._handle

    def __repr__(self):
        return 'neuroshare.File(%r)' % self._filename
