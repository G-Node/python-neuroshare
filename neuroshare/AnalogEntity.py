
from Entity import Entity

class AnalogEntity(Entity):
    def __init__(self, nsfile, eid, info):
        super(AnalogEntity,self).__init__(eid, nsfile, info)

    @property
    def sample_rate(self):
        return self._info['SampleRate']

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
    def units(self):
        return self._info['Units']

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

    def get_data (self, index=0, count=-1):
        if count < 0:
            count = self.item_count

        lib = self.file.library
        data = lib._get_analog_data (self, index, count)
        return data
