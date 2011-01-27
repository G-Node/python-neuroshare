
class EntityTime(object):
    Closest = 0
    Before = -1
    After = 1

class Entity(object):
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
        return self._file.library._get_time_by_index (self, index)

    def get_index_by_time(self, timepoint, position=EntityTime.Closest):
        return self._file.library._get_index_by_time (self, timepoint, position)
    
class EntityType(object):
    Unkown = 0
    Event = 1
    Analog = 2
    Segment = 3
    Neural = 4
    

