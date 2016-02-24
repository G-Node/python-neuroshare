
from .Entity import Entity


class AnalogEntity(Entity):
    """:class:`Entity` that represents continuously sampled, i.e. digitized, analog data.
    Examples are waveforms recorded via an electrode (microelectrodes, EKG, EEG).
    Actual data can be accessed via the :func:`get_data` function.
    .. note:: data may contain gaps (e.g. when no data is recorded between trails)
    """
    def __init__(self, nsfile, eid, info):
        super(AnalogEntity, self).__init__(eid, nsfile, info)

    @property
    def sample_rate(self):
        """Sampling rate (in Hz)."""
        return self._info['SampleRate']

    @property
    def min_value(self):
        """Minimum value of the data"""
        return self._info['MinVal']

    @property
    def max_value(self):
        """Maximum value of the data"""
        return self._info['MaxVal']

    @property
    def resolution(self):
        """Minimal resolvable step size"""
        return self._info['Resolution']

    @property
    def units(self):
        """Physical units of measured data"""
        return self._info['Units']

    @property
    def location_x(self):
        """x coordinate of the source [in meters]"""
        return self._info['LocationX']

    @property
    def location_y(self):
        """y coordinate of the source [in meters]"""
        return self._info['LocationY']

    @property
    def location_z(self):
        """z coordinate of the source [in meters]"""
        return self._info['LocationZ']

    @property
    def location_user(self):
        """Hardware specific additional location information"""
        return self._info['LocationUser']

    @property
    def high_freq_corner(self):
        """High frequency cutoff [in Hz] of the filter"""
        return self._info['HighFreqCorner']

    @property
    def high_freq_order(self):
        """Order of the high frequency filter"""
        return self._info['HighFreqOrder']

    @property
    def high_filter_type(self):
        """Type of the filter used [text]"""
        return self._info['HighFilterType']

    @property
    def low_freq_corner(self):
        """Low frequency cutoff [in Hz] of the filter"""
        return self._info['LowFreqCorner']

    @property
    def low_freq_order(self):
        """Order of the high frequency filter"""
        return self._info['LowFreqOrder']

    @property
    def low_filter_type(self):
        """Type of the filter used [text]"""
        return self._info['LowFilterType']

    @property
    def probe_info(self):
        """Additional information"""
        return self._info['ProbeInfo']

    def get_data(self, index=0, count=-1):
        """Retrieve raw data from file starting at ``index`` up to ``count`` elements.
        If no parameters are given retrieves all available data.

        Returns a tuple with three elements containing the raw data ``[0]``, the timestamp
        of each data point ``[1]`` and how many of the data values are continuous ``[2]``.
        Example use: ``data, times, count = analog1.get_data()``

        Raw data and timestamp data are return as :class:`numpy.ndarray`.
        """
        if count < 0:
            count = self.item_count

        lib = self.file.library
        data = lib._get_analog_data(self, index, count)
        return data
