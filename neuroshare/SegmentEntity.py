from .Entity import Entity


class SegmentSource(object):
    """Segment sources provide access to the metadata of individual sources
    of a :class:`SegmentEntity`"""
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
        """x coordinate [in meters]"""
        return self._info['LocationX']

    @property
    def location_y(self):
        """y coordinate [in meters]"""
        return self._info['LocationY']

    @property
    def location_z(self):
        """z coordinate [in meters]"""
        return self._info['LocationZ']

    @property
    def location_user(self):
        """Additional hardware specific location information"""
        return self._info['LocationUser']

    @property
    def high_freq_corner(self):
        return self._info['HighFreqCorner']

    @property
    def high_freq_order(self):
        return self._info['HighFreqOrder']

    @property
    def high_filter_type(self):
        return self._info['HighFilterType']

    @property
    def low_freq_corner(self):
        return self._info['LowFreqCorner']

    @property
    def low_freq_order(self):
        return self._info['LowFreqOrder']

    @property
    def low_filter_type(self):
        return self._info['LowFilterType']

    @property
    def probe_info(self):
        """Additional information"""
        return self._info['ProbeInfo']


class SourcesBag(object):
    def __init__(self, segment, infos):
        self._infos = infos
        self._segment = segment

    def __getitem__(self, key):
        source_id = int(key)
        source_info = self._infos[source_id]
        return SegmentSource(self._segment, source_id, source_info)

    def __iter__(self):
        for x in range(0, len(self._infos)):
            yield self[x]


class SegmentEntity(Entity):
    """Segment entities contain cutouts of continuously sampled analog signals from
    one or more sources that are usually short in time. Most prominent example are
    waveforms of action potentials from one ore more electrodes."""
    def __init__(self, nsfile, eid, info):
        from copy import copy
        self._source_infos = info['SourceInfos']
        pure_info = copy(info)
        del pure_info['SourceInfos']
        super(SegmentEntity, self).__init__(eid, nsfile, pure_info)

    @property
    def max_sample_count(self):
        """Maximum number of samples in each data item"""
        return self._info['MaxSampleCount']

    @property
    def source_count(self):
        """Number of sources for this segment entity."""
        return self._info['SourceCount']

    @property
    def sources(self):
        """Property that provides access to the metadata of the individual
        sources of this entity.

        Returns a sequence of objects of type :class:`SegmentSource`.
        Metadata properties of a SegmentSource are analogous to the
        :class:`AnalogEntity`."""
        return SourcesBag(self, self._source_infos)

    def get_data(self, index):
        """Retrieve the data at ``index``.

        Returns:

        data : numpy.ndarray
            The Segment data.
        timestamp : float
            Time stamp of the Segment data.
        sample_count : int
            How many sample points were obtained.
        unit_id : int
            Classification of the unit. A bit field (32 bits) where bit `0`
            indicates if the segment is noise or artifact data, bit `n`
            in the range of 1..32 indicates the unit n was present.
        """
        lib = self.file.library
        data = lib._get_segment_data(self, index)
        return data
