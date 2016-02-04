import os
import sys
from . import _capi


class ArgumentError(Exception):
    def __init__(self, arg, msg):
        self.arg = arg
        self.msg = msg

    def __str__(self):
        return "\"%s\": %s" % (self.arg, self.msg)


class DLLException(Exception):
    def __init__(self, name, ext, lib=None):
        self.name = name
        self.ext = ext
        self.lib = lib


class DLLTypeUnknown(DLLException):
    def __str__(self):
        return '"%s": Unknown library type.' % self.ext


class DLLNotFound(DLLException):
    def __str__(self):
        return 'Vendor DLL "%s" could not be found' % self.lib


def _find_dll(library_name):
    
    known_paths = ["~/.neuroshare", "/usr/lib/neuroshare", "/usr/local/lib/neuroshare"]
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
    
    dt = os.path.join(os.getcwd(), dll_name)
    if os.path.lexists(dt):
        return dt

    for cur_path in known_paths+sys.path:
        dt = os.path.join(os.path.expanduser(cur_path), dll_name)
        if os.path.lexists(dt):
            return dt
        
    return None


def find_library_for_file(filename):

    dll_map = {"mcd": "nsMCDLibrary",
               "plx": "nsPlxLibrary",
               "map": "nsAOLibrary",
               "nev": "nsNEVLibrary",
               "nex": "NeuroExplorerNeuroShareLibrary"}

    (root, ext) = os.path.splitext(filename)
    if not ext or not ext.startswith('.'):
        raise ArgumentError(filename, "Could find file extension")

    ext = ext[1:]

    if ext not in dll_map:
        raise DLLTypeUnknown(root, ext)

    library_name = dll_map[ext]
    path = _find_dll(library_name)

    if not path:
        path = _find_dll("nsWineLibrary")

    if not path:
        raise DLLNotFound(root, ext, library_name)

    return library_name, path


def load_library_for_file(filename):
    return Library.for_file(filename)

# ## Library Implementation


class Library(object):

    _loaded_libs = {}

    @classmethod
    def for_file(cls, filename):
        (name, path) = find_library_for_file(filename)
        if name not in cls._loaded_libs:
            lib = Library(name, path)
            cls._loaded_libs[name] = lib

        return cls._loaded_libs[name]

    def __init__(self, name, path):
        self._name = name
        self._path = path
        self._handle = _capi.library_open(path)
        self._open_files = []
        self._info = _capi.get_library_info(self._handle)

    def _open_file(self, filename):
        (fh, file_info) = _capi.open_file(self._handle, filename)
        self._open_files.append(fh)
        return fh, file_info

    def _close_file(self, nsfile):
        fh = nsfile.handle
        _capi.close_file(self._handle, fh)
        self._open_files.remove(fh)

    def _get_entity_info(self, nsfile, entity_id):
        fh = nsfile.handle
        
        info = _capi.get_entity_info(self._handle, fh, entity_id)
        return info

    def _get_event_data(self, event, index):
        fh = event.file.handle
        entity_id = event.id
        
        event_type = event.event_type
        max_data_len = event.max_data_length
        
        data = _capi.get_event_data(self._handle, fh, entity_id, index, event_type, max_data_len)
        return data

    def _get_analog_data(self, analog, index, count):
        fh = analog.file.handle
        entity_id = analog.id
        
        data = _capi.get_analog_data(self._handle, fh, entity_id, index, count)
        return data 

    def _get_segment_data(self, segment, index):
        fh = segment.file.handle
        entity_id = segment.id

        source_count = segment.source_count
        max_sample_count = segment.max_sample_count
        
        data = _capi.get_segment_data(self._handle, fh, entity_id, index, source_count, max_sample_count)
        return data  

    def _get_neural_data(self, neural, index, count):
        fh = neural.file.handle
        entity_id = neural.id
        
        data = _capi.get_neural_data(self._handle, fh, entity_id, index, count)
        return data  

    def _get_time_by_index(self, entity, index):
        fh = entity.file.handle
        entity_id = entity.id

        t = _capi.get_time_by_index(self._handle, fh, entity_id, index)
        return t

    def _get_index_by_time(self, entity, time, position):
        fh = entity.file.handle
        entity_id = entity.id
        
        idx = _capi.get_index_by_time(self._handle, fh, entity_id, time, position)
        return idx

    def __del__(self):
        _capi.library_close(self._handle)

    @property
    def metadata_raw(self):
        return self._info

    @property
    def creator(self):
        return self._info['Creator']

    @property
    def description(self):
        return self._info['Description']

    @property
    def api_version(self):
        major = self._info['APIVersionMaj']
        minor = self._info['APIVersionMin']
        return major, minor

    @property
    def library_version(self):
        major = self._info['LibVersionMaj']
        minor = self._info['LibVersionMin']
        return major, minor

    @property
    def max_files(self):
        return self._info['MaxFiles']

    @property
    def mtime(self):
        from datetime import date
        year = self._info['Time_Year']
        month = self._info['Time_Month']
        day = self._info['Time_Day']
        return date(year, month, day)

    @property
    def name(self):
        return self._name

    @property
    def path(self):
        return self._path
