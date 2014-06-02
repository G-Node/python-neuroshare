
class EntityTime(object):
    Closest = 0
    Before = -1
    After = 1


class Entity(object):
    """Base class of all entities that are contained in a neuroshare file
    """
    def __init__(self, entity_id, nsfile, entity_info):
        self._info = entity_info
        self._id = entity_id
        self._file = nsfile

    @property
    def id(self):
        """The entity id of this entity"""
        return self._id

    @property
    def file(self):
        """The underlying data file of this entity"""
        return self._file

    @property
    def metadata_raw(self):
        return self._info

    @property
    def label(self):
        """The label or name of the entity"""
        return self._info['EntityLabel']

    @property
    def entity_type(self):
        """The type of the entity (of EntityType)"""
        return self._info['EntityType']

    @property
    def item_count(self):
        """ Number of data items for the specified entity in the file"""
        return self._info['ItemCount']

    def get_time_by_index(self, index):
        """Convert from a given index to the corresponding timestamp"""
        return self._file.library._get_time_by_index(self, index)

    def get_index_by_time(self, timepoint, position=EntityTime.Closest):
        """Convert from a given timestamp to the corresponding index.
        The position argument controls how the timestamp is matched to the index.
        Options are:

        * before and inclusive of the timepoint (``EntityTime.Before``)
        * after and inclusive of the timepoint (``EntityTime.After``)
        * closest to timepoint (``EntityTime.Closest``) [default]
        """
        return self._file.library._get_index_by_time(self, timepoint, position)

    def __len__(self):
        return self.item_count


class EntityType(object):
    Unknown = 0
    Unkown = 0
    Event = 1
    Analog = 2
    Segment = 3
    Neural = 4
