from Entity import *

class SegmentSource(object):
    def __init__(self, segment, source_id, info):
        self._segment = segment
        self._source_id = source_id
        self._info = info

    @property
    def segment(self):
        return self._segment

    @property
    def id(self):
        return self._source_id

    @property
    def metadata_raw(self):
        return self._info

    @property
    def min_value(self):
        return self._info['MinVal']

    @property
    def max_value(self):
        return self._info['MaxVal']

    @property
    def resolution(self):
        return self._info['Resolution']
    
    @property
    def sub_sample_shift(self):
        return self._info['SubSampleShift']

    @property
    def location_x(self):
        return self._info['LocationX']

    @property
    def location_y(self):
        return self._info['LocationY']

    @property
    def location_z(self):
        return self._info['LocationZ']

    @property
    def location_user(self):
        return self._info['LocationUser']

    @property
    def high_freq_corner(self):
        return self._info['HighFreqOrder']
    
    @property
    def high_freq_order(self):
        return self._info['HighFreqOrder']
    
    @property
    def high_filter_type(self):
        return self._info['HighFilterType']

    @property
    def low_freq_corner(self):
        return self._info['LowFreqOrder']
    
    @property
    def low_freq_order(self):
        return self._info['LowFreqOrder']
    
    @property
    def low_filter_type(self):
        return self._info['LowFilterType']

    @property
    def probe_info(self):
        return self._info['ProbeInfo']


class SourcesBag(object):
    def __init__(self, segment, infos):
        self._infos = infos
        self._segment = segment

    def __getitem__(self, key):
        source_id = int (key)
        source_info = self._infos[source_id]
        return SegmentSource (self._segment, source_id, source_info)

    def __iter__(self):
        for x in range(0, len (self._infos)):
            yield self[x]
        

class SegmentEntity(Entity):
    def __init__(self, nsfile, eid, info):
        super(SegmentEntity,self).__init__(eid, nsfile, info)

    @property
    def max_sample_count(self):
        return self._info['MaxSampleCount']

    @property
    def source_count(self):
        return self._info['SourceCount']

    @property
    def sources(self):
        return SourcesBag(self, self._info['SourceInfos'])

    def get_data (self, index):
        lib = self.file.library
        data = lib._get_segment_data (self, index)
        return data


