# Data model mapping between Neuroshare and NIX

## Structure of Data
- The main_block entity is a top-level, summarizing element that groups the other data entities belonging to the same recording session.
- Every entity exists as an group inside the main_block.
- Thus there are four groups:
                            1: 'Event',
                            2: 'Analog',
                            3: 'Segment',
                            4: 'Neural'
- Every group contains the data arrays corresponding to that entity i.e. every data array is appended to an appropriate group.

## Structure for metadata
- The metadata is stored in top level section named same as the input file.
- The section contains four sub-section:
                            1: 'events',
                            2: 'analogs',
                            3: 'segments',
                            4: 'neurals'
- The metadata for every data array in a group(except segments) is added to the respective sub-section as listed above.
 -  The sub-sections of individual segments contain the metadata for the segment.
 -  The segments sub-section contains the metadata of every segment in sub-sections named after those segments(segment.label).
 -  The sub-sections of individual segments contain the metadata for individual dataArrays of the segment as their sub-sections.
 -  The sub-sections of individual segments contain the metadata for all the sources of segment as its sub-section (Ex. 'SourceInfo.0').
 
## neuroshare.File
Does not directly map to but is analogous nix.File .
The top level data container of the nix.File object is a block entity. In our case lets call it main_block.

## main_block
The main_block entity is a top-level, summarizing element that allows to group the other data entities belonging for example to the same recording session.
Since all the data in a neuroshare file is from a single recording thus all the data in the resulting nix file is added as a child to the block named same as the input file.

## neuroshare.EventEntity
Maps directly to a nix group containing the event data stored in a data array with the timestamps as the ticks of dimension descriptor.
- Attributes

    | Neuroshare                    | NIX                                        |
    |-------------------------------|--------------------------------------------|
    | EventEntity.csv_desc          |DataArray.metadata(*Section*)(#SectionNotes)|
    | EventEntity.event_type        |DataArray.metadata(*Section*)(#SectionNotes)|
    | EventEntity.max_data_length   |DataArray.metadata(*Section*)(#SectionNotes)|
    | EventEntity.min_data_length   |DataArray.metadata(*Section*)(#SectionNotes)|
    * Attribute names in Nix can be accessed by camel case equivalents of those in Neuroshare.

## neuroshare.AnalogEntity
Maps directly to a nix group containing the analog data stored in a data array with the timestamps as the ticks of the dimension descriptor.
- Attributes

    | Neuroshare                    | NIX                                        |
    |-------------------------------|--------------------------------------------|
    | AnalogEntity.high_filter_type |DataArray.metadata(*Section*)(#SectionNotes)|
    | AnalogEntity.high_freq_corner |DataArray.metadata(*Section*)(#SectionNotes)|
    | AnalogEntity.high_freq_order  |DataArray.metadata(*Section*)(#SectionNotes)|
    | AnalogEntity.location_user    |DataArray.metadata(*Section*)(#SectionNotes)|
    | AnalogEntity.location_x       |DataArray.metadata(*Section*)(#SectionNotes)|
    | AnalogEntity.location_y       |DataArray.metadata(*Section*)(#SectionNotes)|
    | AnalogEntity.location_z       |DataArray.metadata(*Section*)(#SectionNotes)|
    | AnalogEntity.low_filter_type  |DataArray.metadata(*Section*)(#SectionNotes)|
    | AnalogEntity.low_freq_corner  |DataArray.metadata(*Section*)(#SectionNotes)|
    | AnalogEntity.low_freq_order   |DataArray.metadata(*Section*)(#SectionNotes)|
    | AnalogEntity.max_value        |DataArray.metadata(*Section*)(#SectionNotes)|
    | AnalogEntity.min_value        |DataArray.metadata(*Section*)(#SectionNotes)|
    | AnalogEntity.probe_info       |DataArray.metadata(*Section*)(#SectionNotes)|
    | AnalogEntity.resolution       |DataArray.metadata(*Section*)(#SectionNotes)|
    | AnalogEntity.sample_rate      |DataArray.metadata(*Section*)(#SectionNotes)|
    | AnalogEntity.units            |DataArray.metadata(*Section*)(#SectionNotes)|
    * Attribute names in Nix can be accessed by camel case equivalents of those in Neuroshare.

## neuroshare.NeuralEntity
Maps directly to a nix group containing the neural data stored in a data array.
- Attributes

    | Neuroshare                    | NIX                                        |
    |-------------------------------|--------------------------------------------|
    | NeuralEntity.probe_info       |DataArray.metadata(*Section*)(#SectionNotes)|
    | NeuralEntity.source_entity_id |DataArray.metadata(*Section*)(#SectionNotes)|
    | NeuralEntity.source_unit_id   |DataArray.metadata(*Section*)(#SectionNotes)|
    * Attribute names in Nix can be accessed by camel case equivalents of those in Neuroshare.

## neuroshare.SegmentEntity
Maps directly to a nix group containing all segments all data arrays corresponding to all segments.
All dataArrays from all segment enitities are collectively stored in the segment group.
The metadata for all segments are stored as sub sections in the segment section.
- Attributes

    | Neuroshare                           | NIX                                                      |
    |--------------------------------------|----------------------------------------------------------|
    | SegmentEntity.max_sample_count       |SubSection.SubSection.properties(*Section*)(#SectionNotes)|
    | SegmentEntity.source_count           |SubSection.SubSection.properties(*Section*)(#SectionNotes)|
    * Attribute names in Nix can be accessed by camel case equivalents of those in Neuroshare.

#Section Notes
**Attribute names in Nix can be accessed by camel case equivalents of those in Neuroshare.**

(1)The metadata of an Event entities can be accessed by:
    meta = file.blocks['input_file'].groups['Event'].data_arrays[#index or name].metadata
    print meta['ItemCount'] #note the camel case equivalent of attribute name

(2)The metadata of an Analog entities can be accessed by:
    meta = file.blocks['input_file'].groups['Analog'].data_arrays[#index or name].metadata
    print meta['SampleRate'] #note the camel case equivalent of attribute name
    
(3)The metadata of an Neural entities can be accessed by:
    meta = file.blocks['input_file'].groups['Neural'].data_arrays[#index or name].metadata
    print meta['ProbeInfo'] #note the camel case equivalent of attribute name    

(4)The metadata of a Segment:
    
    The metadata for a segment can be accessed by:
        meta = file.sections['input_file'].sections['segments'].sections[#index or name+"_metadata"]
        print meta['MaxSampleCount'] #note the camel case equivalent of attribute name

    The metadata for the sources of a segment can be accessed by using index of the source:
        # HERE let the index of desired source be 0
        meta = file.sections['input_file'].sections['segments'].sections[#index or name+"_metadata"].sections['SourceInfo.0']
        print meta['HighFilterType'] #note the camel case equivalent of attribute name
                
    The metadata for the dataArray in a segment contanins only one property i.e. 'UnitId'
        meta = file.blocks['input_file'].groups['Segment'].data_arrays[#index or name].metadata
        print meta['unitID'] #note the camel case equivalent of attribute name
    
