from .Entity import Entity


class NeuralEntity(Entity):
    """Entity the represents timestamps of action potentials, i.e. spike times.
    Cutouts of the waveforms corresponding to spike data in a neural entity
    might be found in a separate :class:`SegmentEntity` (cf. :func:`source_entity_id`).
    """
    def __init__(self, nsfile, eid, info):
        super(NeuralEntity, self).__init__(eid, nsfile, info)

    @property
    def probe_info(self):
        """Additional information about the signal source"""
        return self._info['ProbeInfo']

    @property
    def source_entity_id(self):
        """[*Optional*] Id of the source entity of this spike, if any.
        For example the spike waveform of the action potential corresponding
        to this spike might have been recorded in a segment entity."""
        return self._info['SourceEntityID']

    @property
    def source_unit_id(self):
        """[*Optional*] unit id used in the source entity
        (cf. :func:`source_entity_id`)"""
        return self._info['SourceUnitID']

    def get_data(self, index=0, count=-1):
        """Retrieve the spike times associated with this entity. A subset
        of the data can be requested via the ``index`` and ``count``
        parameters."""
        lib = self.file.library
        if count < 0:
            count = self.item_count
        data = lib._get_neural_data(self, index, count)
        return data
