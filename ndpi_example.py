'''Wrapper for ndpi_util.h

Generated with:
../../ctypesgen/ctypesgen.py -lneon ndpi_util.h ndpiReader.c -o ndpi_example.py

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # FIXME / TODO return '.' and os.path.dirname(__file__)
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")
        dirs.append(os.path.dirname(__file__))

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")
        directories.append(os.path.dirname(__file__))

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        unix_lib_dirs_list = ['/lib', '/usr/lib', '/lib64', '/usr/lib64']
        if sys.platform.startswith('linux'):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            bitage = platform.architecture()[0]
            if bitage.startswith('32'):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ['/lib/i386-linux-gnu', '/usr/lib/i386-linux-gnu']
            elif bitage.startswith('64'):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ['/lib/x86_64-linux-gnu', '/usr/lib/x86_64-linux-gnu']
            else:
                # guess...
                unix_lib_dirs_list += glob.glob('/lib/*linux-gnu')
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries

_libs["neon"] = load_library("neon")

# 1 libraries
# End libraries

# No modules

u_int8_t = c_ubyte # /usr/include/x86_64-linux-gnu/sys/types.h: 173

u_int16_t = c_uint # /usr/include/x86_64-linux-gnu/sys/types.h: 174

u_int32_t = c_uint # /usr/include/x86_64-linux-gnu/sys/types.h: 175

u_int64_t = c_ulong # /usr/include/x86_64-linux-gnu/sys/types.h: 177

# /usr/include/pcap/pcap.h: 81
class struct_pcap(Structure):
    pass

pcap_t = struct_pcap # /usr/include/pcap/pcap.h: 81

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 95
for _lib in _libs.values():
    try:
        info = (c_char * 96).in_dll(_lib, 'info')
        break
    except:
        pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 96
for _lib in _libs.values():
    try:
        host_server_name = (c_char * 256).in_dll(_lib, 'host_server_name')
        break
    except:
        pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 97
for _lib in _libs.values():
    try:
        bittorent_hash = (c_char * 41).in_dll(_lib, 'bittorent_hash')
        break
    except:
        pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 98
for _lib in _libs.values():
    try:
        dhcp_fingerprint = (c_char * 48).in_dll(_lib, 'dhcp_fingerprint')
        break
    except:
        pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 108
for _lib in _libs.values():
    try:
        src_id = (POINTER(None)).in_dll(_lib, 'src_id')
        break
    except:
        pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 108
for _lib in _libs.values():
    try:
        dst_id = (POINTER(None)).in_dll(_lib, 'dst_id')
        break
    except:
        pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 126
class struct_ndpi_stats(Structure):
    pass

struct_ndpi_stats.__slots__ = [
    'guessed_flow_protocols',
    'raw_packet_count',
    'ip_packet_count',
    'total_wire_bytes',
    'total_ip_bytes',
    'total_discarded_bytes',
    'protocol_counter',
    'protocol_counter_bytes',
    'protocol_flows',
    'ndpi_flow_count',
    'tcp_count',
    'udp_count',
    'mpls_count',
    'pppoe_count',
    'vlan_count',
    'fragmented_count',
    'packet_len',
    'max_packet_len',
]
struct_ndpi_stats._fields_ = [
    ('guessed_flow_protocols', u_int32_t),
    ('raw_packet_count', u_int64_t),
    ('ip_packet_count', u_int64_t),
    ('total_wire_bytes', u_int64_t),
    ('total_ip_bytes', u_int64_t),
    ('total_discarded_bytes', u_int64_t),
    ('protocol_counter', u_int64_t * ((NDPI_MAX_SUPPORTED_PROTOCOLS + NDPI_MAX_NUM_CUSTOM_PROTOCOLS) + 1)),
    ('protocol_counter_bytes', u_int64_t * ((NDPI_MAX_SUPPORTED_PROTOCOLS + NDPI_MAX_NUM_CUSTOM_PROTOCOLS) + 1)),
    ('protocol_flows', u_int32_t * ((NDPI_MAX_SUPPORTED_PROTOCOLS + NDPI_MAX_NUM_CUSTOM_PROTOCOLS) + 1)),
    ('ndpi_flow_count', u_int32_t),
    ('tcp_count', u_int64_t),
    ('udp_count', u_int64_t),
    ('mpls_count', u_int64_t),
    ('pppoe_count', u_int64_t),
    ('vlan_count', u_int64_t),
    ('fragmented_count', u_int64_t),
    ('packet_len', u_int64_t * 6),
    ('max_packet_len', u_int16_t),
]

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 135
class struct_ndpi_workflow_prefs(Structure):
    pass

struct_ndpi_workflow_prefs.__slots__ = [
    'decode_tunnels',
    'quiet_mode',
    'num_roots',
    'max_ndpi_flows',
]
struct_ndpi_workflow_prefs._fields_ = [
    ('decode_tunnels', u_int8_t),
    ('quiet_mode', u_int8_t),
    ('num_roots', u_int32_t),
    ('max_ndpi_flows', u_int32_t),
]

ndpi_workflow_prefs_t = struct_ndpi_workflow_prefs # /home/massimo/Desktop/nDPI/example/ndpi_util.h: 135

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 144
class struct_ndpi_workflow(Structure):
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 140
class struct_ndpi_flow_info(Structure):
    pass

ndpi_workflow_callback_ptr = CFUNCTYPE(UNCHECKED(None), POINTER(struct_ndpi_workflow), POINTER(struct_ndpi_flow_info), POINTER(None)) # /home/massimo/Desktop/nDPI/example/ndpi_util.h: 140

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 160
class struct_ndpi_detection_module_struct(Structure):
    pass

struct_ndpi_workflow.__slots__ = [
    'last_time',
    'prefs',
    'stats',
    '__flow_detected_callback',
    '__flow_detected_udata',
    '__flow_giveup_callback',
    '__flow_giveup_udata',
    'pcap_handle',
    'ndpi_flows_root',
    'ndpi_struct',
    'num_allocated_flows',
]
struct_ndpi_workflow._fields_ = [
    ('last_time', u_int64_t),
    ('prefs', struct_ndpi_workflow_prefs),
    ('stats', struct_ndpi_stats),
    ('__flow_detected_callback', ndpi_workflow_callback_ptr),
    ('__flow_detected_udata', POINTER(None)),
    ('__flow_giveup_callback', ndpi_workflow_callback_ptr),
    ('__flow_giveup_udata', POINTER(None)),
    ('pcap_handle', POINTER(pcap_t)),
    ('ndpi_flows_root', POINTER(POINTER(None))),
    ('ndpi_struct', POINTER(struct_ndpi_detection_module_struct)),
    ('num_allocated_flows', u_int32_t),
]

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 177
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_free_flow_info_half'):
        continue
    ndpi_free_flow_info_half = _lib.ndpi_free_flow_info_half
    ndpi_free_flow_info_half.argtypes = [POINTER(struct_ndpi_flow_info)]
    ndpi_free_flow_info_half.restype = None
    break

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 181
class struct_ndpi_proto(Structure):
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 201
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_workflow_node_cmp'):
        continue
    ndpi_workflow_node_cmp = _lib.ndpi_workflow_node_cmp
    ndpi_workflow_node_cmp.argtypes = [POINTER(None), POINTER(None)]
    ndpi_workflow_node_cmp.restype = c_int
    break

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 203
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ethernet_crc32'):
        continue
    ethernet_crc32 = _lib.ethernet_crc32
    ethernet_crc32.argtypes = [POINTER(None), c_size_t]
    ethernet_crc32.restype = u_int32_t
    break

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 204
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_flow_info_freer'):
        continue
    ndpi_flow_info_freer = _lib.ndpi_flow_info_freer
    ndpi_flow_info_freer.argtypes = [POINTER(None)]
    ndpi_flow_info_freer.restype = None
    break

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 205
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'print_cipher_id'):
        continue
    print_cipher_id = _lib.print_cipher_id
    print_cipher_id.argtypes = [u_int32_t]
    if sizeof(c_int) == sizeof(c_void_p):
        print_cipher_id.restype = ReturnString
    else:
        print_cipher_id.restype = String
        print_cipher_id.errcheck = ReturnString
    break

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 207
for _lib in _libs.values():
    try:
        nDPI_LogLevel = (c_int).in_dll(_lib, 'nDPI_LogLevel')
        break
    except:
        pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 52
try:
    MAX_NUM_READER_THREADS = 16
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 53
try:
    IDLE_SCAN_PERIOD = 10
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 54
try:
    MAX_IDLE_TIME = 30000
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 55
try:
    IDLE_SCAN_BUDGET = 1024
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 56
try:
    NUM_ROOTS = 512
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 57
try:
    MAX_EXTRA_PACKETS_TO_CHECK = 7
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 58
try:
    MAX_NDPI_FLOWS = 200000000
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 59
try:
    TICK_RESOLUTION = 1000
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 60
try:
    MAX_NUM_IP_ADDRESS = 5
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 61
try:
    UPDATED_TREE = 1
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 62
try:
    AGGRESSIVE_PERCENT = 95.0
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 63
try:
    DIR_SRC = 10
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 64
try:
    DIR_DST = 20
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 65
try:
    PORT_ARRAY_SIZE = 20
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 66
try:
    HOST_ARRAY_SIZE = 20
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 67
try:
    FLOWS_PACKETS_THRESHOLD = 0.9
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 68
try:
    FLOWS_PERCENT_THRESHOLD = 1.0
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 69
try:
    FLOWS_PERCENT_THRESHOLD_2 = 0.2
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 70
try:
    FLOWS_THRESHOLD = 1000
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 71
try:
    PKTS_PERCENT_THRESHOLD = 0.1
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 72
try:
    MAX_TABLE_SIZE_1 = 4096
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 73
try:
    MAX_TABLE_SIZE_2 = 8192
except:
    pass

# /home/massimo/Desktop/nDPI/example/ndpi_util.h: 74
try:
    INIT_VAL = (-1)
except:
    pass

ndpi_workflow_prefs = struct_ndpi_workflow_prefs # /home/massimo/Desktop/nDPI/example/ndpi_util.h: 135

ndpi_flow_info = struct_ndpi_flow_info # /home/massimo/Desktop/nDPI/example/ndpi_util.h: 140

ndpi_detection_module_struct = struct_ndpi_detection_module_struct # /home/massimo/Desktop/nDPI/example/ndpi_util.h: 160

ndpi_proto = struct_ndpi_proto # /home/massimo/Desktop/nDPI/example/ndpi_util.h: 181

# No inserted files

