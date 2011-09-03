import os
import sys
import _capi

def _find_dll(library_name):
    
    known_paths = ["~/.neuroshare", "/usr/lib/neuroshare", "/usr/local/lib/neuroshare"];
    platform = sys.platform

    if platform.startswith('linux'):
        dll_suffix = "so"
    elif platform.startswith('darwin'):
        dll_suffix = "dylib"
    elif platform.startswith('win'):
        dll_suffix = "dll"
    else:
        dll_suffix = "error"
    
    dll_name = "%s.%s" % (library_name, dll_suffix)
    
    dt = os.path.join (os.getcwd (), dll_name)
    if os.path.lexists (dt):
        return dt

    for cur_path in known_paths:
        dt = os.path.join (os.path.expanduser (cur_path), dll_name)
        if os.path.lexists (dt):
            return dt
        
    return None

def load_library_for_file(filename):

    dll_map = {"mcd" : "nsMCDLibrary",
               "plx": "nsPlxLibrary",
               "map": "nsAOLibrary",
               "nev": "nsNEVLibrary",
               "nex": "NeuroExplorerNeuroShareLibrary"}
    
    (root, ext) = os.path.splitext(filename)
    if not ext or not ext.startswith('.'):
        print 'ERROR' #FIXME: raise exception

    ext = ext[1:]
    
    if not dll_map.has_key (ext):
        print 'ERRPR' #FIXME: raise ex

    library_name = dll_map[ext]
    path = _find_dll (library_name)

    if not path:
        path = _find_dll ("nsWineLibrary")

    if not path:
        print "ERROR !!"
    
    #FIXME: cach open libraries
    lib = Library (path)
    return lib

from File import File
    
class Library(object):
    def __init__(self, path):
        self._handle = _capi.library_open (path)
        self._open_files = []
        self._info = _capi._get_library_info (self._handle)

    def _open_file(self, filename):
        nsfile = _capi._open_file (self._handle, filename)
        self._open_files.append (nsfile)
        return nsfile

    def _close_file(self, file):
        fh = file._handle
        _capi._close_file (self._handle, fh)
        #self._open_files.remove (fh)

    def _get_entity_info(self, nsfile, entity_id):
        fh = nsfile._handle
        
        info = _capi._get_entity_info (self._handle, fh, entity_id)
        return info

    def _get_event_data(self, event, index):
        fh = event.file._handle
        entity_id = event.id
        
        event_type = event.event_type
        max_data_len = event.max_data_length
        
        data = _capi._get_event_data (self._handle, fh, entity_id, index, event_type, max_data_len)
        return data

    def _get_analog_data (self, analog, index, count):
        fh = analog.file._handle
        entity_id = analog.id
        
        data = _capi._get_analog_data (self._handle, fh, entity_id, index, count)
        return data 

    def _get_segment_data (self, segment, index):
        fh = segment.file._handle
        entity_id = segment.id

        source_count = segment.source_count
        max_sample_count = segment.max_sample_count
        
        data = _capi._get_segment_data (self._handle, fh, entity_id, index, source_count, max_sample_count)
        return data  

    def _get_neural_data (self, neural, index, count):
        fh = neural.file._handle
        entity_id = neural.id
        
        data = _capi._get_neural_data (self._handle, fh, entity_id, index, count)
        return data  

    def _get_time_by_index (self, entity, index):
        fh = entity.file._handle
        entity_id = entity.id

        t = _capi._get_time_by_index(self._handle, fh, entity_id, index)
        return t

    def _get_index_by_time (self, entity, time, position):
        fh = entity.file._handle
        entity_id = entity.id
        
        idx = _capi._get_index_by_time (self._handle, fh, entity_id, time, position)
        return idx

    def __del__(self):
        _capi.library_close(self._handle)

    @property
    def creator(self):
        return self._info['Creator']



