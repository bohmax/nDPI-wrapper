'''Wrapper for ndpi_api.h

Generated with:
../../../ctypesgen/ctypesgen.py -lneon ndpi_api.h ndpi_config.h ndpi_define.h ndpi_includes.h ndpi_main.h ndpi_protocol_ids.h ndpi_protocols.h ndpi_typedefs.h ndpi_unix.h ndpi_win32.h -o ndpi.py

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

NULL = None # <built-in>

__u_char = c_ubyte # /usr/include/x86_64-linux-gnu/bits/types.h: 30

__u_int = c_uint # /usr/include/x86_64-linux-gnu/bits/types.h: 32

__time_t = c_long # /usr/include/x86_64-linux-gnu/bits/types.h: 139

u_char = __u_char # /usr/include/x86_64-linux-gnu/sys/types.h: 33

u_int = __u_int # /usr/include/x86_64-linux-gnu/sys/types.h: 35

time_t = __time_t # /usr/include/time.h: 75

u_int8_t = c_ubyte # /usr/include/x86_64-linux-gnu/sys/types.h: 173

u_int16_t = c_uint # /usr/include/x86_64-linux-gnu/sys/types.h: 174

u_int32_t = c_uint # /usr/include/x86_64-linux-gnu/sys/types.h: 175

u_int64_t = c_ulong # /usr/include/x86_64-linux-gnu/sys/types.h: 177

# /usr/include/string.h: 62
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'memset'):
        continue
    memset = _lib.memset
    memset.argtypes = [POINTER(None), c_int, c_size_t]
    memset.restype = POINTER(None)
    break

# /usr/include/string.h: 65
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'memcmp'):
        continue
    memcmp = _lib.memcmp
    memcmp.argtypes = [POINTER(None), POINTER(None), c_size_t]
    memcmp.restype = c_int
    break

in_addr_t = c_uint32 # /usr/include/netinet/in.h: 30

# /usr/include/netinet/in.h: 31
class struct_in_addr(Structure):
    pass

struct_in_addr.__slots__ = [
    's_addr',
]
struct_in_addr._fields_ = [
    ('s_addr', in_addr_t),
]

enum_anon_75 = c_int # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_UNKNOWN = 0 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_FTP_CONTROL = 1 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_MAIL_POP = 2 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_MAIL_SMTP = 3 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_MAIL_IMAP = 4 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_DNS = 5 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_IPP = 6 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_HTTP = 7 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_MDNS = 8 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_NTP = 9 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_NETBIOS = 10 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_NFS = 11 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SSDP = 12 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_BGP = 13 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SNMP = 14 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_XDMCP = 15 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SMBV1 = 16 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SYSLOG = 17 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_DHCP = 18 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_POSTGRES = 19 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_MYSQL = 20 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_HOTMAIL = 21 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_DIRECT_DOWNLOAD_LINK = 22 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_MAIL_POPS = 23 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_APPLEJUICE = 24 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_DIRECTCONNECT = 25 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_NTOP = 26 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_COAP = 27 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_VMWARE = 28 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_MAIL_SMTPS = 29 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_FBZERO = 30 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_UBNTAC2 = 31 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_KONTIKI = 32 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_OPENFT = 33 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_FASTTRACK = 34 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_GNUTELLA = 35 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_EDONKEY = 36 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_BITTORRENT = 37 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SKYPE_CALL = 38 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SIGNAL = 39 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_MEMCACHED = 40 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SMBV23 = 41 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_MINING = 42 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_NEST_LOG_SINK = 43 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_MODBUS = 44 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_WHATSAPP_VIDEO = 45 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_DATASAVER = 46 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_XBOX = 47 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_QQ = 48 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_TIKTOK = 49 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_RTSP = 50 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_MAIL_IMAPS = 51 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_ICECAST = 52 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_PPLIVE = 53 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_PPSTREAM = 54 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_ZATTOO = 55 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SHOUTCAST = 56 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SOPCAST = 57 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_TVANTS = 58 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_TVUPLAYER = 59 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_HTTP_DOWNLOAD = 60 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_QQLIVE = 61 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_THUNDER = 62 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SOULSEEK = 63 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SSL_NO_CERT = 64 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_IRC = 65 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_AYIYA = 66 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_UNENCRYPTED_JABBER = 67 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_MSN = 68 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_OSCAR = 69 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_YAHOO = 70 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_BATTLEFIELD = 71 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_GOOGLE_PLUS = 72 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_IP_VRRP = 73 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_STEAM = 74 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_HALFLIFE2 = 75 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_WORLDOFWARCRAFT = 76 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_TELNET = 77 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_STUN = 78 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_IP_IPSEC = 79 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_IP_GRE = 80 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_IP_ICMP = 81 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_IP_IGMP = 82 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_IP_EGP = 83 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_IP_SCTP = 84 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_IP_OSPF = 85 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_IP_IP_IN_IP = 86 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_RTP = 87 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_RDP = 88 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_VNC = 89 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_PCANYWHERE = 90 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SSL = 91 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SSH = 92 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_USENET = 93 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_MGCP = 94 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_IAX = 95 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_TFTP = 96 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_AFP = 97 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_STEALTHNET = 98 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_AIMINI = 99 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SIP = 100 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_TRUPHONE = 101 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_IP_ICMPV6 = 102 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_DHCPV6 = 103 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_ARMAGETRON = 104 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_CROSSFIRE = 105 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_DOFUS = 106 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_FIESTA = 107 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_FLORENSIA = 108 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_GUILDWARS = 109 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_HTTP_ACTIVESYNC = 110 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_KERBEROS = 111 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_LDAP = 112 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_MAPLESTORY = 113 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_MSSQL_TDS = 114 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_PPTP = 115 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_WARCRAFT3 = 116 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_WORLD_OF_KUNG_FU = 117 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SLACK = 118 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_FACEBOOK = 119 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_TWITTER = 120 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_DROPBOX = 121 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_GMAIL = 122 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_GOOGLE_MAPS = 123 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_YOUTUBE = 124 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SKYPE = 125 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_GOOGLE = 126 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_DCERPC = 127 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_NETFLOW = 128 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SFLOW = 129 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_HTTP_CONNECT = 130 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_HTTP_PROXY = 131 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_CITRIX = 132 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_NETFLIX = 133 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_LASTFM = 134 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_WAZE = 135 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_YOUTUBE_UPLOAD = 136 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_GENERIC = 137 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_CHECKMK = 138 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_AJP = 139 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_APPLE = 140 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_WEBEX = 141 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_WHATSAPP = 142 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_APPLE_ICLOUD = 143 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_VIBER = 144 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_APPLE_ITUNES = 145 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_RADIUS = 146 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_WINDOWS_UPDATE = 147 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_TEAMVIEWER = 148 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_TUENTI = 149 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_LOTUS_NOTES = 150 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SAP = 151 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_GTP = 152 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_UPNP = 153 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_LLMNR = 154 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_REMOTE_SCAN = 155 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SPOTIFY = 156 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_MESSENGER = 157 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_H323 = 158 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_OPENVPN = 159 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_NOE = 160 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_CISCOVPN = 161 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_TEAMSPEAK = 162 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_TOR = 163 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SKINNY = 164 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_RTCP = 165 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_RSYNC = 166 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_ORACLE = 167 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_CORBA = 168 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_UBUNTUONE = 169 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_WHOIS_DAS = 170 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_COLLECTD = 171 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SOCKS = 172 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_NINTENDO = 173 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_RTMP = 174 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_FTP_DATA = 175 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_WIKIPEDIA = 176 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_ZMQ = 177 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_AMAZON = 178 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_EBAY = 179 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_CNN = 180 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_MEGACO = 181 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_REDIS = 182 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_PANDO = 183 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_VHUA = 184 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_TELEGRAM = 185 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_VEVO = 186 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_PANDORA = 187 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_QUIC = 188 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_WHATSAPP_VOICE = 189 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_EAQ = 190 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_OOKLA = 191 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_AMQP = 192 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_KAKAOTALK = 193 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_KAKAOTALK_VOICE = 194 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_TWITCH = 195 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_DNS_OVER_HTTPS = 196 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_WECHAT = 197 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_MPEGTS = 198 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SNAPCHAT = 199 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SINA = 200 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_HANGOUT = 201 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_IFLIX = 202 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_GITHUB = 203 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_BJNP = 204 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_FREE_205 = 205 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_FREE_206 = 206 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SMPP = 207 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_DNSCRYPT = 208 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_TINC = 209 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_DEEZER = 210 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_INSTAGRAM = 211 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_MICROSOFT = 212 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_STARCRAFT = 213 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_TEREDO = 214 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_HOTSPOT_SHIELD = 215 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_HEP = 216 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_GOOGLE_DRIVE = 217 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_OCS = 218 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_OFFICE_365 = 219 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_CLOUDFLARE = 220 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_MS_ONE_DRIVE = 221 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_MQTT = 222 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_RX = 223 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_APPLESTORE = 224 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_OPENDNS = 225 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_GIT = 226 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_DRDA = 227 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_PLAYSTORE = 228 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SOMEIP = 229 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_FIX = 230 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_PLAYSTATION = 231 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_PASTEBIN = 232 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_LINKEDIN = 233 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_SOUNDCLOUD = 234 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_CSGO = 235 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_LISP = 236 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_DIAMETER = 237 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_APPLE_PUSH = 238 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_GOOGLE_SERVICES = 239 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_AMAZON_VIDEO = 240 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_GOOGLE_DOCS = 241 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_PROTOCOL_WHATSAPP_FILES = 242 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

NDPI_LAST_IMPLEMENTED_PROTOCOL = (NDPI_PROTOCOL_WHATSAPP_FILES + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

ndpi_protocol_id_t = enum_anon_75 # /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 290

enum_anon_76 = c_int # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 36

NDPI_LOG_ERROR = 0 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 36

NDPI_LOG_TRACE = (NDPI_LOG_ERROR + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 36

NDPI_LOG_DEBUG = (NDPI_LOG_TRACE + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 36

NDPI_LOG_DEBUG_EXTRA = (NDPI_LOG_DEBUG + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 36

ndpi_log_level_t = enum_anon_76 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 36

enum_anon_77 = c_int # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 44

ndpi_preorder = 0 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 44

ndpi_postorder = (ndpi_preorder + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 44

ndpi_endorder = (ndpi_postorder + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 44

ndpi_leaf = (ndpi_endorder + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 44

ndpi_VISIT = enum_anon_77 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 44

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 47
class struct_node_t(Structure):
    pass

struct_node_t.__slots__ = [
    'key',
    'left',
    'right',
]
struct_node_t._fields_ = [
    ('key', String),
    ('left', POINTER(struct_node_t)),
    ('right', POINTER(struct_node_t)),
]

ndpi_node = struct_node_t # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 50

ndpi_ndpi_mask = u_int32_t # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 53

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 58
class struct_ndpi_protocol_bitmask_struct(Structure):
    pass

struct_ndpi_protocol_bitmask_struct.__slots__ = [
    'fds_bits',
]
struct_ndpi_protocol_bitmask_struct._fields_ = [
    ('fds_bits', ndpi_ndpi_mask * ((512 + ((sizeof(ndpi_ndpi_mask) * 8) - 1)) / (sizeof(ndpi_ndpi_mask) * 8))),
]

ndpi_protocol_bitmask_struct_t = struct_ndpi_protocol_bitmask_struct # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 58

ndpi_debug_function_ptr = CFUNCTYPE(UNCHECKED(None), u_int32_t, POINTER(None), ndpi_log_level_t, String, String, c_uint, String) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 61

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 89
class struct_ndpi_chdlc(Structure):
    pass

struct_ndpi_chdlc.__slots__ = [
    'addr',
    'ctrl',
    'proto_code',
]
struct_ndpi_chdlc._fields_ = [
    ('addr', u_int8_t),
    ('ctrl', u_int8_t),
    ('proto_code', u_int16_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 89
for _lib in _libs.values():
    try:
        PACK_OFF = (struct_ndpi_chdlc).in_dll(_lib, 'PACK_OFF')
        break
    except:
        pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 102
class struct_ndpi_slarp(Structure):
    pass

struct_ndpi_slarp.__slots__ = [
    'slarp_type',
    'addr_1',
    'addr_2',
]
struct_ndpi_slarp._fields_ = [
    ('slarp_type', u_int32_t),
    ('addr_1', u_int32_t),
    ('addr_2', u_int32_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 102
for _lib in _libs.values():
    try:
        PACK_OFF = (struct_ndpi_slarp).in_dll(_lib, 'PACK_OFF')
        break
    except:
        pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 113
class struct_ndpi_cdp(Structure):
    pass

struct_ndpi_cdp.__slots__ = [
    'version',
    'ttl',
    'checksum',
    'type',
    'length',
]
struct_ndpi_cdp._fields_ = [
    ('version', u_int8_t),
    ('ttl', u_int8_t),
    ('checksum', u_int16_t),
    ('type', u_int16_t),
    ('length', u_int16_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 113
for _lib in _libs.values():
    try:
        PACK_OFF = (struct_ndpi_cdp).in_dll(_lib, 'PACK_OFF')
        break
    except:
        pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 123
class struct_ndpi_ethhdr(Structure):
    pass

struct_ndpi_ethhdr.__slots__ = [
    'h_dest',
    'h_source',
    'h_proto',
]
struct_ndpi_ethhdr._fields_ = [
    ('h_dest', u_char * 6),
    ('h_source', u_char * 6),
    ('h_proto', u_int16_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 123
for _lib in _libs.values():
    try:
        PACK_OFF = (struct_ndpi_ethhdr).in_dll(_lib, 'PACK_OFF')
        break
    except:
        pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 133
class struct_ndpi_snap_extension(Structure):
    pass

struct_ndpi_snap_extension.__slots__ = [
    'oui',
    'oui2',
    'proto_ID',
]
struct_ndpi_snap_extension._fields_ = [
    ('oui', u_int16_t),
    ('oui2', u_int8_t),
    ('proto_ID', u_int16_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 133
for _lib in _libs.values():
    try:
        PACK_OFF = (struct_ndpi_snap_extension).in_dll(_lib, 'PACK_OFF')
        break
    except:
        pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 142
class struct_ndpi_llc_header_snap(Structure):
    pass

struct_ndpi_llc_header_snap.__slots__ = [
    'dsap',
    'ssap',
    'ctrl',
    'snap',
]
struct_ndpi_llc_header_snap._fields_ = [
    ('dsap', u_int8_t),
    ('ssap', u_int8_t),
    ('ctrl', u_int8_t),
    ('snap', struct_ndpi_snap_extension),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 142
for _lib in _libs.values():
    try:
        PACK_OFF = (struct_ndpi_llc_header_snap).in_dll(_lib, 'PACK_OFF')
        break
    except:
        pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 154
class struct_ndpi_radiotap_header(Structure):
    pass

struct_ndpi_radiotap_header.__slots__ = [
    'version',
    'pad',
    'len',
    'present',
    'MAC_timestamp',
    'flags',
]
struct_ndpi_radiotap_header._fields_ = [
    ('version', u_int8_t),
    ('pad', u_int8_t),
    ('len', u_int16_t),
    ('present', u_int32_t),
    ('MAC_timestamp', u_int64_t),
    ('flags', u_int8_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 154
for _lib in _libs.values():
    try:
        PACK_OFF = (struct_ndpi_radiotap_header).in_dll(_lib, 'PACK_OFF')
        break
    except:
        pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 167
class struct_ndpi_wifi_header(Structure):
    pass

struct_ndpi_wifi_header.__slots__ = [
    'fc',
    'duration',
    'rcvr',
    'trsm',
    'dest',
    'seq_ctrl',
]
struct_ndpi_wifi_header._fields_ = [
    ('fc', u_int16_t),
    ('duration', u_int16_t),
    ('rcvr', u_char * 6),
    ('trsm', u_char * 6),
    ('dest', u_char * 6),
    ('seq_ctrl', u_int16_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 167
for _lib in _libs.values():
    try:
        PACK_OFF = (struct_ndpi_wifi_header).in_dll(_lib, 'PACK_OFF')
        break
    except:
        pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 183
class struct_ndpi_mpls_header(Structure):
    pass

struct_ndpi_mpls_header.__slots__ = [
    'ttl',
    's',
    'exp',
    'label',
]
struct_ndpi_mpls_header._fields_ = [
    ('ttl', u_int32_t, 8),
    ('s', u_int32_t, 1),
    ('exp', u_int32_t, 3),
    ('label', u_int32_t, 20),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 183
for _lib in _libs.values():
    try:
        PACK_OFF = (struct_ndpi_mpls_header).in_dll(_lib, 'PACK_OFF')
        break
    except:
        pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 205
class struct_ndpi_iphdr(Structure):
    pass

struct_ndpi_iphdr.__slots__ = [
    'ihl',
    'version',
    'tos',
    'tot_len',
    'id',
    'frag_off',
    'ttl',
    'protocol',
    'check',
    'saddr',
    'daddr',
]
struct_ndpi_iphdr._fields_ = [
    ('ihl', u_int8_t, 4),
    ('version', u_int8_t, 4),
    ('tos', u_int8_t),
    ('tot_len', u_int16_t),
    ('id', u_int16_t),
    ('frag_off', u_int16_t),
    ('ttl', u_int8_t),
    ('protocol', u_int8_t),
    ('check', u_int16_t),
    ('saddr', u_int32_t),
    ('daddr', u_int32_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 205
for _lib in _libs.values():
    try:
        PACK_OFF = (struct_ndpi_iphdr).in_dll(_lib, 'PACK_OFF')
        break
    except:
        pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 211
class union_anon_78(Union):
    pass

union_anon_78.__slots__ = [
    'u6_addr8',
    'u6_addr16',
    'u6_addr32',
]
union_anon_78._fields_ = [
    ('u6_addr8', u_int8_t * 16),
    ('u6_addr16', u_int16_t * 8),
    ('u6_addr32', u_int32_t * 4),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 210
class struct_ndpi_in6_addr(Structure):
    pass

struct_ndpi_in6_addr.__slots__ = [
    'u6_addr',
]
struct_ndpi_in6_addr._fields_ = [
    ('u6_addr', union_anon_78),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 218
class struct_ndpi_ip6_hdrctl(Structure):
    pass

struct_ndpi_ip6_hdrctl.__slots__ = [
    'ip6_un1_flow',
    'ip6_un1_plen',
    'ip6_un1_nxt',
    'ip6_un1_hlim',
]
struct_ndpi_ip6_hdrctl._fields_ = [
    ('ip6_un1_flow', u_int32_t),
    ('ip6_un1_plen', u_int16_t),
    ('ip6_un1_nxt', u_int8_t),
    ('ip6_un1_hlim', u_int8_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 226
class struct_ndpi_ipv6hdr(Structure):
    pass

struct_ndpi_ipv6hdr.__slots__ = [
    'ip6_hdr',
    'ip6_src',
    'ip6_dst',
]
struct_ndpi_ipv6hdr._fields_ = [
    ('ip6_hdr', struct_ndpi_ip6_hdrctl),
    ('ip6_src', struct_ndpi_in6_addr),
    ('ip6_dst', struct_ndpi_in6_addr),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 251
class struct_ndpi_tcphdr(Structure):
    pass

struct_ndpi_tcphdr.__slots__ = [
    'source',
    'dest',
    'seq',
    'ack_seq',
    'res1',
    'doff',
    'fin',
    'syn',
    'rst',
    'psh',
    'ack',
    'urg',
    'ece',
    'cwr',
    'window',
    'check',
    'urg_ptr',
]
struct_ndpi_tcphdr._fields_ = [
    ('source', u_int16_t),
    ('dest', u_int16_t),
    ('seq', u_int32_t),
    ('ack_seq', u_int32_t),
    ('res1', u_int16_t, 4),
    ('doff', u_int16_t, 4),
    ('fin', u_int16_t, 1),
    ('syn', u_int16_t, 1),
    ('rst', u_int16_t, 1),
    ('psh', u_int16_t, 1),
    ('ack', u_int16_t, 1),
    ('urg', u_int16_t, 1),
    ('ece', u_int16_t, 1),
    ('cwr', u_int16_t, 1),
    ('window', u_int16_t),
    ('check', u_int16_t),
    ('urg_ptr', u_int16_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 251
for _lib in _libs.values():
    try:
        PACK_OFF = (struct_ndpi_tcphdr).in_dll(_lib, 'PACK_OFF')
        break
    except:
        pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 262
class struct_ndpi_udphdr(Structure):
    pass

struct_ndpi_udphdr.__slots__ = [
    'source',
    'dest',
    'len',
    'check',
]
struct_ndpi_udphdr._fields_ = [
    ('source', u_int16_t),
    ('dest', u_int16_t),
    ('len', u_int16_t),
    ('check', u_int16_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 262
for _lib in _libs.values():
    try:
        PACK_OFF = (struct_ndpi_udphdr).in_dll(_lib, 'PACK_OFF')
        break
    except:
        pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 272
class struct_ndpi_dns_packet_header(Structure):
    pass

struct_ndpi_dns_packet_header.__slots__ = [
    'tr_id',
    'flags',
    'num_queries',
    'num_answers',
    'authority_rrs',
    'additional_rrs',
]
struct_ndpi_dns_packet_header._fields_ = [
    ('tr_id', u_int16_t),
    ('flags', u_int16_t),
    ('num_queries', u_int16_t),
    ('num_answers', u_int16_t),
    ('authority_rrs', u_int16_t),
    ('additional_rrs', u_int16_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 272
for _lib in _libs.values():
    try:
        PACK_OFF = (struct_ndpi_dns_packet_header).in_dll(_lib, 'PACK_OFF')
        break
    except:
        pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 281
class union_anon_79(Union):
    pass

union_anon_79.__slots__ = [
    'ipv4',
    'ipv4_u_int8_t',
    'ipv6',
]
union_anon_79._fields_ = [
    ('ipv4', u_int32_t),
    ('ipv4_u_int8_t', u_int8_t * 4),
    ('ipv6', struct_ndpi_in6_addr),
]

ndpi_ip_addr_t = union_anon_79 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 281

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 292
class struct_anon_80(Structure):
    pass

struct_anon_80.__slots__ = [
    'id',
    'sequence',
]
struct_anon_80._fields_ = [
    ('id', u_int16_t),
    ('sequence', u_int16_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 298
class struct_anon_81(Structure):
    pass

struct_anon_81.__slots__ = [
    '_unused',
    'mtu',
]
struct_anon_81._fields_ = [
    ('_unused', u_int16_t),
    ('mtu', u_int16_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 291
class union_anon_82(Union):
    pass

union_anon_82.__slots__ = [
    'echo',
    'gateway',
    'frag',
]
union_anon_82._fields_ = [
    ('echo', struct_anon_80),
    ('gateway', u_int32_t),
    ('frag', struct_anon_81),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 303
class struct_ndpi_icmphdr(Structure):
    pass

struct_ndpi_icmphdr.__slots__ = [
    'type',
    'code',
    'checksum',
    'un',
]
struct_ndpi_icmphdr._fields_ = [
    ('type', u_int8_t),
    ('code', u_int8_t),
    ('checksum', u_int16_t),
    ('un', union_anon_82),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 303
for _lib in _libs.values():
    try:
        PACK_OFF = (struct_ndpi_icmphdr).in_dll(_lib, 'PACK_OFF')
        break
    except:
        pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 312
class struct_spinlock(Structure):
    pass

struct_spinlock.__slots__ = [
    'val',
]
struct_spinlock._fields_ = [
    ('val', c_int),
]

spinlock_t = struct_spinlock # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 312

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 316
class struct_atomic(Structure):
    pass

struct_atomic.__slots__ = [
    'counter',
]
struct_atomic._fields_ = [
    ('counter', c_int),
]

atomic_t = struct_atomic # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 316

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 318
class struct_hash_ip4p_node(Structure):
    pass

struct_hash_ip4p_node.__slots__ = [
    'next',
    'prev',
    'lchg',
    'port',
    'count',
    'flag',
    'ip',
]
struct_hash_ip4p_node._fields_ = [
    ('next', POINTER(struct_hash_ip4p_node)),
    ('prev', POINTER(struct_hash_ip4p_node)),
    ('lchg', time_t),
    ('port', u_int16_t),
    ('count', u_int16_t, 12),
    ('flag', u_int16_t, 4),
    ('ip', u_int32_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 326
class struct_hash_ip4p(Structure):
    pass

struct_hash_ip4p.__slots__ = [
    'top',
    'lock',
    'len',
]
struct_hash_ip4p._fields_ = [
    ('top', POINTER(struct_hash_ip4p_node)),
    ('lock', spinlock_t),
    ('len', c_size_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 332
class struct_hash_ip4p_table(Structure):
    pass

struct_hash_ip4p_table.__slots__ = [
    'size',
    'ipv6',
    'lock',
    'count',
    'tbl',
]
struct_hash_ip4p_table._fields_ = [
    ('size', c_size_t),
    ('ipv6', c_int),
    ('lock', spinlock_t),
    ('count', atomic_t),
    ('tbl', struct_hash_ip4p),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 340
class struct_bt_announce(Structure):
    pass

struct_bt_announce.__slots__ = [
    'hash',
    'ip',
    'time',
    'port',
    'name_len',
    'name',
]
struct_bt_announce._fields_ = [
    ('hash', u_int32_t * 5),
    ('ip', u_int32_t * 4),
    ('time', u_int32_t),
    ('port', u_int16_t),
    ('name_len', u_int8_t),
    ('name', u_int8_t * (((192 - (4 * 10)) - 2) - 1)),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 356
class struct_tinc_cache_entry(Structure):
    pass

struct_tinc_cache_entry.__slots__ = [
    'src_address',
    'dst_address',
    'dst_port',
]
struct_tinc_cache_entry._fields_ = [
    ('src_address', u_int32_t),
    ('dst_address', u_int32_t),
    ('dst_port', u_int16_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 356
for _lib in _libs.values():
    try:
        PACK_OFF = (struct_tinc_cache_entry).in_dll(_lib, 'PACK_OFF')
        break
    except:
        pass

enum_anon_83 = c_int # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 369

NDPI_HTTP_METHOD_UNKNOWN = 0 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 369

NDPI_HTTP_METHOD_OPTIONS = (NDPI_HTTP_METHOD_UNKNOWN + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 369

NDPI_HTTP_METHOD_GET = (NDPI_HTTP_METHOD_OPTIONS + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 369

NDPI_HTTP_METHOD_HEAD = (NDPI_HTTP_METHOD_GET + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 369

NDPI_HTTP_METHOD_PATCH = (NDPI_HTTP_METHOD_HEAD + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 369

NDPI_HTTP_METHOD_POST = (NDPI_HTTP_METHOD_PATCH + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 369

NDPI_HTTP_METHOD_PUT = (NDPI_HTTP_METHOD_POST + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 369

NDPI_HTTP_METHOD_DELETE = (NDPI_HTTP_METHOD_PUT + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 369

NDPI_HTTP_METHOD_TRACE = (NDPI_HTTP_METHOD_DELETE + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 369

NDPI_HTTP_METHOD_CONNECT = (NDPI_HTTP_METHOD_TRACE + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 369

ndpi_http_method = enum_anon_83 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 369

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 371
class struct_ndpi_lru_cache(Structure):
    pass

struct_ndpi_lru_cache.__slots__ = [
    'num_entries',
    'entries',
]
struct_ndpi_lru_cache._fields_ = [
    ('num_entries', u_int32_t),
    ('entries', POINTER(u_int32_t)),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 375
class struct_ndpi_id_struct(Structure):
    pass

struct_ndpi_id_struct.__slots__ = [
    'detected_protocol_bitmask',
    'rtsp_ip_address',
    'yahoo_video_lan_timer',
    'irc_port',
    'last_time_port_used',
    'irc_ts',
    'gnutella_ts',
    'battlefield_ts',
    'thunder_ts',
    'rtsp_timer',
    'oscar_last_safe_access_time',
    'zattoo_ts',
    'jabber_stun_or_ft_ts',
    'directconnect_last_safe_access_time',
    'soulseek_last_safe_access_time',
    'detected_directconnect_port',
    'detected_directconnect_udp_port',
    'detected_directconnect_ssl_port',
    'bt_port_t',
    'bt_port_u',
    'jabber_voice_stun_port',
    'jabber_file_transfer_port',
    'detected_gnutella_port',
    'detected_gnutella_udp_port1',
    'detected_gnutella_udp_port2',
    'soulseek_listen_port',
    'irc_number_of_port',
    'oscar_ssl_session_id',
    'jabber_voice_stun_used_ports',
    'yahoo_video_lan_dir',
    'yahoo_conf_logged_in',
    'yahoo_voice_conf_logged_in',
    'rtsp_ts_set',
]
struct_ndpi_id_struct._fields_ = [
    ('detected_protocol_bitmask', ndpi_protocol_bitmask_struct_t),
    ('rtsp_ip_address', ndpi_ip_addr_t),
    ('yahoo_video_lan_timer', u_int32_t),
    ('irc_port', u_int16_t * 8),
    ('last_time_port_used', u_int32_t * 8),
    ('irc_ts', u_int32_t),
    ('gnutella_ts', u_int32_t),
    ('battlefield_ts', u_int32_t),
    ('thunder_ts', u_int32_t),
    ('rtsp_timer', u_int32_t),
    ('oscar_last_safe_access_time', u_int32_t),
    ('zattoo_ts', u_int32_t),
    ('jabber_stun_or_ft_ts', u_int32_t),
    ('directconnect_last_safe_access_time', u_int32_t),
    ('soulseek_last_safe_access_time', u_int32_t),
    ('detected_directconnect_port', u_int16_t),
    ('detected_directconnect_udp_port', u_int16_t),
    ('detected_directconnect_ssl_port', u_int16_t),
    ('bt_port_t', u_int16_t * 8),
    ('bt_port_u', u_int16_t * 8),
    ('jabber_voice_stun_port', u_int16_t * 6),
    ('jabber_file_transfer_port', u_int16_t * 2),
    ('detected_gnutella_port', u_int16_t),
    ('detected_gnutella_udp_port1', u_int16_t),
    ('detected_gnutella_udp_port2', u_int16_t),
    ('soulseek_listen_port', u_int16_t),
    ('irc_number_of_port', u_int8_t),
    ('oscar_ssl_session_id', u_int8_t * 33),
    ('jabber_voice_stun_used_ports', u_int8_t),
    ('yahoo_video_lan_dir', u_int32_t, 1),
    ('yahoo_conf_logged_in', u_int32_t, 1),
    ('yahoo_voice_conf_logged_in', u_int32_t, 1),
    ('rtsp_ts_set', u_int32_t, 1),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 471
class struct_ndpi_flow_tcp_struct(Structure):
    pass

struct_ndpi_flow_tcp_struct.__slots__ = [
    'smtp_command_bitmask',
    'pop_command_bitmask',
    'qq_nxt_len',
    'wa_matched_so_far',
    'tds_login_version',
    'irc_stage',
    'irc_port',
    'h323_valid_packets',
    'gnutella_msg_id',
    'irc_3a_counter',
    'irc_stage2',
    'irc_direction',
    'irc_0x1000_full',
    'soulseek_stage',
    'tds_stage',
    'usenet_stage',
    'imesh_stage',
    'http_setup_dir',
    'http_stage',
    'http_empty_line_seen',
    'http_wait_for_retransmission',
    'gnutella_stage',
    'mms_stage',
    'yahoo_sip_comm',
    'yahoo_http_proxy_stage',
    'msn_stage',
    'msn_ssl_ft',
    'ssh_stage',
    'vnc_stage',
    'telnet_stage',
    'ssl_seen_client_cert',
    'ssl_seen_server_cert',
    'ssl_seen_certificate',
    'ssl_stage',
    'postgres_stage',
    'ddlink_server_direction',
    'seen_syn',
    'seen_syn_ack',
    'seen_ack',
    'icecast_stage',
    'dofus_stage',
    'fiesta_stage',
    'wow_stage',
    'veoh_tv_stage',
    'shoutcast_stage',
    'rtp_special_packets_seen',
    'mail_pop_stage',
    'mail_imap_stage',
    'mail_imap_starttls',
    'skype_packet_id',
    'citrix_packet_id',
    'lotus_notes_packet_id',
    'teamviewer_stage',
    'prev_zmq_pkt_len',
    'prev_zmq_pkt',
    'ppstream_stage',
    'memcached_matches',
    'nest_log_sink_matches',
]
struct_ndpi_flow_tcp_struct._fields_ = [
    ('smtp_command_bitmask', u_int16_t),
    ('pop_command_bitmask', u_int16_t),
    ('qq_nxt_len', u_int16_t),
    ('wa_matched_so_far', u_int8_t),
    ('tds_login_version', u_int8_t),
    ('irc_stage', u_int8_t),
    ('irc_port', u_int8_t),
    ('h323_valid_packets', u_int8_t),
    ('gnutella_msg_id', u_int8_t * 3),
    ('irc_3a_counter', u_int32_t, 3),
    ('irc_stage2', u_int32_t, 5),
    ('irc_direction', u_int32_t, 2),
    ('irc_0x1000_full', u_int32_t, 1),
    ('soulseek_stage', u_int32_t, 2),
    ('tds_stage', u_int32_t, 3),
    ('usenet_stage', u_int32_t, 2),
    ('imesh_stage', u_int32_t, 4),
    ('http_setup_dir', u_int32_t, 2),
    ('http_stage', u_int32_t, 2),
    ('http_empty_line_seen', u_int32_t, 1),
    ('http_wait_for_retransmission', u_int32_t, 1),
    ('gnutella_stage', u_int32_t, 2),
    ('mms_stage', u_int32_t, 2),
    ('yahoo_sip_comm', u_int32_t, 1),
    ('yahoo_http_proxy_stage', u_int32_t, 2),
    ('msn_stage', u_int32_t, 3),
    ('msn_ssl_ft', u_int32_t, 2),
    ('ssh_stage', u_int32_t, 3),
    ('vnc_stage', u_int32_t, 2),
    ('telnet_stage', u_int32_t, 2),
    ('ssl_seen_client_cert', u_int8_t, 1),
    ('ssl_seen_server_cert', u_int8_t, 1),
    ('ssl_seen_certificate', u_int8_t, 1),
    ('ssl_stage', u_int8_t, 2),
    ('postgres_stage', u_int32_t, 3),
    ('ddlink_server_direction', u_int32_t, 1),
    ('seen_syn', u_int32_t, 1),
    ('seen_syn_ack', u_int32_t, 1),
    ('seen_ack', u_int32_t, 1),
    ('icecast_stage', u_int32_t, 1),
    ('dofus_stage', u_int32_t, 1),
    ('fiesta_stage', u_int32_t, 2),
    ('wow_stage', u_int32_t, 2),
    ('veoh_tv_stage', u_int32_t, 2),
    ('shoutcast_stage', u_int32_t, 2),
    ('rtp_special_packets_seen', u_int32_t, 1),
    ('mail_pop_stage', u_int32_t, 2),
    ('mail_imap_stage', u_int32_t, 3),
    ('mail_imap_starttls', u_int32_t, 2),
    ('skype_packet_id', u_int8_t),
    ('citrix_packet_id', u_int8_t),
    ('lotus_notes_packet_id', u_int8_t),
    ('teamviewer_stage', u_int8_t),
    ('prev_zmq_pkt_len', u_int8_t),
    ('prev_zmq_pkt', u_char * 10),
    ('ppstream_stage', u_int32_t, 3),
    ('memcached_matches', u_int8_t),
    ('nest_log_sink_matches', u_int8_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 618
class struct_ndpi_flow_udp_struct(Structure):
    pass

struct_ndpi_flow_udp_struct.__slots__ = [
    'battlefield_msg_id',
    'snmp_msg_id',
    'battlefield_stage',
    'snmp_stage',
    'ppstream_stage',
    'halflife2_stage',
    'tftp_stage',
    'aimini_stage',
    'xbox_stage',
    'wsus_stage',
    'skype_packet_id',
    'teamviewer_stage',
    'eaq_pkt_id',
    'eaq_sequence',
    'rx_conn_epoch',
    'rx_conn_id',
    'memcached_matches',
]
struct_ndpi_flow_udp_struct._fields_ = [
    ('battlefield_msg_id', u_int32_t),
    ('snmp_msg_id', u_int32_t),
    ('battlefield_stage', u_int32_t, 3),
    ('snmp_stage', u_int32_t, 2),
    ('ppstream_stage', u_int32_t, 3),
    ('halflife2_stage', u_int32_t, 2),
    ('tftp_stage', u_int32_t, 1),
    ('aimini_stage', u_int32_t, 5),
    ('xbox_stage', u_int32_t, 1),
    ('wsus_stage', u_int32_t, 1),
    ('skype_packet_id', u_int8_t),
    ('teamviewer_stage', u_int8_t),
    ('eaq_pkt_id', u_int8_t),
    ('eaq_sequence', u_int32_t),
    ('rx_conn_epoch', u_int32_t),
    ('rx_conn_id', u_int32_t),
    ('memcached_matches', u_int8_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 673
class struct_ndpi_int_one_line_struct(Structure):
    pass

struct_ndpi_int_one_line_struct.__slots__ = [
    'ptr',
    'len',
]
struct_ndpi_int_one_line_struct._fields_ = [
    ('ptr', POINTER(u_int8_t)),
    ('len', u_int16_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 678
class struct_ndpi_packet_struct(Structure):
    pass

struct_ndpi_packet_struct.__slots__ = [
    'iph',
    'iphv6',
    'tcp',
    'udp',
    'generic_l4_ptr',
    'payload',
    'tick_timestamp',
    'tick_timestamp_l',
    'detected_protocol_stack',
    'detected_subprotocol_stack',
    'protocol_stack_info',
    'line',
    'host_line',
    'forwarded_line',
    'referer_line',
    'content_line',
    'accept_line',
    'user_agent_line',
    'http_url_name',
    'http_encoding',
    'http_transfer_encoding',
    'http_contentlen',
    'http_cookie',
    'http_origin',
    'http_x_session_type',
    'server_line',
    'http_method',
    'http_response',
    'http_num_headers',
    'l3_packet_len',
    'l4_packet_len',
    'payload_packet_len',
    'actual_payload_len',
    'num_retried_bytes',
    'parsed_lines',
    'parsed_unix_lines',
    'empty_line_position',
    'tcp_retransmission',
    'l4_protocol',
    'ssl_certificate_detected',
    'ssl_certificate_num_checks',
    'packet_lines_parsed_complete',
    'packet_direction',
    'empty_line_position_set',
]
struct_ndpi_packet_struct._fields_ = [
    ('iph', POINTER(struct_ndpi_iphdr)),
    ('iphv6', POINTER(struct_ndpi_ipv6hdr)),
    ('tcp', POINTER(struct_ndpi_tcphdr)),
    ('udp', POINTER(struct_ndpi_udphdr)),
    ('generic_l4_ptr', POINTER(u_int8_t)),
    ('payload', POINTER(u_int8_t)),
    ('tick_timestamp', u_int32_t),
    ('tick_timestamp_l', u_int64_t),
    ('detected_protocol_stack', u_int16_t * 2),
    ('detected_subprotocol_stack', u_int8_t * 2),
    ('protocol_stack_info', u_int16_t),
    ('line', struct_ndpi_int_one_line_struct * 64),
    ('host_line', struct_ndpi_int_one_line_struct),
    ('forwarded_line', struct_ndpi_int_one_line_struct),
    ('referer_line', struct_ndpi_int_one_line_struct),
    ('content_line', struct_ndpi_int_one_line_struct),
    ('accept_line', struct_ndpi_int_one_line_struct),
    ('user_agent_line', struct_ndpi_int_one_line_struct),
    ('http_url_name', struct_ndpi_int_one_line_struct),
    ('http_encoding', struct_ndpi_int_one_line_struct),
    ('http_transfer_encoding', struct_ndpi_int_one_line_struct),
    ('http_contentlen', struct_ndpi_int_one_line_struct),
    ('http_cookie', struct_ndpi_int_one_line_struct),
    ('http_origin', struct_ndpi_int_one_line_struct),
    ('http_x_session_type', struct_ndpi_int_one_line_struct),
    ('server_line', struct_ndpi_int_one_line_struct),
    ('http_method', struct_ndpi_int_one_line_struct),
    ('http_response', struct_ndpi_int_one_line_struct),
    ('http_num_headers', u_int8_t),
    ('l3_packet_len', u_int16_t),
    ('l4_packet_len', u_int16_t),
    ('payload_packet_len', u_int16_t),
    ('actual_payload_len', u_int16_t),
    ('num_retried_bytes', u_int16_t),
    ('parsed_lines', u_int16_t),
    ('parsed_unix_lines', u_int16_t),
    ('empty_line_position', u_int16_t),
    ('tcp_retransmission', u_int8_t),
    ('l4_protocol', u_int8_t),
    ('ssl_certificate_detected', u_int8_t, 4),
    ('ssl_certificate_num_checks', u_int8_t, 4),
    ('packet_lines_parsed_complete', u_int8_t, 1),
    ('packet_direction', u_int8_t, 1),
    ('empty_line_position_set', u_int8_t, 1),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 737
class struct_ndpi_detection_module_struct(Structure):
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1036
class struct_ndpi_flow_struct(Structure):
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 740
class struct_ndpi_call_function_struct(Structure):
    pass

struct_ndpi_call_function_struct.__slots__ = [
    'detection_bitmask',
    'excluded_protocol_bitmask',
    'ndpi_selection_bitmask',
    'func',
    'detection_feature',
]
struct_ndpi_call_function_struct._fields_ = [
    ('detection_bitmask', ndpi_protocol_bitmask_struct_t),
    ('excluded_protocol_bitmask', ndpi_protocol_bitmask_struct_t),
    ('ndpi_selection_bitmask', u_int32_t),
    ('func', CFUNCTYPE(UNCHECKED(None), POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct))),
    ('detection_feature', u_int8_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 748
class struct_ndpi_subprotocol_conf_struct(Structure):
    pass

struct_ndpi_subprotocol_conf_struct.__slots__ = [
    'func',
]
struct_ndpi_subprotocol_conf_struct._fields_ = [
    ('func', CFUNCTYPE(UNCHECKED(None), POINTER(struct_ndpi_detection_module_struct), String, String, c_int)),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 754
class struct_anon_84(Structure):
    pass

struct_anon_84.__slots__ = [
    'port_low',
    'port_high',
]
struct_anon_84._fields_ = [
    ('port_low', u_int16_t),
    ('port_high', u_int16_t),
]

ndpi_port_range = struct_anon_84 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 754

enum_anon_85 = c_int # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 764

NDPI_PROTOCOL_SAFE = 0 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 764

NDPI_PROTOCOL_ACCEPTABLE = (NDPI_PROTOCOL_SAFE + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 764

NDPI_PROTOCOL_FUN = (NDPI_PROTOCOL_ACCEPTABLE + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 764

NDPI_PROTOCOL_UNSAFE = (NDPI_PROTOCOL_FUN + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 764

NDPI_PROTOCOL_POTENTIALLY_DANGEROUS = (NDPI_PROTOCOL_UNSAFE + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 764

NDPI_PROTOCOL_TRACKER_ADS = (NDPI_PROTOCOL_POTENTIALLY_DANGEROUS + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 764

NDPI_PROTOCOL_UNRATED = (NDPI_PROTOCOL_TRACKER_ADS + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 764

ndpi_protocol_breed_t = enum_anon_85 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 764

enum_anon_86 = c_int # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_UNSPECIFIED = 0 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_MEDIA = (NDPI_PROTOCOL_CATEGORY_UNSPECIFIED + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_VPN = (NDPI_PROTOCOL_CATEGORY_MEDIA + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_MAIL = (NDPI_PROTOCOL_CATEGORY_VPN + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_DATA_TRANSFER = (NDPI_PROTOCOL_CATEGORY_MAIL + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_WEB = (NDPI_PROTOCOL_CATEGORY_DATA_TRANSFER + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_SOCIAL_NETWORK = (NDPI_PROTOCOL_CATEGORY_WEB + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_DOWNLOAD_FT = (NDPI_PROTOCOL_CATEGORY_SOCIAL_NETWORK + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_GAME = (NDPI_PROTOCOL_CATEGORY_DOWNLOAD_FT + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_CHAT = (NDPI_PROTOCOL_CATEGORY_GAME + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_VOIP = (NDPI_PROTOCOL_CATEGORY_CHAT + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_DATABASE = (NDPI_PROTOCOL_CATEGORY_VOIP + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_REMOTE_ACCESS = (NDPI_PROTOCOL_CATEGORY_DATABASE + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_CLOUD = (NDPI_PROTOCOL_CATEGORY_REMOTE_ACCESS + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_NETWORK = (NDPI_PROTOCOL_CATEGORY_CLOUD + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_COLLABORATIVE = (NDPI_PROTOCOL_CATEGORY_NETWORK + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_RPC = (NDPI_PROTOCOL_CATEGORY_COLLABORATIVE + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_STREAMING = (NDPI_PROTOCOL_CATEGORY_RPC + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_SYSTEM_OS = (NDPI_PROTOCOL_CATEGORY_STREAMING + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_SW_UPDATE = (NDPI_PROTOCOL_CATEGORY_SYSTEM_OS + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_CUSTOM_1 = (NDPI_PROTOCOL_CATEGORY_SW_UPDATE + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_CUSTOM_2 = (NDPI_PROTOCOL_CATEGORY_CUSTOM_1 + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_CUSTOM_3 = (NDPI_PROTOCOL_CATEGORY_CUSTOM_2 + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_CUSTOM_4 = (NDPI_PROTOCOL_CATEGORY_CUSTOM_3 + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_CUSTOM_5 = (NDPI_PROTOCOL_CATEGORY_CUSTOM_4 + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_MUSIC = (NDPI_PROTOCOL_CATEGORY_CUSTOM_5 + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_VIDEO = (NDPI_PROTOCOL_CATEGORY_MUSIC + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_SHOPPING = (NDPI_PROTOCOL_CATEGORY_VIDEO + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_PRODUCTIVITY = (NDPI_PROTOCOL_CATEGORY_SHOPPING + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_CATEGORY_FILE_SHARING = (NDPI_PROTOCOL_CATEGORY_PRODUCTIVITY + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

CUSTOM_CATEGORY_MINING = 99 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

CUSTOM_CATEGORY_MALWARE = 100 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

CUSTOM_CATEGORY_ADVERTISEMENT = 101 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

CUSTOM_CATEGORY_BANNED_SITE = 102 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

CUSTOM_CATEGORY_SITE_UNAVAILABLE = 103 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

CUSTOM_CATEGORY_ALLOWED_SITE = 104 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

CUSTOM_CATEGORY_ANTIMALWARE = 105 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

NDPI_PROTOCOL_NUM_CATEGORIES = (CUSTOM_CATEGORY_ANTIMALWARE + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

ndpi_protocol_category_t = enum_anon_86 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 834

enum_anon_87 = c_int # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 842

ndpi_pref_http_dont_dissect_response = 0 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 842

ndpi_pref_dns_dont_dissect_response = (ndpi_pref_http_dont_dissect_response + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 842

ndpi_pref_direction_detect_disable = (ndpi_pref_dns_dont_dissect_response + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 842

ndpi_pref_disable_metadata_export = (ndpi_pref_direction_detect_disable + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 842

ndpi_pref_enable_category_substring_match = (ndpi_pref_disable_metadata_export + 1) # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 842

ndpi_detection_preference = enum_anon_87 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 842

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 853
class struct_ndpi_proto_defaults(Structure):
    pass

struct_ndpi_proto_defaults.__slots__ = [
    'protoName',
    'protoCategory',
    'can_have_a_subprotocol',
    'protoId',
    'protoIdx',
    'master_tcp_protoId',
    'master_udp_protoId',
    'protoBreed',
    'func',
]
struct_ndpi_proto_defaults._fields_ = [
    ('protoName', String),
    ('protoCategory', ndpi_protocol_category_t),
    ('can_have_a_subprotocol', u_int8_t),
    ('protoId', u_int16_t),
    ('protoIdx', u_int16_t),
    ('master_tcp_protoId', u_int16_t * 2),
    ('master_udp_protoId', u_int16_t * 2),
    ('protoBreed', ndpi_protocol_breed_t),
    ('func', CFUNCTYPE(UNCHECKED(None), POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct))),
]

ndpi_proto_defaults_t = struct_ndpi_proto_defaults # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 853

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 859
class struct_ndpi_default_ports_tree_node(Structure):
    pass

struct_ndpi_default_ports_tree_node.__slots__ = [
    'proto',
    'customUserProto',
    'default_port',
]
struct_ndpi_default_ports_tree_node._fields_ = [
    ('proto', POINTER(ndpi_proto_defaults_t)),
    ('customUserProto', u_int8_t),
    ('default_port', u_int16_t),
]

ndpi_default_ports_tree_node_t = struct_ndpi_default_ports_tree_node # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 859

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 864
class struct__ndpi_automa(Structure):
    pass

struct__ndpi_automa.__slots__ = [
    'ac_automa',
    'ac_automa_finalized',
]
struct__ndpi_automa._fields_ = [
    ('ac_automa', POINTER(None)),
    ('ac_automa_finalized', u_int8_t),
]

ndpi_automa = struct__ndpi_automa # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 864

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 874
class struct_ndpi_proto(Structure):
    pass

struct_ndpi_proto.__slots__ = [
    'master_protocol',
    'app_protocol',
    'category',
]
struct_ndpi_proto._fields_ = [
    ('master_protocol', u_int16_t),
    ('app_protocol', u_int16_t),
    ('category', ndpi_protocol_category_t),
]

ndpi_protocol = struct_ndpi_proto # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 874

enum_anon_88 = c_int # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1034

ndpi_cipher_safe = 0 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1034

ndpi_cipher_weak = 1 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1034

ndpi_cipher_insecure = 2 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1034

ndpi_cipher_weakness = enum_anon_88 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1034

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1063
class union_anon_89(Union):
    pass

union_anon_89.__slots__ = [
    'tcp',
    'udp',
]
union_anon_89._fields_ = [
    ('tcp', struct_ndpi_flow_tcp_struct),
    ('udp', struct_ndpi_flow_udp_struct),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1083
class struct_anon_90(Structure):
    pass

struct_anon_90.__slots__ = [
    'method',
    'url',
    'content_type',
    'num_request_headers',
    'num_response_headers',
    'request_version',
    'response_status_code',
]
struct_anon_90._fields_ = [
    ('method', ndpi_http_method),
    ('url', String),
    ('content_type', String),
    ('num_request_headers', u_int8_t),
    ('num_response_headers', u_int8_t),
    ('request_version', u_int8_t),
    ('response_status_code', u_int16_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1093
class struct_anon_91(Structure):
    pass

struct_anon_91.__slots__ = [
    'num_queries',
    'num_answers',
    'reply_code',
    'query_type',
    'query_class',
    'rsp_type',
    'rsp_addr',
]
struct_anon_91._fields_ = [
    ('num_queries', u_int8_t),
    ('num_answers', u_int8_t),
    ('reply_code', u_int8_t),
    ('query_type', u_int16_t),
    ('query_class', u_int16_t),
    ('rsp_type', u_int16_t),
    ('rsp_addr', ndpi_ip_addr_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1099
class struct_anon_92(Structure):
    pass

struct_anon_92.__slots__ = [
    'request_code',
    'version',
]
struct_anon_92._fields_ = [
    ('request_code', u_int8_t),
    ('version', u_int8_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1105
class struct_anon_93(Structure):
    pass

struct_anon_93.__slots__ = [
    'ssl_version',
    'client_certificate',
    'server_certificate',
    'server_organization',
    'ja3_client',
    'ja3_server',
    'server_cipher',
    'server_unsafe_cipher',
]
struct_anon_93._fields_ = [
    ('ssl_version', u_int16_t),
    ('client_certificate', c_char * 64),
    ('server_certificate', c_char * 64),
    ('server_organization', c_char * 64),
    ('ja3_client', c_char * 33),
    ('ja3_server', c_char * 33),
    ('server_cipher', u_int16_t),
    ('server_unsafe_cipher', ndpi_cipher_weakness),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1113
class struct_anon_94(Structure):
    pass

struct_anon_94.__slots__ = [
    'num_udp_pkts',
    'num_processed_pkts',
    'num_binding_requests',
    'is_skype',
]
struct_anon_94._fields_ = [
    ('num_udp_pkts', u_int8_t),
    ('num_processed_pkts', u_int8_t),
    ('num_binding_requests', u_int8_t),
    ('is_skype', u_int8_t),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1104
class struct_anon_95(Structure):
    pass

struct_anon_95.__slots__ = [
    'ssl',
    'stun',
]
struct_anon_95._fields_ = [
    ('ssl', struct_anon_93),
    ('stun', struct_anon_94),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1120
class struct_anon_96(Structure):
    pass

struct_anon_96.__slots__ = [
    'client_signature',
    'server_signature',
]
struct_anon_96._fields_ = [
    ('client_signature', c_char * 48),
    ('server_signature', c_char * 48),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1124
class struct_anon_97(Structure):
    pass

struct_anon_97.__slots__ = [
    'answer',
]
struct_anon_97._fields_ = [
    ('answer', c_char * 96),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1128
class struct_anon_98(Structure):
    pass

struct_anon_98.__slots__ = [
    'version',
]
struct_anon_98._fields_ = [
    ('version', c_char * 96),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1132
class struct_anon_99(Structure):
    pass

struct_anon_99.__slots__ = [
    'detected_os',
    'nat_ip',
]
struct_anon_99._fields_ = [
    ('detected_os', u_char * 32),
    ('nat_ip', u_char * 24),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1139
class struct_anon_100(Structure):
    pass

struct_anon_100.__slots__ = [
    'hash',
]
struct_anon_100._fields_ = [
    ('hash', u_char * 20),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1144
class struct_anon_101(Structure):
    pass

struct_anon_101.__slots__ = [
    'fingerprint',
    'class_ident',
]
struct_anon_101._fields_ = [
    ('fingerprint', c_char * 48),
    ('class_ident', c_char * 48),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1091
class union_anon_102(Union):
    pass

union_anon_102.__slots__ = [
    'dns',
    'ntp',
    'stun_ssl',
    'ssh',
    'mdns',
    'ubntac2',
    'http',
    'bittorrent',
    'dhcp',
]
union_anon_102._fields_ = [
    ('dns', struct_anon_91),
    ('ntp', struct_anon_92),
    ('stun_ssl', struct_anon_95),
    ('ssh', struct_anon_96),
    ('mdns', struct_anon_97),
    ('ubntac2', struct_anon_98),
    ('http', struct_anon_99),
    ('bittorrent', struct_anon_100),
    ('dhcp', struct_anon_101),
]

struct_ndpi_flow_struct.__slots__ = [
    'detected_protocol_stack',
    'protocol_stack_info',
    'guessed_protocol_id',
    'guessed_host_protocol_id',
    'guessed_category',
    'guessed_header_category',
    'protocol_id_already_guessed',
    'host_already_guessed',
    'init_finished',
    'setup_packet_direction',
    'packet_direction',
    'check_extra_packets',
    'next_tcp_seq_nr',
    'max_extra_packets_to_check',
    'num_extra_packets_checked',
    'num_processed_pkts',
    'extra_packets_func',
    'l4',
    'server_id',
    'host_server_name',
    'http',
    'protos',
    'excluded_protocol_bitmask',
    'category',
    'redis_s2d_first_char',
    'redis_d2s_first_char',
    'packet_counter',
    'packet_direction_counter',
    'byte_counter',
    'bittorrent_stage',
    'directconnect_stage',
    'sip_yahoo_voice',
    'http_detected',
    'http_upper_protocol',
    'http_lower_protocol',
    'rtsprdt_stage',
    'rtsp_control_flow',
    'yahoo_detection_finished',
    'zattoo_stage',
    'qq_stage',
    'thunder_stage',
    'oscar_ssl_voice_stage',
    'oscar_video_voice',
    'florensia_stage',
    'socks5_stage',
    'socks4_stage',
    'edonkey_stage',
    'ftp_control_stage',
    'rtmp_stage',
    'pando_stage',
    'steam_stage',
    'steam_stage1',
    'steam_stage2',
    'steam_stage3',
    'pplive_stage1',
    'pplive_stage2',
    'pplive_stage3',
    'starcraft_udp_stage',
    'ovpn_session_id',
    'ovpn_counter',
    'tinc_state',
    'tinc_cache_entry',
    'csgo_strid',
    'csgo_state',
    'csgo_s2',
    'csgo_id2',
    'kxun_counter',
    'iqiyi_counter',
    'packet',
    'flow',
    'src',
    'dst',
]
struct_ndpi_flow_struct._fields_ = [
    ('detected_protocol_stack', u_int16_t * 2),
    ('protocol_stack_info', u_int16_t),
    ('guessed_protocol_id', u_int16_t),
    ('guessed_host_protocol_id', u_int16_t),
    ('guessed_category', u_int16_t),
    ('guessed_header_category', u_int16_t),
    ('protocol_id_already_guessed', u_int8_t, 1),
    ('host_already_guessed', u_int8_t, 1),
    ('init_finished', u_int8_t, 1),
    ('setup_packet_direction', u_int8_t, 1),
    ('packet_direction', u_int8_t, 1),
    ('check_extra_packets', u_int8_t, 1),
    ('next_tcp_seq_nr', u_int32_t * 2),
    ('max_extra_packets_to_check', u_int8_t),
    ('num_extra_packets_checked', u_int8_t),
    ('num_processed_pkts', u_int8_t),
    ('extra_packets_func', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct))),
    ('l4', union_anon_89),
    ('server_id', POINTER(struct_ndpi_id_struct)),
    ('host_server_name', u_char * 256),
    ('http', struct_anon_90),
    ('protos', union_anon_102),
    ('excluded_protocol_bitmask', ndpi_protocol_bitmask_struct_t),
    ('category', ndpi_protocol_category_t),
    ('redis_s2d_first_char', u_int8_t),
    ('redis_d2s_first_char', u_int8_t),
    ('packet_counter', u_int16_t),
    ('packet_direction_counter', u_int16_t * 2),
    ('byte_counter', u_int16_t * 2),
    ('bittorrent_stage', u_int8_t),
    ('directconnect_stage', u_int8_t, 2),
    ('sip_yahoo_voice', u_int8_t, 1),
    ('http_detected', u_int8_t, 1),
    ('http_upper_protocol', u_int16_t),
    ('http_lower_protocol', u_int16_t),
    ('rtsprdt_stage', u_int8_t, 2),
    ('rtsp_control_flow', u_int8_t, 1),
    ('yahoo_detection_finished', u_int8_t, 2),
    ('zattoo_stage', u_int8_t, 3),
    ('qq_stage', u_int8_t, 3),
    ('thunder_stage', u_int8_t, 2),
    ('oscar_ssl_voice_stage', u_int8_t, 3),
    ('oscar_video_voice', u_int8_t, 1),
    ('florensia_stage', u_int8_t, 1),
    ('socks5_stage', u_int8_t, 2),
    ('socks4_stage', u_int8_t, 2),
    ('edonkey_stage', u_int8_t, 2),
    ('ftp_control_stage', u_int8_t, 2),
    ('rtmp_stage', u_int8_t, 2),
    ('pando_stage', u_int8_t, 3),
    ('steam_stage', u_int16_t, 3),
    ('steam_stage1', u_int16_t, 3),
    ('steam_stage2', u_int16_t, 2),
    ('steam_stage3', u_int16_t, 2),
    ('pplive_stage1', u_int8_t, 3),
    ('pplive_stage2', u_int8_t, 2),
    ('pplive_stage3', u_int8_t, 2),
    ('starcraft_udp_stage', u_int8_t, 3),
    ('ovpn_session_id', u_int8_t * 8),
    ('ovpn_counter', u_int8_t),
    ('tinc_state', u_int8_t),
    ('tinc_cache_entry', struct_tinc_cache_entry),
    ('csgo_strid', u_int8_t * 18),
    ('csgo_state', u_int8_t),
    ('csgo_s2', u_int8_t),
    ('csgo_id2', u_int32_t),
    ('kxun_counter', u_int16_t),
    ('iqiyi_counter', u_int16_t),
    ('packet', struct_ndpi_packet_struct),
    ('flow', POINTER(struct_ndpi_flow_struct)),
    ('src', POINTER(struct_ndpi_id_struct)),
    ('dst', POINTER(struct_ndpi_id_struct)),
]

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1248
class struct_anon_103(Structure):
    pass

struct_anon_103.__slots__ = [
    'string_to_match',
    'string2_to_match',
    'pattern_to_match',
    'proto_name',
    'protocol_id',
    'protocol_category',
    'protocol_breed',
]
struct_anon_103._fields_ = [
    ('string_to_match', String),
    ('string2_to_match', String),
    ('pattern_to_match', String),
    ('proto_name', String),
    ('protocol_id', c_int),
    ('protocol_category', ndpi_protocol_category_t),
    ('protocol_breed', ndpi_protocol_breed_t),
]

ndpi_protocol_match = struct_anon_103 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1248

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1254
class struct_anon_104(Structure):
    pass

struct_anon_104.__slots__ = [
    'network',
    'cidr',
    'value',
]
struct_anon_104._fields_ = [
    ('network', u_int32_t),
    ('cidr', u_int8_t),
    ('value', u_int8_t),
]

ndpi_network = struct_anon_104 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1254

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1260
class struct_anon_105(Structure):
    pass

struct_anon_105.__slots__ = [
    'protocol_id',
    'protocol_category',
    'protocol_breed',
]
struct_anon_105._fields_ = [
    ('protocol_id', c_int),
    ('protocol_category', ndpi_protocol_category_t),
    ('protocol_breed', ndpi_protocol_breed_t),
]

ndpi_protocol_match_result = struct_anon_105 # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1260

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 31
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_build_default_ports_range'):
        continue
    ndpi_build_default_ports_range = _lib.ndpi_build_default_ports_range
    ndpi_build_default_ports_range.argtypes = [POINTER(ndpi_port_range), u_int16_t, u_int16_t, u_int16_t, u_int16_t, u_int16_t, u_int16_t, u_int16_t, u_int16_t, u_int16_t, u_int16_t]
    ndpi_build_default_ports_range.restype = POINTER(ndpi_port_range)
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 38
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_build_default_ports'):
        continue
    ndpi_build_default_ports = _lib.ndpi_build_default_ports
    ndpi_build_default_ports.argtypes = [POINTER(ndpi_port_range), u_int16_t, u_int16_t, u_int16_t, u_int16_t, u_int16_t]
    ndpi_build_default_ports.restype = POINTER(ndpi_port_range)
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 46
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_tcp_or_udp_raw'):
        continue
    ndpi_search_tcp_or_udp_raw = _lib.ndpi_search_tcp_or_udp_raw
    ndpi_search_tcp_or_udp_raw.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct), u_int8_t, u_int32_t, u_int32_t, u_int16_t, u_int16_t]
    ndpi_search_tcp_or_udp_raw.restype = u_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 52
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_tcp_or_udp'):
        continue
    ndpi_search_tcp_or_udp = _lib.ndpi_search_tcp_or_udp
    ndpi_search_tcp_or_udp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_tcp_or_udp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 55
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_diameter'):
        continue
    ndpi_search_diameter = _lib.ndpi_search_diameter
    ndpi_search_diameter.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_diameter.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 56
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_bittorrent'):
        continue
    ndpi_search_bittorrent = _lib.ndpi_search_bittorrent
    ndpi_search_bittorrent.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_bittorrent.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 57
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_lisp'):
        continue
    ndpi_search_lisp = _lib.ndpi_search_lisp
    ndpi_search_lisp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_lisp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 58
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_edonkey'):
        continue
    ndpi_search_edonkey = _lib.ndpi_search_edonkey
    ndpi_search_edonkey.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_edonkey.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 59
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_fasttrack_tcp'):
        continue
    ndpi_search_fasttrack_tcp = _lib.ndpi_search_fasttrack_tcp
    ndpi_search_fasttrack_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_fasttrack_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 60
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_gnutella'):
        continue
    ndpi_search_gnutella = _lib.ndpi_search_gnutella
    ndpi_search_gnutella.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_gnutella.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 61
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_directconnect'):
        continue
    ndpi_search_directconnect = _lib.ndpi_search_directconnect
    ndpi_search_directconnect.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_directconnect.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 62
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_applejuice_tcp'):
        continue
    ndpi_search_applejuice_tcp = _lib.ndpi_search_applejuice_tcp
    ndpi_search_applejuice_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_applejuice_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 63
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_i23v5'):
        continue
    ndpi_search_i23v5 = _lib.ndpi_search_i23v5
    ndpi_search_i23v5.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_i23v5.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 64
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_socrates'):
        continue
    ndpi_search_socrates = _lib.ndpi_search_socrates
    ndpi_search_socrates.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_socrates.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 65
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_soulseek_tcp'):
        continue
    ndpi_search_soulseek_tcp = _lib.ndpi_search_soulseek_tcp
    ndpi_search_soulseek_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_soulseek_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 66
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_msn'):
        continue
    ndpi_search_msn = _lib.ndpi_search_msn
    ndpi_search_msn.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_msn.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 67
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_yahoo'):
        continue
    ndpi_search_yahoo = _lib.ndpi_search_yahoo
    ndpi_search_yahoo.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_yahoo.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 68
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_oscar'):
        continue
    ndpi_search_oscar = _lib.ndpi_search_oscar
    ndpi_search_oscar.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_oscar.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 69
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_jabber_tcp'):
        continue
    ndpi_search_jabber_tcp = _lib.ndpi_search_jabber_tcp
    ndpi_search_jabber_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_jabber_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 70
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_irc_tcp'):
        continue
    ndpi_search_irc_tcp = _lib.ndpi_search_irc_tcp
    ndpi_search_irc_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_irc_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 71
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_sip'):
        continue
    ndpi_search_sip = _lib.ndpi_search_sip
    ndpi_search_sip.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_sip.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 72
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_hep'):
        continue
    ndpi_search_hep = _lib.ndpi_search_hep
    ndpi_search_hep.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_hep.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 73
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_direct_download_link_tcp'):
        continue
    ndpi_search_direct_download_link_tcp = _lib.ndpi_search_direct_download_link_tcp
    ndpi_search_direct_download_link_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_direct_download_link_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 74
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_mail_pop_tcp'):
        continue
    ndpi_search_mail_pop_tcp = _lib.ndpi_search_mail_pop_tcp
    ndpi_search_mail_pop_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_mail_pop_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 75
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_mail_imap_tcp'):
        continue
    ndpi_search_mail_imap_tcp = _lib.ndpi_search_mail_imap_tcp
    ndpi_search_mail_imap_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_mail_imap_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 76
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_mail_smtp_tcp'):
        continue
    ndpi_search_mail_smtp_tcp = _lib.ndpi_search_mail_smtp_tcp
    ndpi_search_mail_smtp_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_mail_smtp_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 77
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_http_tcp'):
        continue
    ndpi_search_http_tcp = _lib.ndpi_search_http_tcp
    ndpi_search_http_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_http_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 78
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_http_subprotocol_conf'):
        continue
    ndpi_http_subprotocol_conf = _lib.ndpi_http_subprotocol_conf
    ndpi_http_subprotocol_conf.argtypes = [POINTER(struct_ndpi_detection_module_struct), String, String, c_int]
    ndpi_http_subprotocol_conf.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 79
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_ftp_control'):
        continue
    ndpi_search_ftp_control = _lib.ndpi_search_ftp_control
    ndpi_search_ftp_control.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_ftp_control.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 80
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_ftp_data'):
        continue
    ndpi_search_ftp_data = _lib.ndpi_search_ftp_data
    ndpi_search_ftp_data.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_ftp_data.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 81
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_usenet_tcp'):
        continue
    ndpi_search_usenet_tcp = _lib.ndpi_search_usenet_tcp
    ndpi_search_usenet_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_usenet_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 82
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_dns'):
        continue
    ndpi_search_dns = _lib.ndpi_search_dns
    ndpi_search_dns.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_dns.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 83
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_rtsp_tcp_udp'):
        continue
    ndpi_search_rtsp_tcp_udp = _lib.ndpi_search_rtsp_tcp_udp
    ndpi_search_rtsp_tcp_udp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_rtsp_tcp_udp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 84
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_filetopia_tcp'):
        continue
    ndpi_search_filetopia_tcp = _lib.ndpi_search_filetopia_tcp
    ndpi_search_filetopia_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_filetopia_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 85
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_vmware'):
        continue
    ndpi_search_vmware = _lib.ndpi_search_vmware
    ndpi_search_vmware.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_vmware.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 86
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_ssl_tcp'):
        continue
    ndpi_search_ssl_tcp = _lib.ndpi_search_ssl_tcp
    ndpi_search_ssl_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_ssl_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 87
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_mms_tcp'):
        continue
    ndpi_search_mms_tcp = _lib.ndpi_search_mms_tcp
    ndpi_search_mms_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_mms_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 88
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_icecast_tcp'):
        continue
    ndpi_search_icecast_tcp = _lib.ndpi_search_icecast_tcp
    ndpi_search_icecast_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_icecast_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 89
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_shoutcast_tcp'):
        continue
    ndpi_search_shoutcast_tcp = _lib.ndpi_search_shoutcast_tcp
    ndpi_search_shoutcast_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_shoutcast_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 90
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_veohtv_tcp'):
        continue
    ndpi_search_veohtv_tcp = _lib.ndpi_search_veohtv_tcp
    ndpi_search_veohtv_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_veohtv_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 91
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_openft_tcp'):
        continue
    ndpi_search_openft_tcp = _lib.ndpi_search_openft_tcp
    ndpi_search_openft_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_openft_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 92
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_stun'):
        continue
    ndpi_search_stun = _lib.ndpi_search_stun
    ndpi_search_stun.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_stun.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 93
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_tvants_udp'):
        continue
    ndpi_search_tvants_udp = _lib.ndpi_search_tvants_udp
    ndpi_search_tvants_udp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_tvants_udp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 94
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_sopcast'):
        continue
    ndpi_search_sopcast = _lib.ndpi_search_sopcast
    ndpi_search_sopcast.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_sopcast.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 95
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_tvuplayer'):
        continue
    ndpi_search_tvuplayer = _lib.ndpi_search_tvuplayer
    ndpi_search_tvuplayer.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_tvuplayer.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 96
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_ppstream'):
        continue
    ndpi_search_ppstream = _lib.ndpi_search_ppstream
    ndpi_search_ppstream.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_ppstream.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 97
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_pplive'):
        continue
    ndpi_search_pplive = _lib.ndpi_search_pplive
    ndpi_search_pplive.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_pplive.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 98
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_iax'):
        continue
    ndpi_search_iax = _lib.ndpi_search_iax
    ndpi_search_iax.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_iax.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 99
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_mgcp'):
        continue
    ndpi_search_mgcp = _lib.ndpi_search_mgcp
    ndpi_search_mgcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_mgcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 100
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_zattoo'):
        continue
    ndpi_search_zattoo = _lib.ndpi_search_zattoo
    ndpi_search_zattoo.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_zattoo.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 101
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_qq'):
        continue
    ndpi_search_qq = _lib.ndpi_search_qq
    ndpi_search_qq.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_qq.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 102
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_feidian'):
        continue
    ndpi_search_feidian = _lib.ndpi_search_feidian
    ndpi_search_feidian.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_feidian.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 103
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_ssh_tcp'):
        continue
    ndpi_search_ssh_tcp = _lib.ndpi_search_ssh_tcp
    ndpi_search_ssh_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_ssh_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 104
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_ayiya'):
        continue
    ndpi_search_ayiya = _lib.ndpi_search_ayiya
    ndpi_search_ayiya.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_ayiya.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 105
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_thunder'):
        continue
    ndpi_search_thunder = _lib.ndpi_search_thunder
    ndpi_search_thunder.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_thunder.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 106
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_activesync'):
        continue
    ndpi_search_activesync = _lib.ndpi_search_activesync
    ndpi_search_activesync.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_activesync.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 107
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_in_non_tcp_udp'):
        continue
    ndpi_search_in_non_tcp_udp = _lib.ndpi_search_in_non_tcp_udp
    ndpi_search_in_non_tcp_udp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_in_non_tcp_udp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 108
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_vnc_tcp'):
        continue
    ndpi_search_vnc_tcp = _lib.ndpi_search_vnc_tcp
    ndpi_search_vnc_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_vnc_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 109
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_dhcp_udp'):
        continue
    ndpi_search_dhcp_udp = _lib.ndpi_search_dhcp_udp
    ndpi_search_dhcp_udp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_dhcp_udp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 110
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_steam'):
        continue
    ndpi_search_steam = _lib.ndpi_search_steam
    ndpi_search_steam.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_steam.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 111
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_halflife2'):
        continue
    ndpi_search_halflife2 = _lib.ndpi_search_halflife2
    ndpi_search_halflife2.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_halflife2.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 112
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_xbox'):
        continue
    ndpi_search_xbox = _lib.ndpi_search_xbox
    ndpi_search_xbox.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_xbox.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 113
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_smb_tcp'):
        continue
    ndpi_search_smb_tcp = _lib.ndpi_search_smb_tcp
    ndpi_search_smb_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_smb_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 114
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_telnet_tcp'):
        continue
    ndpi_search_telnet_tcp = _lib.ndpi_search_telnet_tcp
    ndpi_search_telnet_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_telnet_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 115
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_ntp_udp'):
        continue
    ndpi_search_ntp_udp = _lib.ndpi_search_ntp_udp
    ndpi_search_ntp_udp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_ntp_udp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 116
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_nfs'):
        continue
    ndpi_search_nfs = _lib.ndpi_search_nfs
    ndpi_search_nfs.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_nfs.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 117
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_rtp'):
        continue
    ndpi_search_rtp = _lib.ndpi_search_rtp
    ndpi_search_rtp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_rtp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 118
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_ssdp'):
        continue
    ndpi_search_ssdp = _lib.ndpi_search_ssdp
    ndpi_search_ssdp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_ssdp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 119
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_worldofwarcraft'):
        continue
    ndpi_search_worldofwarcraft = _lib.ndpi_search_worldofwarcraft
    ndpi_search_worldofwarcraft.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_worldofwarcraft.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 120
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_postgres_tcp'):
        continue
    ndpi_search_postgres_tcp = _lib.ndpi_search_postgres_tcp
    ndpi_search_postgres_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_postgres_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 121
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_mysql_tcp'):
        continue
    ndpi_search_mysql_tcp = _lib.ndpi_search_mysql_tcp
    ndpi_search_mysql_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_mysql_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 122
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_bgp'):
        continue
    ndpi_search_bgp = _lib.ndpi_search_bgp
    ndpi_search_bgp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_bgp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 123
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_quake'):
        continue
    ndpi_search_quake = _lib.ndpi_search_quake
    ndpi_search_quake.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_quake.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 124
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_battlefield'):
        continue
    ndpi_search_battlefield = _lib.ndpi_search_battlefield
    ndpi_search_battlefield.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_battlefield.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 125
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_secondlife'):
        continue
    ndpi_search_secondlife = _lib.ndpi_search_secondlife
    ndpi_search_secondlife.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_secondlife.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 126
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_pcanywhere'):
        continue
    ndpi_search_pcanywhere = _lib.ndpi_search_pcanywhere
    ndpi_search_pcanywhere.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_pcanywhere.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 127
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_rdp'):
        continue
    ndpi_search_rdp = _lib.ndpi_search_rdp
    ndpi_search_rdp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_rdp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 128
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_snmp'):
        continue
    ndpi_search_snmp = _lib.ndpi_search_snmp
    ndpi_search_snmp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_snmp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 129
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_kontiki'):
        continue
    ndpi_search_kontiki = _lib.ndpi_search_kontiki
    ndpi_search_kontiki.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_kontiki.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 130
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_syslog'):
        continue
    ndpi_search_syslog = _lib.ndpi_search_syslog
    ndpi_search_syslog.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_syslog.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 131
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_netbios'):
        continue
    ndpi_search_netbios = _lib.ndpi_search_netbios
    ndpi_search_netbios.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_netbios.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 132
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_mdns'):
        continue
    ndpi_search_mdns = _lib.ndpi_search_mdns
    ndpi_search_mdns.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_mdns.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 133
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_ipp'):
        continue
    ndpi_search_ipp = _lib.ndpi_search_ipp
    ndpi_search_ipp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_ipp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 134
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_ldap'):
        continue
    ndpi_search_ldap = _lib.ndpi_search_ldap
    ndpi_search_ldap.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_ldap.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 135
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_warcraft3'):
        continue
    ndpi_search_warcraft3 = _lib.ndpi_search_warcraft3
    ndpi_search_warcraft3.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_warcraft3.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 136
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_kerberos'):
        continue
    ndpi_search_kerberos = _lib.ndpi_search_kerberos
    ndpi_search_kerberos.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_kerberos.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 137
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_xdmcp'):
        continue
    ndpi_search_xdmcp = _lib.ndpi_search_xdmcp
    ndpi_search_xdmcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_xdmcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 138
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_tftp'):
        continue
    ndpi_search_tftp = _lib.ndpi_search_tftp
    ndpi_search_tftp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_tftp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 139
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_mssql_tds'):
        continue
    ndpi_search_mssql_tds = _lib.ndpi_search_mssql_tds
    ndpi_search_mssql_tds.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_mssql_tds.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 140
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_pptp'):
        continue
    ndpi_search_pptp = _lib.ndpi_search_pptp
    ndpi_search_pptp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_pptp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 141
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_stealthnet'):
        continue
    ndpi_search_stealthnet = _lib.ndpi_search_stealthnet
    ndpi_search_stealthnet.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_stealthnet.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 142
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_dhcpv6_udp'):
        continue
    ndpi_search_dhcpv6_udp = _lib.ndpi_search_dhcpv6_udp
    ndpi_search_dhcpv6_udp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_dhcpv6_udp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 143
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_afp'):
        continue
    ndpi_search_afp = _lib.ndpi_search_afp
    ndpi_search_afp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_afp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 144
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_checkmk'):
        continue
    ndpi_search_checkmk = _lib.ndpi_search_checkmk
    ndpi_search_checkmk.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_checkmk.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 145
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_aimini'):
        continue
    ndpi_search_aimini = _lib.ndpi_search_aimini
    ndpi_search_aimini.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_aimini.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 146
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_florensia'):
        continue
    ndpi_search_florensia = _lib.ndpi_search_florensia
    ndpi_search_florensia.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_florensia.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 147
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_maplestory'):
        continue
    ndpi_search_maplestory = _lib.ndpi_search_maplestory
    ndpi_search_maplestory.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_maplestory.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 148
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_dofus'):
        continue
    ndpi_search_dofus = _lib.ndpi_search_dofus
    ndpi_search_dofus.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_dofus.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 149
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_world_of_kung_fu'):
        continue
    ndpi_search_world_of_kung_fu = _lib.ndpi_search_world_of_kung_fu
    ndpi_search_world_of_kung_fu.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_world_of_kung_fu.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 150
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_fiesta'):
        continue
    ndpi_search_fiesta = _lib.ndpi_search_fiesta
    ndpi_search_fiesta.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_fiesta.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 151
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_crossfire_tcp_udp'):
        continue
    ndpi_search_crossfire_tcp_udp = _lib.ndpi_search_crossfire_tcp_udp
    ndpi_search_crossfire_tcp_udp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_crossfire_tcp_udp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 152
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_guildwars_tcp'):
        continue
    ndpi_search_guildwars_tcp = _lib.ndpi_search_guildwars_tcp
    ndpi_search_guildwars_tcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_guildwars_tcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 153
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_armagetron_udp'):
        continue
    ndpi_search_armagetron_udp = _lib.ndpi_search_armagetron_udp
    ndpi_search_armagetron_udp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_armagetron_udp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 154
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_dropbox'):
        continue
    ndpi_search_dropbox = _lib.ndpi_search_dropbox
    ndpi_search_dropbox.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_dropbox.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 155
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_citrix'):
        continue
    ndpi_search_citrix = _lib.ndpi_search_citrix
    ndpi_search_citrix.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_citrix.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 156
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_dcerpc'):
        continue
    ndpi_search_dcerpc = _lib.ndpi_search_dcerpc
    ndpi_search_dcerpc.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_dcerpc.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 157
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_netflow'):
        continue
    ndpi_search_netflow = _lib.ndpi_search_netflow
    ndpi_search_netflow.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_netflow.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 158
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_sflow'):
        continue
    ndpi_search_sflow = _lib.ndpi_search_sflow
    ndpi_search_sflow.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_sflow.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 159
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_radius'):
        continue
    ndpi_search_radius = _lib.ndpi_search_radius
    ndpi_search_radius.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_radius.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 160
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_wsus'):
        continue
    ndpi_search_wsus = _lib.ndpi_search_wsus
    ndpi_search_wsus.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_wsus.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 161
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_teamview'):
        continue
    ndpi_search_teamview = _lib.ndpi_search_teamview
    ndpi_search_teamview.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_teamview.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 162
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_lotus_notes'):
        continue
    ndpi_search_lotus_notes = _lib.ndpi_search_lotus_notes
    ndpi_search_lotus_notes.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_lotus_notes.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 163
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_gtp'):
        continue
    ndpi_search_gtp = _lib.ndpi_search_gtp
    ndpi_search_gtp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_gtp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 164
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_spotify'):
        continue
    ndpi_search_spotify = _lib.ndpi_search_spotify
    ndpi_search_spotify.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_spotify.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 165
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_h323'):
        continue
    ndpi_search_h323 = _lib.ndpi_search_h323
    ndpi_search_h323.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_h323.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 166
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_openvpn'):
        continue
    ndpi_search_openvpn = _lib.ndpi_search_openvpn
    ndpi_search_openvpn.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_openvpn.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 167
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_noe'):
        continue
    ndpi_search_noe = _lib.ndpi_search_noe
    ndpi_search_noe.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_noe.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 168
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_ciscovpn'):
        continue
    ndpi_search_ciscovpn = _lib.ndpi_search_ciscovpn
    ndpi_search_ciscovpn.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_ciscovpn.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 169
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_viber'):
        continue
    ndpi_search_viber = _lib.ndpi_search_viber
    ndpi_search_viber.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_viber.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 170
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_teamspeak'):
        continue
    ndpi_search_teamspeak = _lib.ndpi_search_teamspeak
    ndpi_search_teamspeak.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_teamspeak.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 171
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_corba'):
        continue
    ndpi_search_corba = _lib.ndpi_search_corba
    ndpi_search_corba.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_corba.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 172
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_collectd'):
        continue
    ndpi_search_collectd = _lib.ndpi_search_collectd
    ndpi_search_collectd.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_collectd.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 173
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_oracle'):
        continue
    ndpi_search_oracle = _lib.ndpi_search_oracle
    ndpi_search_oracle.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_oracle.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 174
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_rsync'):
        continue
    ndpi_search_rsync = _lib.ndpi_search_rsync
    ndpi_search_rsync.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_rsync.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 175
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_rtcp'):
        continue
    ndpi_search_rtcp = _lib.ndpi_search_rtcp
    ndpi_search_rtcp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_rtcp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 176
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_skinny'):
        continue
    ndpi_search_skinny = _lib.ndpi_search_skinny
    ndpi_search_skinny.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_skinny.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 177
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_tor'):
        continue
    ndpi_search_tor = _lib.ndpi_search_tor
    ndpi_search_tor.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_tor.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 178
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_whois_das'):
        continue
    ndpi_search_whois_das = _lib.ndpi_search_whois_das
    ndpi_search_whois_das.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_whois_das.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 179
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_socks5'):
        continue
    ndpi_search_socks5 = _lib.ndpi_search_socks5
    ndpi_search_socks5.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_socks5.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 180
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_socks4'):
        continue
    ndpi_search_socks4 = _lib.ndpi_search_socks4
    ndpi_search_socks4.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_socks4.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 181
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_rtmp'):
        continue
    ndpi_search_rtmp = _lib.ndpi_search_rtmp
    ndpi_search_rtmp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_rtmp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 182
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_pando'):
        continue
    ndpi_search_pando = _lib.ndpi_search_pando
    ndpi_search_pando.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_pando.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 183
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_megaco'):
        continue
    ndpi_search_megaco = _lib.ndpi_search_megaco
    ndpi_search_megaco.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_megaco.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 184
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_redis'):
        continue
    ndpi_search_redis = _lib.ndpi_search_redis
    ndpi_search_redis.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_redis.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 185
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_zmq'):
        continue
    ndpi_search_zmq = _lib.ndpi_search_zmq
    ndpi_search_zmq.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_zmq.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 186
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_vhua'):
        continue
    ndpi_search_vhua = _lib.ndpi_search_vhua
    ndpi_search_vhua.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_vhua.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 187
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_telegram'):
        continue
    ndpi_search_telegram = _lib.ndpi_search_telegram
    ndpi_search_telegram.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_telegram.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 188
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_quic'):
        continue
    ndpi_search_quic = _lib.ndpi_search_quic
    ndpi_search_quic.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_quic.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 189
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_eaq'):
        continue
    ndpi_search_eaq = _lib.ndpi_search_eaq
    ndpi_search_eaq.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_eaq.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 190
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_kakaotalk_voice'):
        continue
    ndpi_search_kakaotalk_voice = _lib.ndpi_search_kakaotalk_voice
    ndpi_search_kakaotalk_voice.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_kakaotalk_voice.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 191
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_mpegts'):
        continue
    ndpi_search_mpegts = _lib.ndpi_search_mpegts
    ndpi_search_mpegts.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_mpegts.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 192
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_starcraft'):
        continue
    ndpi_search_starcraft = _lib.ndpi_search_starcraft
    ndpi_search_starcraft.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_starcraft.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 193
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_ubntac2'):
        continue
    ndpi_search_ubntac2 = _lib.ndpi_search_ubntac2
    ndpi_search_ubntac2.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_ubntac2.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 194
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_coap'):
        continue
    ndpi_search_coap = _lib.ndpi_search_coap
    ndpi_search_coap.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_coap.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 195
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_mqtt'):
        continue
    ndpi_search_mqtt = _lib.ndpi_search_mqtt
    ndpi_search_mqtt.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_mqtt.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 196
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_someip'):
        continue
    ndpi_search_someip = _lib.ndpi_search_someip
    ndpi_search_someip.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_someip.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 197
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_rx'):
        continue
    ndpi_search_rx = _lib.ndpi_search_rx
    ndpi_search_rx.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_rx.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 198
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_git'):
        continue
    ndpi_search_git = _lib.ndpi_search_git
    ndpi_search_git.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_git.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 199
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_drda'):
        continue
    ndpi_search_drda = _lib.ndpi_search_drda
    ndpi_search_drda.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_drda.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 200
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_bjnp'):
        continue
    ndpi_search_bjnp = _lib.ndpi_search_bjnp
    ndpi_search_bjnp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_bjnp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 201
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_smpp'):
        continue
    ndpi_search_smpp = _lib.ndpi_search_smpp
    ndpi_search_smpp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_smpp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 202
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_tinc'):
        continue
    ndpi_search_tinc = _lib.ndpi_search_tinc
    ndpi_search_tinc.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_tinc.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 203
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_fix'):
        continue
    ndpi_search_fix = _lib.ndpi_search_fix
    ndpi_search_fix.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_fix.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 204
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_csgo'):
        continue
    ndpi_search_csgo = _lib.ndpi_search_csgo
    ndpi_search_csgo.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_csgo.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 205
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_ajp'):
        continue
    ndpi_search_ajp = _lib.ndpi_search_ajp
    ndpi_search_ajp.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_ajp.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 206
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_memcached'):
        continue
    ndpi_search_memcached = _lib.ndpi_search_memcached
    ndpi_search_memcached.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_memcached.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 207
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_search_nest_log_sink'):
        continue
    ndpi_search_nest_log_sink = _lib.ndpi_search_nest_log_sink
    ndpi_search_nest_log_sink.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_search_nest_log_sink.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 209
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_diameter_dissector'):
        continue
    init_diameter_dissector = _lib.init_diameter_dissector
    init_diameter_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_diameter_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 210
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_afp_dissector'):
        continue
    init_afp_dissector = _lib.init_afp_dissector
    init_afp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_afp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 211
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_aimini_dissector'):
        continue
    init_aimini_dissector = _lib.init_aimini_dissector
    init_aimini_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_aimini_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 212
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_applejuice_dissector'):
        continue
    init_applejuice_dissector = _lib.init_applejuice_dissector
    init_applejuice_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_applejuice_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 213
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_armagetron_dissector'):
        continue
    init_armagetron_dissector = _lib.init_armagetron_dissector
    init_armagetron_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_armagetron_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 214
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_ayiya_dissector'):
        continue
    init_ayiya_dissector = _lib.init_ayiya_dissector
    init_ayiya_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_ayiya_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 215
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_amqp_dissector'):
        continue
    init_amqp_dissector = _lib.init_amqp_dissector
    init_amqp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_amqp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 216
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_battlefield_dissector'):
        continue
    init_battlefield_dissector = _lib.init_battlefield_dissector
    init_battlefield_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_battlefield_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 217
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_bgp_dissector'):
        continue
    init_bgp_dissector = _lib.init_bgp_dissector
    init_bgp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_bgp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 218
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_bittorrent_dissector'):
        continue
    init_bittorrent_dissector = _lib.init_bittorrent_dissector
    init_bittorrent_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_bittorrent_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 219
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_lisp_dissector'):
        continue
    init_lisp_dissector = _lib.init_lisp_dissector
    init_lisp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_lisp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 220
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_teredo_dissector'):
        continue
    init_teredo_dissector = _lib.init_teredo_dissector
    init_teredo_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_teredo_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 221
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_ciscovpn_dissector'):
        continue
    init_ciscovpn_dissector = _lib.init_ciscovpn_dissector
    init_ciscovpn_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_ciscovpn_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 222
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_citrix_dissector'):
        continue
    init_citrix_dissector = _lib.init_citrix_dissector
    init_citrix_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_citrix_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 223
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_corba_dissector'):
        continue
    init_corba_dissector = _lib.init_corba_dissector
    init_corba_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_corba_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 224
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_crossfire_dissector'):
        continue
    init_crossfire_dissector = _lib.init_crossfire_dissector
    init_crossfire_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_crossfire_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 225
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_dcerpc_dissector'):
        continue
    init_dcerpc_dissector = _lib.init_dcerpc_dissector
    init_dcerpc_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_dcerpc_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 226
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_dhcp_dissector'):
        continue
    init_dhcp_dissector = _lib.init_dhcp_dissector
    init_dhcp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_dhcp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 227
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_dhcpv6_dissector'):
        continue
    init_dhcpv6_dissector = _lib.init_dhcpv6_dissector
    init_dhcpv6_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_dhcpv6_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 228
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_directconnect_dissector'):
        continue
    init_directconnect_dissector = _lib.init_directconnect_dissector
    init_directconnect_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_directconnect_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 229
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_dns_dissector'):
        continue
    init_dns_dissector = _lib.init_dns_dissector
    init_dns_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_dns_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 230
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_dofus_dissector'):
        continue
    init_dofus_dissector = _lib.init_dofus_dissector
    init_dofus_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_dofus_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 231
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_directdownloadlink_dissector'):
        continue
    init_directdownloadlink_dissector = _lib.init_directdownloadlink_dissector
    init_directdownloadlink_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_directdownloadlink_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 232
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_dropbox_dissector'):
        continue
    init_dropbox_dissector = _lib.init_dropbox_dissector
    init_dropbox_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_dropbox_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 233
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_eaq_dissector'):
        continue
    init_eaq_dissector = _lib.init_eaq_dissector
    init_eaq_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_eaq_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 234
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_edonkey_dissector'):
        continue
    init_edonkey_dissector = _lib.init_edonkey_dissector
    init_edonkey_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_edonkey_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 235
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_fasttrack_dissector'):
        continue
    init_fasttrack_dissector = _lib.init_fasttrack_dissector
    init_fasttrack_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_fasttrack_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 236
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_fiesta_dissector'):
        continue
    init_fiesta_dissector = _lib.init_fiesta_dissector
    init_fiesta_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_fiesta_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 237
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_florensia_dissector'):
        continue
    init_florensia_dissector = _lib.init_florensia_dissector
    init_florensia_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_florensia_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 238
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_ftp_control_dissector'):
        continue
    init_ftp_control_dissector = _lib.init_ftp_control_dissector
    init_ftp_control_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_ftp_control_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 239
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_ftp_data_dissector'):
        continue
    init_ftp_data_dissector = _lib.init_ftp_data_dissector
    init_ftp_data_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_ftp_data_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 240
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_gnutella_dissector'):
        continue
    init_gnutella_dissector = _lib.init_gnutella_dissector
    init_gnutella_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_gnutella_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 241
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_gtp_dissector'):
        continue
    init_gtp_dissector = _lib.init_gtp_dissector
    init_gtp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_gtp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 242
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_guildwars_dissector'):
        continue
    init_guildwars_dissector = _lib.init_guildwars_dissector
    init_guildwars_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_guildwars_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 243
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_h323_dissector'):
        continue
    init_h323_dissector = _lib.init_h323_dissector
    init_h323_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_h323_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 244
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_halflife2_dissector'):
        continue
    init_halflife2_dissector = _lib.init_halflife2_dissector
    init_halflife2_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_halflife2_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 245
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_http_dissector'):
        continue
    init_http_dissector = _lib.init_http_dissector
    init_http_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_http_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 246
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_http_activesync_dissector'):
        continue
    init_http_activesync_dissector = _lib.init_http_activesync_dissector
    init_http_activesync_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_http_activesync_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 247
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_iax_dissector'):
        continue
    init_iax_dissector = _lib.init_iax_dissector
    init_iax_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_iax_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 248
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_icecast_dissector'):
        continue
    init_icecast_dissector = _lib.init_icecast_dissector
    init_icecast_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_icecast_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 249
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_ipp_dissector'):
        continue
    init_ipp_dissector = _lib.init_ipp_dissector
    init_ipp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_ipp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 250
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_irc_dissector'):
        continue
    init_irc_dissector = _lib.init_irc_dissector
    init_irc_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_irc_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 251
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_jabber_dissector'):
        continue
    init_jabber_dissector = _lib.init_jabber_dissector
    init_jabber_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_jabber_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 252
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_kakaotalk_voice_dissector'):
        continue
    init_kakaotalk_voice_dissector = _lib.init_kakaotalk_voice_dissector
    init_kakaotalk_voice_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_kakaotalk_voice_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 253
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_kerberos_dissector'):
        continue
    init_kerberos_dissector = _lib.init_kerberos_dissector
    init_kerberos_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_kerberos_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 254
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_kontiki_dissector'):
        continue
    init_kontiki_dissector = _lib.init_kontiki_dissector
    init_kontiki_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_kontiki_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 255
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_ldap_dissector'):
        continue
    init_ldap_dissector = _lib.init_ldap_dissector
    init_ldap_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_ldap_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 256
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_lotus_notes_dissector'):
        continue
    init_lotus_notes_dissector = _lib.init_lotus_notes_dissector
    init_lotus_notes_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_lotus_notes_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 257
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_mail_imap_dissector'):
        continue
    init_mail_imap_dissector = _lib.init_mail_imap_dissector
    init_mail_imap_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_mail_imap_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 258
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_mail_pop_dissector'):
        continue
    init_mail_pop_dissector = _lib.init_mail_pop_dissector
    init_mail_pop_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_mail_pop_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 259
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_mail_smtp_dissector'):
        continue
    init_mail_smtp_dissector = _lib.init_mail_smtp_dissector
    init_mail_smtp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_mail_smtp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 260
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_maplestory_dissector'):
        continue
    init_maplestory_dissector = _lib.init_maplestory_dissector
    init_maplestory_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_maplestory_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 261
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_mdns_dissector'):
        continue
    init_mdns_dissector = _lib.init_mdns_dissector
    init_mdns_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_mdns_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 262
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_megaco_dissector'):
        continue
    init_megaco_dissector = _lib.init_megaco_dissector
    init_megaco_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_megaco_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 263
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_mgpc_dissector'):
        continue
    init_mgpc_dissector = _lib.init_mgpc_dissector
    init_mgpc_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_mgpc_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 264
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_mining_dissector'):
        continue
    init_mining_dissector = _lib.init_mining_dissector
    init_mining_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_mining_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 265
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_mms_dissector'):
        continue
    init_mms_dissector = _lib.init_mms_dissector
    init_mms_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_mms_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 266
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_msn_dissector'):
        continue
    init_msn_dissector = _lib.init_msn_dissector
    init_msn_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_msn_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 267
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_mpegts_dissector'):
        continue
    init_mpegts_dissector = _lib.init_mpegts_dissector
    init_mpegts_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_mpegts_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 268
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_mssql_tds_dissector'):
        continue
    init_mssql_tds_dissector = _lib.init_mssql_tds_dissector
    init_mssql_tds_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_mssql_tds_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 269
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_mysql_dissector'):
        continue
    init_mysql_dissector = _lib.init_mysql_dissector
    init_mysql_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_mysql_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 270
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_netbios_dissector'):
        continue
    init_netbios_dissector = _lib.init_netbios_dissector
    init_netbios_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_netbios_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 271
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_netflow_dissector'):
        continue
    init_netflow_dissector = _lib.init_netflow_dissector
    init_netflow_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_netflow_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 272
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_nfs_dissector'):
        continue
    init_nfs_dissector = _lib.init_nfs_dissector
    init_nfs_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_nfs_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 273
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_noe_dissector'):
        continue
    init_noe_dissector = _lib.init_noe_dissector
    init_noe_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_noe_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 274
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_non_tcp_udp_dissector'):
        continue
    init_non_tcp_udp_dissector = _lib.init_non_tcp_udp_dissector
    init_non_tcp_udp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_non_tcp_udp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 275
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_ntp_dissector'):
        continue
    init_ntp_dissector = _lib.init_ntp_dissector
    init_ntp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_ntp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 276
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_openft_dissector'):
        continue
    init_openft_dissector = _lib.init_openft_dissector
    init_openft_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_openft_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 277
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_openvpn_dissector'):
        continue
    init_openvpn_dissector = _lib.init_openvpn_dissector
    init_openvpn_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_openvpn_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 278
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_oracle_dissector'):
        continue
    init_oracle_dissector = _lib.init_oracle_dissector
    init_oracle_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_oracle_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 279
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_oscar_dissector'):
        continue
    init_oscar_dissector = _lib.init_oscar_dissector
    init_oscar_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_oscar_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 280
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_pando_dissector'):
        continue
    init_pando_dissector = _lib.init_pando_dissector
    init_pando_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_pando_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 281
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_pcanywhere_dissector'):
        continue
    init_pcanywhere_dissector = _lib.init_pcanywhere_dissector
    init_pcanywhere_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_pcanywhere_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 282
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_postgres_dissector'):
        continue
    init_postgres_dissector = _lib.init_postgres_dissector
    init_postgres_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_postgres_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 283
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_pplive_dissector'):
        continue
    init_pplive_dissector = _lib.init_pplive_dissector
    init_pplive_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_pplive_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 284
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_ppstream_dissector'):
        continue
    init_ppstream_dissector = _lib.init_ppstream_dissector
    init_ppstream_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_ppstream_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 285
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_pptp_dissector'):
        continue
    init_pptp_dissector = _lib.init_pptp_dissector
    init_pptp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_pptp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 286
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_qq_dissector'):
        continue
    init_qq_dissector = _lib.init_qq_dissector
    init_qq_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_qq_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 287
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_quake_dissector'):
        continue
    init_quake_dissector = _lib.init_quake_dissector
    init_quake_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_quake_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 288
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_quic_dissector'):
        continue
    init_quic_dissector = _lib.init_quic_dissector
    init_quic_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_quic_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 289
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_radius_dissector'):
        continue
    init_radius_dissector = _lib.init_radius_dissector
    init_radius_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_radius_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 290
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_rdp_dissector'):
        continue
    init_rdp_dissector = _lib.init_rdp_dissector
    init_rdp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_rdp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 291
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_redis_dissector'):
        continue
    init_redis_dissector = _lib.init_redis_dissector
    init_redis_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_redis_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 292
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_rsync_dissector'):
        continue
    init_rsync_dissector = _lib.init_rsync_dissector
    init_rsync_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_rsync_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 293
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_rtcp_dissector'):
        continue
    init_rtcp_dissector = _lib.init_rtcp_dissector
    init_rtcp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_rtcp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 294
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_rtmp_dissector'):
        continue
    init_rtmp_dissector = _lib.init_rtmp_dissector
    init_rtmp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_rtmp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 295
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_rtp_dissector'):
        continue
    init_rtp_dissector = _lib.init_rtp_dissector
    init_rtp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_rtp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 296
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_rtsp_dissector'):
        continue
    init_rtsp_dissector = _lib.init_rtsp_dissector
    init_rtsp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_rtsp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 297
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_sflow_dissector'):
        continue
    init_sflow_dissector = _lib.init_sflow_dissector
    init_sflow_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_sflow_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 298
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_shoutcast_dissector'):
        continue
    init_shoutcast_dissector = _lib.init_shoutcast_dissector
    init_shoutcast_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_shoutcast_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 299
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_sip_dissector'):
        continue
    init_sip_dissector = _lib.init_sip_dissector
    init_sip_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_sip_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 300
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_hep_dissector'):
        continue
    init_hep_dissector = _lib.init_hep_dissector
    init_hep_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_hep_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 301
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_skinny_dissector'):
        continue
    init_skinny_dissector = _lib.init_skinny_dissector
    init_skinny_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_skinny_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 302
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_skype_dissector'):
        continue
    init_skype_dissector = _lib.init_skype_dissector
    init_skype_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_skype_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 303
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_smb_dissector'):
        continue
    init_smb_dissector = _lib.init_smb_dissector
    init_smb_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_smb_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 304
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_snmp_dissector'):
        continue
    init_snmp_dissector = _lib.init_snmp_dissector
    init_snmp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_snmp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 305
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_socrates_dissector'):
        continue
    init_socrates_dissector = _lib.init_socrates_dissector
    init_socrates_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_socrates_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 306
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_sopcast_dissector'):
        continue
    init_sopcast_dissector = _lib.init_sopcast_dissector
    init_sopcast_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_sopcast_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 307
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_soulseek_dissector'):
        continue
    init_soulseek_dissector = _lib.init_soulseek_dissector
    init_soulseek_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_soulseek_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 308
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_socks_dissector'):
        continue
    init_socks_dissector = _lib.init_socks_dissector
    init_socks_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_socks_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 309
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_spotify_dissector'):
        continue
    init_spotify_dissector = _lib.init_spotify_dissector
    init_spotify_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_spotify_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 310
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_ssh_dissector'):
        continue
    init_ssh_dissector = _lib.init_ssh_dissector
    init_ssh_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_ssh_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 311
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_ssl_dissector'):
        continue
    init_ssl_dissector = _lib.init_ssl_dissector
    init_ssl_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_ssl_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 312
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_starcraft_dissector'):
        continue
    init_starcraft_dissector = _lib.init_starcraft_dissector
    init_starcraft_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_starcraft_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 313
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_stealthnet_dissector'):
        continue
    init_stealthnet_dissector = _lib.init_stealthnet_dissector
    init_stealthnet_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_stealthnet_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 314
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_steam_dissector'):
        continue
    init_steam_dissector = _lib.init_steam_dissector
    init_steam_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_steam_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 315
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_stun_dissector'):
        continue
    init_stun_dissector = _lib.init_stun_dissector
    init_stun_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_stun_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 316
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_syslog_dissector'):
        continue
    init_syslog_dissector = _lib.init_syslog_dissector
    init_syslog_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_syslog_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 317
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_ssdp_dissector'):
        continue
    init_ssdp_dissector = _lib.init_ssdp_dissector
    init_ssdp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_ssdp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 318
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_teamspeak_dissector'):
        continue
    init_teamspeak_dissector = _lib.init_teamspeak_dissector
    init_teamspeak_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_teamspeak_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 319
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_teamviewer_dissector'):
        continue
    init_teamviewer_dissector = _lib.init_teamviewer_dissector
    init_teamviewer_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_teamviewer_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 320
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_telegram_dissector'):
        continue
    init_telegram_dissector = _lib.init_telegram_dissector
    init_telegram_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_telegram_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 321
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_telnet_dissector'):
        continue
    init_telnet_dissector = _lib.init_telnet_dissector
    init_telnet_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_telnet_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 322
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_tftp_dissector'):
        continue
    init_tftp_dissector = _lib.init_tftp_dissector
    init_tftp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_tftp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 323
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_thunder_dissector'):
        continue
    init_thunder_dissector = _lib.init_thunder_dissector
    init_thunder_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_thunder_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 324
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_tor_dissector'):
        continue
    init_tor_dissector = _lib.init_tor_dissector
    init_tor_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_tor_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 325
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_tvants_dissector'):
        continue
    init_tvants_dissector = _lib.init_tvants_dissector
    init_tvants_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_tvants_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 326
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_tvuplayer_dissector'):
        continue
    init_tvuplayer_dissector = _lib.init_tvuplayer_dissector
    init_tvuplayer_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_tvuplayer_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 327
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_usenet_dissector'):
        continue
    init_usenet_dissector = _lib.init_usenet_dissector
    init_usenet_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_usenet_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 328
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_upnp_dissector'):
        continue
    init_upnp_dissector = _lib.init_upnp_dissector
    init_upnp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_upnp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 329
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_veohtv_dissector'):
        continue
    init_veohtv_dissector = _lib.init_veohtv_dissector
    init_veohtv_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_veohtv_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 330
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_vhua_dissector'):
        continue
    init_vhua_dissector = _lib.init_vhua_dissector
    init_vhua_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_vhua_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 331
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_viber_dissector'):
        continue
    init_viber_dissector = _lib.init_viber_dissector
    init_viber_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_viber_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 332
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_vmware_dissector'):
        continue
    init_vmware_dissector = _lib.init_vmware_dissector
    init_vmware_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_vmware_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 333
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_vnc_dissector'):
        continue
    init_vnc_dissector = _lib.init_vnc_dissector
    init_vnc_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_vnc_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 334
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_warcraft3_dissector'):
        continue
    init_warcraft3_dissector = _lib.init_warcraft3_dissector
    init_warcraft3_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_warcraft3_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 335
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_whois_das_dissector'):
        continue
    init_whois_das_dissector = _lib.init_whois_das_dissector
    init_whois_das_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_whois_das_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 336
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_world_of_warcraft_dissector'):
        continue
    init_world_of_warcraft_dissector = _lib.init_world_of_warcraft_dissector
    init_world_of_warcraft_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_world_of_warcraft_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 337
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_world_of_kung_fu_dissector'):
        continue
    init_world_of_kung_fu_dissector = _lib.init_world_of_kung_fu_dissector
    init_world_of_kung_fu_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_world_of_kung_fu_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 338
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_xbox_dissector'):
        continue
    init_xbox_dissector = _lib.init_xbox_dissector
    init_xbox_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_xbox_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 339
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_xdmcp_dissector'):
        continue
    init_xdmcp_dissector = _lib.init_xdmcp_dissector
    init_xdmcp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_xdmcp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 340
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_yahoo_dissector'):
        continue
    init_yahoo_dissector = _lib.init_yahoo_dissector
    init_yahoo_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_yahoo_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_zattoo_dissector'):
        continue
    init_zattoo_dissector = _lib.init_zattoo_dissector
    init_zattoo_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_zattoo_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_zmq_dissector'):
        continue
    init_zmq_dissector = _lib.init_zmq_dissector
    init_zmq_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_zmq_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_stracraft_dissector'):
        continue
    init_stracraft_dissector = _lib.init_stracraft_dissector
    init_stracraft_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_stracraft_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 344
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_ubntac2_dissector'):
        continue
    init_ubntac2_dissector = _lib.init_ubntac2_dissector
    init_ubntac2_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_ubntac2_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 345
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_coap_dissector'):
        continue
    init_coap_dissector = _lib.init_coap_dissector
    init_coap_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_coap_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 346
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_mqtt_dissector'):
        continue
    init_mqtt_dissector = _lib.init_mqtt_dissector
    init_mqtt_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_mqtt_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 347
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_someip_dissector'):
        continue
    init_someip_dissector = _lib.init_someip_dissector
    init_someip_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_someip_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 348
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_rx_dissector'):
        continue
    init_rx_dissector = _lib.init_rx_dissector
    init_rx_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_rx_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 349
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_git_dissector'):
        continue
    init_git_dissector = _lib.init_git_dissector
    init_git_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_git_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 350
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_hangout_dissector'):
        continue
    init_hangout_dissector = _lib.init_hangout_dissector
    init_hangout_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_hangout_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 351
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_drda_dissector'):
        continue
    init_drda_dissector = _lib.init_drda_dissector
    init_drda_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_drda_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 352
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_bjnp_dissector'):
        continue
    init_bjnp_dissector = _lib.init_bjnp_dissector
    init_bjnp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_bjnp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 353
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_smpp_dissector'):
        continue
    init_smpp_dissector = _lib.init_smpp_dissector
    init_smpp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_smpp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 354
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_tinc_dissector'):
        continue
    init_tinc_dissector = _lib.init_tinc_dissector
    init_tinc_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_tinc_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 355
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_fix_dissector'):
        continue
    init_fix_dissector = _lib.init_fix_dissector
    init_fix_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_fix_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 356
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_nintendo_dissector'):
        continue
    init_nintendo_dissector = _lib.init_nintendo_dissector
    init_nintendo_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_nintendo_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 357
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_csgo_dissector'):
        continue
    init_csgo_dissector = _lib.init_csgo_dissector
    init_csgo_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_csgo_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 358
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_checkmk_dissector'):
        continue
    init_checkmk_dissector = _lib.init_checkmk_dissector
    init_checkmk_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_checkmk_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 359
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_apple_push_dissector'):
        continue
    init_apple_push_dissector = _lib.init_apple_push_dissector
    init_apple_push_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_apple_push_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 360
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_whatsapp_dissector'):
        continue
    init_whatsapp_dissector = _lib.init_whatsapp_dissector
    init_whatsapp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_whatsapp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 361
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_ajp_dissector'):
        continue
    init_ajp_dissector = _lib.init_ajp_dissector
    init_ajp_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_ajp_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 362
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_fbzero_dissector'):
        continue
    init_fbzero_dissector = _lib.init_fbzero_dissector
    init_fbzero_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_fbzero_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 363
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_memcached_dissector'):
        continue
    init_memcached_dissector = _lib.init_memcached_dissector
    init_memcached_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_memcached_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 364
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_nest_log_sink_dissector'):
        continue
    init_nest_log_sink_dissector = _lib.init_nest_log_sink_dissector
    init_nest_log_sink_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_nest_log_sink_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 365
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_ookla_dissector'):
        continue
    init_ookla_dissector = _lib.init_ookla_dissector
    init_ookla_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_ookla_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocols.h: 366
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'init_modbus_dissector'):
        continue
    init_modbus_dissector = _lib.init_modbus_dissector
    init_modbus_dissector.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(u_int32_t), POINTER(ndpi_protocol_bitmask_struct_t)]
    init_modbus_dissector.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 38
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_tdelete'):
        continue
    ndpi_tdelete = _lib.ndpi_tdelete
    ndpi_tdelete.argtypes = [POINTER(None), POINTER(POINTER(None)), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None))]
    ndpi_tdelete.restype = POINTER(None)
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 40
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_tfind'):
        continue
    ndpi_tfind = _lib.ndpi_tfind
    ndpi_tfind.argtypes = [POINTER(None), POINTER(None), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None))]
    ndpi_tfind.restype = POINTER(None)
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 41
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_tsearch'):
        continue
    ndpi_tsearch = _lib.ndpi_tsearch
    ndpi_tsearch.argtypes = [POINTER(None), POINTER(POINTER(None)), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None))]
    ndpi_tsearch.restype = POINTER(None)
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 42
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_twalk'):
        continue
    ndpi_twalk = _lib.ndpi_twalk
    ndpi_twalk.argtypes = [POINTER(None), CFUNCTYPE(UNCHECKED(None), POINTER(None), ndpi_VISIT, c_int, POINTER(None)), POINTER(None)]
    ndpi_twalk.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 43
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_tdestroy'):
        continue
    ndpi_tdestroy = _lib.ndpi_tdestroy
    ndpi_tdestroy.argtypes = [POINTER(None), CFUNCTYPE(UNCHECKED(None), POINTER(None))]
    ndpi_tdestroy.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 45
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'NDPI_BITMASK_COMPARE'):
        continue
    NDPI_BITMASK_COMPARE = _lib.NDPI_BITMASK_COMPARE
    NDPI_BITMASK_COMPARE.argtypes = [ndpi_protocol_bitmask_struct_t, ndpi_protocol_bitmask_struct_t]
    NDPI_BITMASK_COMPARE.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 46
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'NDPI_BITMASK_IS_EMPTY'):
        continue
    NDPI_BITMASK_IS_EMPTY = _lib.NDPI_BITMASK_IS_EMPTY
    NDPI_BITMASK_IS_EMPTY.argtypes = [ndpi_protocol_bitmask_struct_t]
    NDPI_BITMASK_IS_EMPTY.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 47
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'NDPI_DUMP_BITMASK'):
        continue
    NDPI_DUMP_BITMASK = _lib.NDPI_DUMP_BITMASK
    NDPI_DUMP_BITMASK.argtypes = [ndpi_protocol_bitmask_struct_t]
    NDPI_DUMP_BITMASK.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 49
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_net_match'):
        continue
    ndpi_net_match = _lib.ndpi_net_match
    ndpi_net_match.argtypes = [u_int32_t, u_int32_t, u_int32_t]
    ndpi_net_match.restype = u_int8_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 53
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_ips_match'):
        continue
    ndpi_ips_match = _lib.ndpi_ips_match
    ndpi_ips_match.argtypes = [u_int32_t, u_int32_t, u_int32_t, u_int32_t]
    ndpi_ips_match.restype = u_int8_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 56
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ntohs_ndpi_bytestream_to_number'):
        continue
    ntohs_ndpi_bytestream_to_number = _lib.ntohs_ndpi_bytestream_to_number
    ntohs_ndpi_bytestream_to_number.argtypes = [POINTER(u_int8_t), u_int16_t, POINTER(u_int16_t)]
    ntohs_ndpi_bytestream_to_number.restype = u_int16_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 60
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_bytestream_to_number'):
        continue
    ndpi_bytestream_to_number = _lib.ndpi_bytestream_to_number
    ndpi_bytestream_to_number.argtypes = [POINTER(u_int8_t), u_int16_t, POINTER(u_int16_t)]
    ndpi_bytestream_to_number.restype = u_int32_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 62
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_bytestream_to_number64'):
        continue
    ndpi_bytestream_to_number64 = _lib.ndpi_bytestream_to_number64
    ndpi_bytestream_to_number64.argtypes = [POINTER(u_int8_t), u_int16_t, POINTER(u_int16_t)]
    ndpi_bytestream_to_number64.restype = u_int64_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 64
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_bytestream_dec_or_hex_to_number'):
        continue
    ndpi_bytestream_dec_or_hex_to_number = _lib.ndpi_bytestream_dec_or_hex_to_number
    ndpi_bytestream_dec_or_hex_to_number.argtypes = [POINTER(u_int8_t), u_int16_t, POINTER(u_int16_t)]
    ndpi_bytestream_dec_or_hex_to_number.restype = u_int32_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 67
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_bytestream_dec_or_hex_to_number64'):
        continue
    ndpi_bytestream_dec_or_hex_to_number64 = _lib.ndpi_bytestream_dec_or_hex_to_number64
    ndpi_bytestream_dec_or_hex_to_number64.argtypes = [POINTER(u_int8_t), u_int16_t, POINTER(u_int16_t)]
    ndpi_bytestream_dec_or_hex_to_number64.restype = u_int64_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 70
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_bytestream_to_ipv4'):
        continue
    ndpi_bytestream_to_ipv4 = _lib.ndpi_bytestream_to_ipv4
    ndpi_bytestream_to_ipv4.argtypes = [POINTER(u_int8_t), u_int16_t, POINTER(u_int16_t)]
    ndpi_bytestream_to_ipv4.restype = u_int32_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 73
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_set_detected_protocol'):
        continue
    ndpi_set_detected_protocol = _lib.ndpi_set_detected_protocol
    ndpi_set_detected_protocol.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct), u_int16_t, u_int16_t]
    ndpi_set_detected_protocol.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 78
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_parse_packet_line_info'):
        continue
    ndpi_parse_packet_line_info = _lib.ndpi_parse_packet_line_info
    ndpi_parse_packet_line_info.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_parse_packet_line_info.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 80
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_parse_packet_line_info_any'):
        continue
    ndpi_parse_packet_line_info_any = _lib.ndpi_parse_packet_line_info_any
    ndpi_parse_packet_line_info_any.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_parse_packet_line_info_any.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 83
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_check_for_email_address'):
        continue
    ndpi_check_for_email_address = _lib.ndpi_check_for_email_address
    ndpi_check_for_email_address.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct), u_int16_t]
    ndpi_check_for_email_address.restype = u_int16_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 86
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_int_change_packet_protocol'):
        continue
    ndpi_int_change_packet_protocol = _lib.ndpi_int_change_packet_protocol
    ndpi_int_change_packet_protocol.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct), u_int16_t, u_int16_t]
    ndpi_int_change_packet_protocol.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 90
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_int_change_protocol'):
        continue
    ndpi_int_change_protocol = _lib.ndpi_int_change_protocol
    ndpi_int_change_protocol.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct), u_int16_t, u_int16_t]
    ndpi_int_change_protocol.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 94
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_int_change_category'):
        continue
    ndpi_int_change_category = _lib.ndpi_int_change_category
    ndpi_int_change_category.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct), ndpi_protocol_category_t]
    ndpi_int_change_category.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 98
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_set_proto_defaults'):
        continue
    ndpi_set_proto_defaults = _lib.ndpi_set_proto_defaults
    ndpi_set_proto_defaults.argtypes = [POINTER(struct_ndpi_detection_module_struct), ndpi_protocol_breed_t, u_int16_t, u_int8_t, u_int16_t * 2, u_int16_t * 2, String, ndpi_protocol_category_t, POINTER(ndpi_port_range), POINTER(ndpi_port_range)]
    ndpi_set_proto_defaults.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 107
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_int_reset_packet_protocol'):
        continue
    ndpi_int_reset_packet_protocol = _lib.ndpi_int_reset_packet_protocol
    ndpi_int_reset_packet_protocol.argtypes = [POINTER(struct_ndpi_packet_struct)]
    ndpi_int_reset_packet_protocol.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 108
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_int_reset_protocol'):
        continue
    ndpi_int_reset_protocol = _lib.ndpi_int_reset_protocol
    ndpi_int_reset_protocol.argtypes = [POINTER(struct_ndpi_flow_struct)]
    ndpi_int_reset_protocol.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 110
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_packet_src_ip_eql'):
        continue
    ndpi_packet_src_ip_eql = _lib.ndpi_packet_src_ip_eql
    ndpi_packet_src_ip_eql.argtypes = [POINTER(struct_ndpi_packet_struct), POINTER(ndpi_ip_addr_t)]
    ndpi_packet_src_ip_eql.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 111
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_packet_dst_ip_eql'):
        continue
    ndpi_packet_dst_ip_eql = _lib.ndpi_packet_dst_ip_eql
    ndpi_packet_dst_ip_eql.argtypes = [POINTER(struct_ndpi_packet_struct), POINTER(ndpi_ip_addr_t)]
    ndpi_packet_dst_ip_eql.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 112
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_packet_src_ip_get'):
        continue
    ndpi_packet_src_ip_get = _lib.ndpi_packet_src_ip_get
    ndpi_packet_src_ip_get.argtypes = [POINTER(struct_ndpi_packet_struct), POINTER(ndpi_ip_addr_t)]
    ndpi_packet_src_ip_get.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 113
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_packet_dst_ip_get'):
        continue
    ndpi_packet_dst_ip_get = _lib.ndpi_packet_dst_ip_get
    ndpi_packet_dst_ip_get.argtypes = [POINTER(struct_ndpi_packet_struct), POINTER(ndpi_ip_addr_t)]
    ndpi_packet_dst_ip_get.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 115
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_ip_string'):
        continue
    ndpi_get_ip_string = _lib.ndpi_get_ip_string
    ndpi_get_ip_string.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(ndpi_ip_addr_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        ndpi_get_ip_string.restype = ReturnString
    else:
        ndpi_get_ip_string.restype = String
        ndpi_get_ip_string.errcheck = ReturnString
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 117
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_packet_src_ip_string'):
        continue
    ndpi_get_packet_src_ip_string = _lib.ndpi_get_packet_src_ip_string
    ndpi_get_packet_src_ip_string.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_packet_struct)]
    if sizeof(c_int) == sizeof(c_void_p):
        ndpi_get_packet_src_ip_string.restype = ReturnString
    else:
        ndpi_get_packet_src_ip_string.restype = String
        ndpi_get_packet_src_ip_string.errcheck = ReturnString
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 119
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_proto_by_id'):
        continue
    ndpi_get_proto_by_id = _lib.ndpi_get_proto_by_id
    ndpi_get_proto_by_id.argtypes = [POINTER(struct_ndpi_detection_module_struct), u_int]
    if sizeof(c_int) == sizeof(c_void_p):
        ndpi_get_proto_by_id.restype = ReturnString
    else:
        ndpi_get_proto_by_id.restype = String
        ndpi_get_proto_by_id.errcheck = ReturnString
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 120
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_proto_by_name'):
        continue
    ndpi_get_proto_by_name = _lib.ndpi_get_proto_by_name
    ndpi_get_proto_by_name.argtypes = [POINTER(struct_ndpi_detection_module_struct), String]
    ndpi_get_proto_by_name.restype = u_int16_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 122
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_guess_protocol_id'):
        continue
    ndpi_guess_protocol_id = _lib.ndpi_guess_protocol_id
    ndpi_guess_protocol_id.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct), u_int8_t, u_int16_t, u_int16_t, POINTER(u_int8_t)]
    ndpi_guess_protocol_id.restype = u_int16_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 127
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_is_proto'):
        continue
    ndpi_is_proto = _lib.ndpi_is_proto
    ndpi_is_proto.argtypes = [ndpi_protocol, u_int16_t]
    ndpi_is_proto.restype = u_int8_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 129
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_lower_proto'):
        continue
    ndpi_get_lower_proto = _lib.ndpi_get_lower_proto
    ndpi_get_lower_proto.argtypes = [ndpi_protocol]
    ndpi_get_lower_proto.restype = u_int16_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 130
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_protocol_id_master_proto'):
        continue
    ndpi_get_protocol_id_master_proto = _lib.ndpi_get_protocol_id_master_proto
    ndpi_get_protocol_id_master_proto.argtypes = [POINTER(struct_ndpi_detection_module_struct), u_int16_t, POINTER(POINTER(u_int16_t)), POINTER(POINTER(u_int16_t))]
    ndpi_get_protocol_id_master_proto.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 135
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_netbios_name_interpret'):
        continue
    ndpi_netbios_name_interpret = _lib.ndpi_netbios_name_interpret
    ndpi_netbios_name_interpret.argtypes = [String, String, u_int]
    ndpi_netbios_name_interpret.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 146
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_match_prefix'):
        continue
    ndpi_match_prefix = _lib.ndpi_match_prefix
    ndpi_match_prefix.argtypes = [POINTER(u_int8_t), c_size_t, String, c_size_t]
    ndpi_match_prefix.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 61
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_check_punycode_string'):
        continue
    ndpi_check_punycode_string = _lib.ndpi_check_punycode_string
    ndpi_check_punycode_string.argtypes = [String, c_int]
    ndpi_check_punycode_string.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 70
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_detection_get_sizeof_ndpi_flow_struct'):
        continue
    ndpi_detection_get_sizeof_ndpi_flow_struct = _lib.ndpi_detection_get_sizeof_ndpi_flow_struct
    ndpi_detection_get_sizeof_ndpi_flow_struct.argtypes = []
    ndpi_detection_get_sizeof_ndpi_flow_struct.restype = u_int32_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 79
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_detection_get_sizeof_ndpi_id_struct'):
        continue
    ndpi_detection_get_sizeof_ndpi_id_struct = _lib.ndpi_detection_get_sizeof_ndpi_id_struct
    ndpi_detection_get_sizeof_ndpi_id_struct.argtypes = []
    ndpi_detection_get_sizeof_ndpi_id_struct.restype = u_int32_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 84
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_malloc'):
        continue
    ndpi_malloc = _lib.ndpi_malloc
    ndpi_malloc.argtypes = [c_size_t]
    ndpi_malloc.restype = POINTER(None)
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 85
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_calloc'):
        continue
    ndpi_calloc = _lib.ndpi_calloc
    ndpi_calloc.argtypes = [c_ulong, c_size_t]
    ndpi_calloc.restype = POINTER(None)
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 86
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_realloc'):
        continue
    ndpi_realloc = _lib.ndpi_realloc
    ndpi_realloc.argtypes = [POINTER(None), c_size_t, c_size_t]
    ndpi_realloc.restype = POINTER(None)
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 87
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_strdup'):
        continue
    ndpi_strdup = _lib.ndpi_strdup
    ndpi_strdup.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        ndpi_strdup.restype = ReturnString
    else:
        ndpi_strdup.restype = String
        ndpi_strdup.errcheck = ReturnString
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 88
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_free'):
        continue
    ndpi_free = _lib.ndpi_free
    ndpi_free.argtypes = [POINTER(None)]
    ndpi_free.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 89
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_flow_malloc'):
        continue
    ndpi_flow_malloc = _lib.ndpi_flow_malloc
    ndpi_flow_malloc.argtypes = [c_size_t]
    ndpi_flow_malloc.restype = POINTER(None)
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 90
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_flow_free'):
        continue
    ndpi_flow_free = _lib.ndpi_flow_free
    ndpi_flow_free.argtypes = [POINTER(None)]
    ndpi_flow_free.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 103
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_strnstr'):
        continue
    ndpi_strnstr = _lib.ndpi_strnstr
    ndpi_strnstr.argtypes = [String, String, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        ndpi_strnstr.restype = ReturnString
    else:
        ndpi_strnstr.restype = String
        ndpi_strnstr.errcheck = ReturnString
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 115
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_strncasestr'):
        continue
    ndpi_strncasestr = _lib.ndpi_strncasestr
    ndpi_strncasestr.argtypes = [String, String, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        ndpi_strncasestr.restype = ReturnString
    else:
        ndpi_strncasestr.restype = String
        ndpi_strncasestr.errcheck = ReturnString
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 126
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_network_ptree_match'):
        continue
    ndpi_network_ptree_match = _lib.ndpi_network_ptree_match
    ndpi_network_ptree_match.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_in_addr)]
    ndpi_network_ptree_match.restype = u_int16_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 136
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_init_protocol_match'):
        continue
    ndpi_init_protocol_match = _lib.ndpi_init_protocol_match
    ndpi_init_protocol_match.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(ndpi_protocol_match)]
    ndpi_init_protocol_match.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 145
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_init_detection_module'):
        continue
    ndpi_init_detection_module = _lib.ndpi_init_detection_module
    ndpi_init_detection_module.argtypes = []
    ndpi_init_detection_module.restype = POINTER(struct_ndpi_detection_module_struct)
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 153
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_free_flow'):
        continue
    ndpi_free_flow = _lib.ndpi_free_flow
    ndpi_free_flow.argtypes = [POINTER(struct_ndpi_flow_struct)]
    ndpi_free_flow.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 164
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_enable_cache'):
        continue
    ndpi_enable_cache = _lib.ndpi_enable_cache
    ndpi_enable_cache.argtypes = [POINTER(struct_ndpi_detection_module_struct), String, u_int]
    ndpi_enable_cache.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 173
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_exit_detection_module'):
        continue
    ndpi_exit_detection_module = _lib.ndpi_exit_detection_module
    ndpi_exit_detection_module.argtypes = [POINTER(struct_ndpi_detection_module_struct)]
    ndpi_exit_detection_module.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 189
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_set_bitmask_protocol_detection'):
        continue
    ndpi_set_bitmask_protocol_detection = _lib.ndpi_set_bitmask_protocol_detection
    ndpi_set_bitmask_protocol_detection.argtypes = [String, POINTER(struct_ndpi_detection_module_struct), POINTER(ndpi_protocol_bitmask_struct_t), u_int32_t, u_int16_t, CFUNCTYPE(UNCHECKED(None), POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)), u_int32_t, u_int8_t, u_int8_t]
    ndpi_set_bitmask_protocol_detection.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 207
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_set_protocol_detection_bitmask2'):
        continue
    ndpi_set_protocol_detection_bitmask2 = _lib.ndpi_set_protocol_detection_bitmask2
    ndpi_set_protocol_detection_bitmask2.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(ndpi_protocol_bitmask_struct_t)]
    ndpi_set_protocol_detection_bitmask2.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 219
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_partial_detection'):
        continue
    ndpi_get_partial_detection = _lib.ndpi_get_partial_detection
    ndpi_get_partial_detection.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_get_partial_detection.restype = ndpi_protocol
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 231
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_detection_giveup'):
        continue
    ndpi_detection_giveup = _lib.ndpi_detection_giveup
    ndpi_detection_giveup.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct), u_int8_t]
    ndpi_detection_giveup.restype = ndpi_protocol
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 250
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_process_extra_packet'):
        continue
    ndpi_process_extra_packet = _lib.ndpi_process_extra_packet
    ndpi_process_extra_packet.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct), POINTER(c_ubyte), c_ushort, u_int64_t, POINTER(struct_ndpi_id_struct), POINTER(struct_ndpi_id_struct)]
    ndpi_process_extra_packet.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 272
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_detection_process_packet'):
        continue
    ndpi_detection_process_packet = _lib.ndpi_detection_process_packet
    ndpi_detection_process_packet.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct), POINTER(c_ubyte), c_ushort, u_int64_t, POINTER(struct_ndpi_id_struct), POINTER(struct_ndpi_id_struct)]
    ndpi_detection_process_packet.restype = ndpi_protocol
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 288
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_flow_masterprotocol'):
        continue
    ndpi_get_flow_masterprotocol = _lib.ndpi_get_flow_masterprotocol
    ndpi_get_flow_masterprotocol.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_get_flow_masterprotocol.restype = u_int16_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 302
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_check_flow_func'):
        continue
    ndpi_check_flow_func = _lib.ndpi_check_flow_func
    ndpi_check_flow_func.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct), POINTER(u_int32_t)]
    ndpi_check_flow_func.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 319
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_detection_get_l4'):
        continue
    ndpi_detection_get_l4 = _lib.ndpi_detection_get_l4
    ndpi_detection_get_l4.argtypes = [POINTER(u_int8_t), u_int16_t, POINTER(POINTER(u_int8_t)), POINTER(u_int16_t), POINTER(u_int8_t), u_int32_t]
    ndpi_detection_get_l4.restype = u_int8_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 333
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_find_port_based_protocol'):
        continue
    ndpi_find_port_based_protocol = _lib.ndpi_find_port_based_protocol
    ndpi_find_port_based_protocol.argtypes = [POINTER(struct_ndpi_detection_module_struct), u_int32_t, u_int16_t, u_int32_t, u_int16_t]
    ndpi_find_port_based_protocol.restype = ndpi_protocol
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 351
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_guess_undetected_protocol'):
        continue
    ndpi_guess_undetected_protocol = _lib.ndpi_guess_undetected_protocol
    ndpi_guess_undetected_protocol.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct), u_int8_t, u_int32_t, u_int16_t, u_int32_t, u_int16_t]
    ndpi_guess_undetected_protocol.restype = ndpi_protocol
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 369
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_match_string_subprotocol'):
        continue
    ndpi_match_string_subprotocol = _lib.ndpi_match_string_subprotocol
    ndpi_match_string_subprotocol.argtypes = [POINTER(struct_ndpi_detection_module_struct), String, u_int, POINTER(ndpi_protocol_match_result), u_int8_t]
    ndpi_match_string_subprotocol.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 386
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_match_host_subprotocol'):
        continue
    ndpi_match_host_subprotocol = _lib.ndpi_match_host_subprotocol
    ndpi_match_host_subprotocol.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct), String, u_int, POINTER(ndpi_protocol_match_result), u_int16_t]
    ndpi_match_host_subprotocol.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 406
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_match_content_subprotocol'):
        continue
    ndpi_match_content_subprotocol = _lib.ndpi_match_content_subprotocol
    ndpi_match_content_subprotocol.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct), String, u_int, POINTER(ndpi_protocol_match_result), u_int16_t]
    ndpi_match_content_subprotocol.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 420
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_exclude_protocol'):
        continue
    ndpi_exclude_protocol = _lib.ndpi_exclude_protocol
    ndpi_exclude_protocol.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct), u_int16_t, String, String, c_int]
    ndpi_exclude_protocol.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 433
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_match_bigram'):
        continue
    ndpi_match_bigram = _lib.ndpi_match_bigram
    ndpi_match_bigram.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(ndpi_automa), String]
    ndpi_match_bigram.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 447
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_protocol2name'):
        continue
    ndpi_protocol2name = _lib.ndpi_protocol2name
    ndpi_protocol2name.argtypes = [POINTER(struct_ndpi_detection_module_struct), ndpi_protocol, String, u_int]
    if sizeof(c_int) == sizeof(c_void_p):
        ndpi_protocol2name.restype = ReturnString
    else:
        ndpi_protocol2name.restype = String
        ndpi_protocol2name.errcheck = ReturnString
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 461
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_protocol2id'):
        continue
    ndpi_protocol2id = _lib.ndpi_protocol2id
    ndpi_protocol2id.argtypes = [POINTER(struct_ndpi_detection_module_struct), ndpi_protocol, String, u_int]
    if sizeof(c_int) == sizeof(c_void_p):
        ndpi_protocol2id.restype = ReturnString
    else:
        ndpi_protocol2id.restype = String
        ndpi_protocol2id.errcheck = ReturnString
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 471
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_is_custom_category'):
        continue
    ndpi_is_custom_category = _lib.ndpi_is_custom_category
    ndpi_is_custom_category.argtypes = [ndpi_protocol_category_t]
    ndpi_is_custom_category.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 481
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_set_proto_breed'):
        continue
    ndpi_set_proto_breed = _lib.ndpi_set_proto_breed
    ndpi_set_proto_breed.argtypes = [POINTER(struct_ndpi_detection_module_struct), u_int16_t, ndpi_protocol_breed_t]
    ndpi_set_proto_breed.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 492
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_set_proto_category'):
        continue
    ndpi_set_proto_category = _lib.ndpi_set_proto_category
    ndpi_set_proto_category.argtypes = [POINTER(struct_ndpi_detection_module_struct), u_int16_t, ndpi_protocol_category_t]
    ndpi_set_proto_category.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 504
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_is_subprotocol_informative'):
        continue
    ndpi_is_subprotocol_informative = _lib.ndpi_is_subprotocol_informative
    ndpi_is_subprotocol_informative.argtypes = [POINTER(struct_ndpi_detection_module_struct), u_int16_t]
    ndpi_is_subprotocol_informative.restype = u_int8_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 515
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_category_get_name'):
        continue
    ndpi_category_get_name = _lib.ndpi_category_get_name
    ndpi_category_get_name.argtypes = [POINTER(struct_ndpi_detection_module_struct), ndpi_protocol_category_t]
    if sizeof(c_int) == sizeof(c_void_p):
        ndpi_category_get_name.restype = ReturnString
    else:
        ndpi_category_get_name.restype = String
        ndpi_category_get_name.errcheck = ReturnString
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 526
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_category_set_name'):
        continue
    ndpi_category_set_name = _lib.ndpi_category_set_name
    ndpi_category_set_name.argtypes = [POINTER(struct_ndpi_detection_module_struct), ndpi_protocol_category_t, String]
    ndpi_category_set_name.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 536
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_proto_category'):
        continue
    ndpi_get_proto_category = _lib.ndpi_get_proto_category
    ndpi_get_proto_category.argtypes = [POINTER(struct_ndpi_detection_module_struct), ndpi_protocol]
    ndpi_get_proto_category.restype = ndpi_protocol_category_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 547
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_proto_name'):
        continue
    ndpi_get_proto_name = _lib.ndpi_get_proto_name
    ndpi_get_proto_name.argtypes = [POINTER(struct_ndpi_detection_module_struct), u_int16_t]
    if sizeof(c_int) == sizeof(c_void_p):
        ndpi_get_proto_name.restype = ReturnString
    else:
        ndpi_get_proto_name.restype = String
        ndpi_get_proto_name.errcheck = ReturnString
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 558
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_proto_breed'):
        continue
    ndpi_get_proto_breed = _lib.ndpi_get_proto_breed
    ndpi_get_proto_breed.argtypes = [POINTER(struct_ndpi_detection_module_struct), u_int16_t]
    ndpi_get_proto_breed.restype = ndpi_protocol_breed_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 569
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_proto_breed_name'):
        continue
    ndpi_get_proto_breed_name = _lib.ndpi_get_proto_breed_name
    ndpi_get_proto_breed_name.argtypes = [POINTER(struct_ndpi_detection_module_struct), ndpi_protocol_breed_t]
    if sizeof(c_int) == sizeof(c_void_p):
        ndpi_get_proto_breed_name.restype = ReturnString
    else:
        ndpi_get_proto_breed_name.restype = String
        ndpi_get_proto_breed_name.errcheck = ReturnString
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 580
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_protocol_id'):
        continue
    ndpi_get_protocol_id = _lib.ndpi_get_protocol_id
    ndpi_get_protocol_id.argtypes = [POINTER(struct_ndpi_detection_module_struct), String]
    ndpi_get_protocol_id.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 590
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_category_id'):
        continue
    ndpi_get_category_id = _lib.ndpi_get_category_id
    ndpi_get_category_id.argtypes = [POINTER(struct_ndpi_detection_module_struct), String]
    ndpi_get_category_id.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 597
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_dump_protocols'):
        continue
    ndpi_dump_protocols = _lib.ndpi_dump_protocols
    ndpi_dump_protocols.argtypes = [POINTER(struct_ndpi_detection_module_struct)]
    ndpi_dump_protocols.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 614
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_load_protocols_file'):
        continue
    ndpi_load_protocols_file = _lib.ndpi_load_protocols_file
    ndpi_load_protocols_file.argtypes = [POINTER(struct_ndpi_detection_module_struct), String]
    ndpi_load_protocols_file.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 624
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_num_supported_protocols'):
        continue
    ndpi_get_num_supported_protocols = _lib.ndpi_get_num_supported_protocols
    ndpi_get_num_supported_protocols.argtypes = [POINTER(struct_ndpi_detection_module_struct)]
    ndpi_get_num_supported_protocols.restype = u_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 632
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_revision'):
        continue
    ndpi_revision = _lib.ndpi_revision
    ndpi_revision.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        ndpi_revision.restype = ReturnString
    else:
        ndpi_revision.restype = String
        ndpi_revision.errcheck = ReturnString
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 641
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_set_automa'):
        continue
    ndpi_set_automa = _lib.ndpi_set_automa
    ndpi_set_automa.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(None)]
    ndpi_set_automa.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 653
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_http_method'):
        continue
    ndpi_get_http_method = _lib.ndpi_get_http_method
    ndpi_get_http_method.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_get_http_method.restype = ndpi_http_method
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 664
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_http_url'):
        continue
    ndpi_get_http_url = _lib.ndpi_get_http_url
    ndpi_get_http_url.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    if sizeof(c_int) == sizeof(c_void_p):
        ndpi_get_http_url.restype = ReturnString
    else:
        ndpi_get_http_url.restype = String
        ndpi_get_http_url.errcheck = ReturnString
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 675
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_http_content_type'):
        continue
    ndpi_get_http_content_type = _lib.ndpi_get_http_content_type
    ndpi_get_http_content_type.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    if sizeof(c_int) == sizeof(c_void_p):
        ndpi_get_http_content_type.restype = ReturnString
    else:
        ndpi_get_http_content_type.restype = String
        ndpi_get_http_content_type.errcheck = ReturnString
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 689
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_is_ssl_tor'):
        continue
    ndpi_is_ssl_tor = _lib.ndpi_is_ssl_tor
    ndpi_is_ssl_tor.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct), String]
    ndpi_is_ssl_tor.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 699
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_init_automa'):
        continue
    ndpi_init_automa = _lib.ndpi_init_automa
    ndpi_init_automa.argtypes = []
    ndpi_init_automa.restype = POINTER(None)
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 707
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_free_automa'):
        continue
    ndpi_free_automa = _lib.ndpi_free_automa
    ndpi_free_automa.argtypes = [POINTER(None)]
    ndpi_free_automa.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 718
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_add_string_value_to_automa'):
        continue
    ndpi_add_string_value_to_automa = _lib.ndpi_add_string_value_to_automa
    ndpi_add_string_value_to_automa.argtypes = [POINTER(None), String, c_ulong]
    ndpi_add_string_value_to_automa.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 728
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_add_string_to_automa'):
        continue
    ndpi_add_string_to_automa = _lib.ndpi_add_string_to_automa
    ndpi_add_string_to_automa.argtypes = [POINTER(None), String]
    ndpi_add_string_to_automa.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 736
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_finalize_automa'):
        continue
    ndpi_finalize_automa = _lib.ndpi_finalize_automa
    ndpi_finalize_automa.argtypes = [POINTER(None)]
    ndpi_finalize_automa.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 746
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_match_string'):
        continue
    ndpi_match_string = _lib.ndpi_match_string
    ndpi_match_string.argtypes = [POINTER(None), String]
    ndpi_match_string.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 748
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_load_ip_category'):
        continue
    ndpi_load_ip_category = _lib.ndpi_load_ip_category
    ndpi_load_ip_category.argtypes = [POINTER(struct_ndpi_detection_module_struct), String, ndpi_protocol_category_t]
    ndpi_load_ip_category.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 750
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_load_hostname_category'):
        continue
    ndpi_load_hostname_category = _lib.ndpi_load_hostname_category
    ndpi_load_hostname_category.argtypes = [POINTER(struct_ndpi_detection_module_struct), String, ndpi_protocol_category_t]
    ndpi_load_hostname_category.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 752
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_enable_loaded_categories'):
        continue
    ndpi_enable_loaded_categories = _lib.ndpi_enable_loaded_categories
    ndpi_enable_loaded_categories.argtypes = [POINTER(struct_ndpi_detection_module_struct)]
    ndpi_enable_loaded_categories.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 753
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_fill_ip_protocol_category'):
        continue
    ndpi_fill_ip_protocol_category = _lib.ndpi_fill_ip_protocol_category
    ndpi_fill_ip_protocol_category.argtypes = [POINTER(struct_ndpi_detection_module_struct), u_int32_t, u_int32_t, POINTER(ndpi_protocol)]
    ndpi_fill_ip_protocol_category.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 757
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_match_custom_category'):
        continue
    ndpi_match_custom_category = _lib.ndpi_match_custom_category
    ndpi_match_custom_category.argtypes = [POINTER(struct_ndpi_detection_module_struct), String, POINTER(c_ulong)]
    ndpi_match_custom_category.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 759
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_fill_protocol_category'):
        continue
    ndpi_fill_protocol_category = _lib.ndpi_fill_protocol_category
    ndpi_fill_protocol_category.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct), POINTER(ndpi_protocol)]
    ndpi_fill_protocol_category.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 762
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_custom_category_match'):
        continue
    ndpi_get_custom_category_match = _lib.ndpi_get_custom_category_match
    ndpi_get_custom_category_match.argtypes = [POINTER(struct_ndpi_detection_module_struct), String, POINTER(c_ulong)]
    ndpi_get_custom_category_match.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 764
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_set_detection_preferences'):
        continue
    ndpi_set_detection_preferences = _lib.ndpi_set_detection_preferences
    ndpi_set_detection_preferences.argtypes = [POINTER(struct_ndpi_detection_module_struct), ndpi_detection_preference, c_int]
    ndpi_set_detection_preferences.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 768
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_proto_defaults'):
        continue
    ndpi_get_proto_defaults = _lib.ndpi_get_proto_defaults
    ndpi_get_proto_defaults.argtypes = [POINTER(struct_ndpi_detection_module_struct)]
    ndpi_get_proto_defaults.restype = POINTER(ndpi_proto_defaults_t)
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 769
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_ndpi_num_supported_protocols'):
        continue
    ndpi_get_ndpi_num_supported_protocols = _lib.ndpi_get_ndpi_num_supported_protocols
    ndpi_get_ndpi_num_supported_protocols.argtypes = [POINTER(struct_ndpi_detection_module_struct)]
    ndpi_get_ndpi_num_supported_protocols.restype = u_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 770
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_ndpi_num_custom_protocols'):
        continue
    ndpi_get_ndpi_num_custom_protocols = _lib.ndpi_get_ndpi_num_custom_protocols
    ndpi_get_ndpi_num_custom_protocols.argtypes = [POINTER(struct_ndpi_detection_module_struct)]
    ndpi_get_ndpi_num_custom_protocols.restype = u_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 771
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_ndpi_detection_module_size'):
        continue
    ndpi_get_ndpi_detection_module_size = _lib.ndpi_get_ndpi_detection_module_size
    ndpi_get_ndpi_detection_module_size.argtypes = []
    ndpi_get_ndpi_detection_module_size.restype = u_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 772
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_set_log_level'):
        continue
    ndpi_set_log_level = _lib.ndpi_set_log_level
    ndpi_set_log_level.argtypes = [POINTER(struct_ndpi_detection_module_struct), u_int]
    ndpi_set_log_level.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 775
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_lru_cache_init'):
        continue
    ndpi_lru_cache_init = _lib.ndpi_lru_cache_init
    ndpi_lru_cache_init.argtypes = [u_int32_t]
    ndpi_lru_cache_init.restype = POINTER(struct_ndpi_lru_cache)
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 776
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_lru_free_cache'):
        continue
    ndpi_lru_free_cache = _lib.ndpi_lru_free_cache
    ndpi_lru_free_cache.argtypes = [POINTER(struct_ndpi_lru_cache)]
    ndpi_lru_free_cache.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 777
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_lru_find_cache'):
        continue
    ndpi_lru_find_cache = _lib.ndpi_lru_find_cache
    ndpi_lru_find_cache.argtypes = [POINTER(struct_ndpi_lru_cache), u_int32_t, u_int8_t]
    ndpi_lru_find_cache.restype = u_int8_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 778
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_lru_add_to_cache'):
        continue
    ndpi_lru_add_to_cache = _lib.ndpi_lru_add_to_cache
    ndpi_lru_add_to_cache.argtypes = [POINTER(struct_ndpi_lru_cache), u_int32_t]
    ndpi_lru_add_to_cache.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 789
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_match_string_id'):
        continue
    ndpi_match_string_id = _lib.ndpi_match_string_id
    ndpi_match_string_id.argtypes = [POINTER(None), String, POINTER(c_ulong)]
    ndpi_match_string_id.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 792
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'set_ndpi_malloc'):
        continue
    set_ndpi_malloc = _lib.set_ndpi_malloc
    set_ndpi_malloc.argtypes = [CFUNCTYPE(UNCHECKED(POINTER(None)), c_size_t)]
    set_ndpi_malloc.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 793
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'set_ndpi_free'):
        continue
    set_ndpi_free = _lib.set_ndpi_free
    set_ndpi_free.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(None))]
    set_ndpi_free.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 794
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'set_ndpi_flow_malloc'):
        continue
    set_ndpi_flow_malloc = _lib.set_ndpi_flow_malloc
    set_ndpi_flow_malloc.argtypes = [CFUNCTYPE(UNCHECKED(POINTER(None)), c_size_t)]
    set_ndpi_flow_malloc.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 795
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'set_ndpi_flow_free'):
        continue
    set_ndpi_flow_free = _lib.set_ndpi_flow_free
    set_ndpi_flow_free.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(None))]
    set_ndpi_flow_free.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 796
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'set_ndpi_debug_function'):
        continue
    set_ndpi_debug_function = _lib.set_ndpi_debug_function
    set_ndpi_debug_function.argtypes = [POINTER(struct_ndpi_detection_module_struct), ndpi_debug_function_ptr]
    set_ndpi_debug_function.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 798
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_malloc'):
        continue
    ndpi_malloc = _lib.ndpi_malloc
    ndpi_malloc.argtypes = [c_size_t]
    ndpi_malloc.restype = POINTER(None)
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 799
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_calloc'):
        continue
    ndpi_calloc = _lib.ndpi_calloc
    ndpi_calloc.argtypes = [c_ulong, c_size_t]
    ndpi_calloc.restype = POINTER(None)
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 800
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_free'):
        continue
    ndpi_free = _lib.ndpi_free
    ndpi_free.argtypes = [POINTER(None)]
    ndpi_free.restype = None
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 801
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_get_api_version'):
        continue
    ndpi_get_api_version = _lib.ndpi_get_api_version
    ndpi_get_api_version.argtypes = []
    ndpi_get_api_version.restype = u_int8_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 804
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_flowv4_flow_hash'):
        continue
    ndpi_flowv4_flow_hash = _lib.ndpi_flowv4_flow_hash
    ndpi_flowv4_flow_hash.argtypes = [u_int8_t, u_int32_t, u_int32_t, u_int16_t, u_int16_t, u_int8_t, u_int8_t, POINTER(u_char), u_int8_t]
    ndpi_flowv4_flow_hash.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 806
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_flowv6_flow_hash'):
        continue
    ndpi_flowv6_flow_hash = _lib.ndpi_flowv6_flow_hash
    ndpi_flowv6_flow_hash.argtypes = [u_int8_t, POINTER(struct_ndpi_in6_addr), POINTER(struct_ndpi_in6_addr), u_int16_t, u_int16_t, u_int8_t, u_int8_t, POINTER(u_char), u_int8_t]
    ndpi_flowv6_flow_hash.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 810
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_is_safe_ssl_cipher'):
        continue
    ndpi_is_safe_ssl_cipher = _lib.ndpi_is_safe_ssl_cipher
    ndpi_is_safe_ssl_cipher.argtypes = [u_int32_t]
    ndpi_is_safe_ssl_cipher.restype = u_int8_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 811
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_cipher2str'):
        continue
    ndpi_cipher2str = _lib.ndpi_cipher2str
    ndpi_cipher2str.argtypes = [u_int32_t]
    if sizeof(c_int) == sizeof(c_void_p):
        ndpi_cipher2str.restype = ReturnString
    else:
        ndpi_cipher2str.restype = String
        ndpi_cipher2str.errcheck = ReturnString
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 812
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_guess_host_protocol_id'):
        continue
    ndpi_guess_host_protocol_id = _lib.ndpi_guess_host_protocol_id
    ndpi_guess_host_protocol_id.argtypes = [POINTER(struct_ndpi_detection_module_struct), POINTER(struct_ndpi_flow_struct)]
    ndpi_guess_host_protocol_id.restype = u_int16_t
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 814
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndpi_has_human_readeable_string'):
        continue
    ndpi_has_human_readeable_string = _lib.ndpi_has_human_readeable_string
    ndpi_has_human_readeable_string.argtypes = [POINTER(struct_ndpi_detection_module_struct), String, u_int]
    ndpi_has_human_readeable_string.restype = c_int
    break

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 79
try:
    NDPI_USE_ASYMMETRIC_DETECTION = 0
except:
    pass

NDPI_SELECTION_BITMASK_PROTOCOL_SIZE = u_int32_t # /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 80

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 82
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_IP = (1 << 0)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 83
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_INT_TCP = (1 << 1)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 84
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_INT_UDP = (1 << 2)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 85
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_INT_TCP_OR_UDP = (1 << 3)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 86
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_HAS_PAYLOAD = (1 << 4)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 87
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_NO_TCP_RETRANSMISSION = (1 << 5)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 88
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_IPV6 = (1 << 6)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 89
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_IPV4_OR_IPV6 = (1 << 7)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 90
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_COMPLETE_TRAFFIC = (1 << 8)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 94
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_TCP = (NDPI_SELECTION_BITMASK_PROTOCOL_IP | NDPI_SELECTION_BITMASK_PROTOCOL_INT_TCP)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 95
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_UDP = (NDPI_SELECTION_BITMASK_PROTOCOL_IP | NDPI_SELECTION_BITMASK_PROTOCOL_INT_UDP)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 96
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_TCP_OR_UDP = (NDPI_SELECTION_BITMASK_PROTOCOL_IP | NDPI_SELECTION_BITMASK_PROTOCOL_INT_TCP_OR_UDP)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 99
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_V6_TCP = (NDPI_SELECTION_BITMASK_PROTOCOL_IPV6 | NDPI_SELECTION_BITMASK_PROTOCOL_INT_TCP)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 100
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_V6_UDP = (NDPI_SELECTION_BITMASK_PROTOCOL_IPV6 | NDPI_SELECTION_BITMASK_PROTOCOL_INT_UDP)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 101
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_V6_TCP_OR_UDP = (NDPI_SELECTION_BITMASK_PROTOCOL_IPV6 | NDPI_SELECTION_BITMASK_PROTOCOL_INT_TCP_OR_UDP)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 104
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_V4_V6_TCP = (NDPI_SELECTION_BITMASK_PROTOCOL_IPV4_OR_IPV6 | NDPI_SELECTION_BITMASK_PROTOCOL_INT_TCP)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 105
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_V4_V6_UDP = (NDPI_SELECTION_BITMASK_PROTOCOL_IPV4_OR_IPV6 | NDPI_SELECTION_BITMASK_PROTOCOL_INT_UDP)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 106
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_V4_V6_TCP_OR_UDP = (NDPI_SELECTION_BITMASK_PROTOCOL_IPV4_OR_IPV6 | NDPI_SELECTION_BITMASK_PROTOCOL_INT_TCP_OR_UDP)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 109
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_TCP_WITH_PAYLOAD = (NDPI_SELECTION_BITMASK_PROTOCOL_TCP | NDPI_SELECTION_BITMASK_PROTOCOL_HAS_PAYLOAD)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 110
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_V6_TCP_WITH_PAYLOAD = (NDPI_SELECTION_BITMASK_PROTOCOL_V6_TCP | NDPI_SELECTION_BITMASK_PROTOCOL_HAS_PAYLOAD)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 111
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_V4_V6_TCP_WITH_PAYLOAD = (NDPI_SELECTION_BITMASK_PROTOCOL_V4_V6_TCP | NDPI_SELECTION_BITMASK_PROTOCOL_HAS_PAYLOAD)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 114
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_UDP_WITH_PAYLOAD = (NDPI_SELECTION_BITMASK_PROTOCOL_UDP | NDPI_SELECTION_BITMASK_PROTOCOL_HAS_PAYLOAD)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 115
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_V6_UDP_WITH_PAYLOAD = (NDPI_SELECTION_BITMASK_PROTOCOL_V6_UDP | NDPI_SELECTION_BITMASK_PROTOCOL_HAS_PAYLOAD)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 116
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_V4_V6_UDP_WITH_PAYLOAD = (NDPI_SELECTION_BITMASK_PROTOCOL_V4_V6_UDP | NDPI_SELECTION_BITMASK_PROTOCOL_HAS_PAYLOAD)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 118
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_TCP_OR_UDP_WITH_PAYLOAD = (NDPI_SELECTION_BITMASK_PROTOCOL_TCP_OR_UDP | NDPI_SELECTION_BITMASK_PROTOCOL_HAS_PAYLOAD)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 119
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_V6_TCP_OR_UDP_WITH_PAYLOAD = (NDPI_SELECTION_BITMASK_PROTOCOL_V6_TCP_OR_UDP | NDPI_SELECTION_BITMASK_PROTOCOL_HAS_PAYLOAD)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 120
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_V4_V6_TCP_OR_UDP_WITH_PAYLOAD = (NDPI_SELECTION_BITMASK_PROTOCOL_V4_V6_TCP_OR_UDP | NDPI_SELECTION_BITMASK_PROTOCOL_HAS_PAYLOAD)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 122
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_TCP_WITHOUT_RETRANSMISSION = (NDPI_SELECTION_BITMASK_PROTOCOL_TCP | NDPI_SELECTION_BITMASK_PROTOCOL_NO_TCP_RETRANSMISSION)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 123
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_V6_TCP_WITHOUT_RETRANSMISSION = (NDPI_SELECTION_BITMASK_PROTOCOL_V6_TCP | NDPI_SELECTION_BITMASK_PROTOCOL_NO_TCP_RETRANSMISSION)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 124
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_V4_V6_TCP_WITHOUT_RETRANSMISSION = (NDPI_SELECTION_BITMASK_PROTOCOL_V4_V6_TCP | NDPI_SELECTION_BITMASK_PROTOCOL_NO_TCP_RETRANSMISSION)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 126
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_TCP_OR_UDP_WITHOUT_RETRANSMISSION = (NDPI_SELECTION_BITMASK_PROTOCOL_TCP_OR_UDP | NDPI_SELECTION_BITMASK_PROTOCOL_NO_TCP_RETRANSMISSION)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 127
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_V6_TCP_OR_UDP_WITHOUT_RETRANSMISSION = (NDPI_SELECTION_BITMASK_PROTOCOL_V6_TCP_OR_UDP | NDPI_SELECTION_BITMASK_PROTOCOL_NO_TCP_RETRANSMISSION)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 128
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_V4_V6_TCP_OR_UDP_WITHOUT_RETRANSMISSION = (NDPI_SELECTION_BITMASK_PROTOCOL_V4_V6_TCP_OR_UDP | NDPI_SELECTION_BITMASK_PROTOCOL_NO_TCP_RETRANSMISSION)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 130
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_TCP_WITH_PAYLOAD_WITHOUT_RETRANSMISSION = ((NDPI_SELECTION_BITMASK_PROTOCOL_TCP | NDPI_SELECTION_BITMASK_PROTOCOL_NO_TCP_RETRANSMISSION) | NDPI_SELECTION_BITMASK_PROTOCOL_HAS_PAYLOAD)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 131
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_V6_TCP_WITH_PAYLOAD_WITHOUT_RETRANSMISSION = ((NDPI_SELECTION_BITMASK_PROTOCOL_V6_TCP | NDPI_SELECTION_BITMASK_PROTOCOL_NO_TCP_RETRANSMISSION) | NDPI_SELECTION_BITMASK_PROTOCOL_HAS_PAYLOAD)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 132
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_V4_V6_TCP_WITH_PAYLOAD_WITHOUT_RETRANSMISSION = ((NDPI_SELECTION_BITMASK_PROTOCOL_V4_V6_TCP | NDPI_SELECTION_BITMASK_PROTOCOL_NO_TCP_RETRANSMISSION) | NDPI_SELECTION_BITMASK_PROTOCOL_HAS_PAYLOAD)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 134
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_TCP_OR_UDP_WITH_PAYLOAD_WITHOUT_RETRANSMISSION = ((NDPI_SELECTION_BITMASK_PROTOCOL_TCP_OR_UDP | NDPI_SELECTION_BITMASK_PROTOCOL_NO_TCP_RETRANSMISSION) | NDPI_SELECTION_BITMASK_PROTOCOL_HAS_PAYLOAD)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 135
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_V6_TCP_OR_UDP_WITH_PAYLOAD_WITHOUT_RETRANSMISSION = ((NDPI_SELECTION_BITMASK_PROTOCOL_V6_TCP_OR_UDP | NDPI_SELECTION_BITMASK_PROTOCOL_NO_TCP_RETRANSMISSION) | NDPI_SELECTION_BITMASK_PROTOCOL_HAS_PAYLOAD)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 136
try:
    NDPI_SELECTION_BITMASK_PROTOCOL_V4_V6_TCP_OR_UDP_WITH_PAYLOAD_WITHOUT_RETRANSMISSION = ((NDPI_SELECTION_BITMASK_PROTOCOL_V4_V6_TCP_OR_UDP | NDPI_SELECTION_BITMASK_PROTOCOL_NO_TCP_RETRANSMISSION) | NDPI_SELECTION_BITMASK_PROTOCOL_HAS_PAYLOAD)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 140
def NDPI_SRC_HAS_PROTOCOL(src, protocol):
    return ((src != NULL) and (((NDPI_COMPARE_PROTOCOL_TO_BITMASK (((src.contents.detected_protocol_bitmask).value), protocol)).value) != 0))

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 142
def NDPI_DST_HAS_PROTOCOL(dst, protocol):
    return ((dst != NULL) and (((NDPI_COMPARE_PROTOCOL_TO_BITMASK (((dst.contents.detected_protocol_bitmask).value), protocol)).value) != 0))

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 144
def NDPI_SRC_OR_DST_HAS_PROTOCOL(src, dst, protocol):
    return ((NDPI_SRC_HAS_PROTOCOL (src, protocol)) or (NDPI_SRC_HAS_PROTOCOL (dst, protocol)))

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 151
def NDPI_FLOW_PROTOCOL_EXCLUDED(ndpi_struct, flow, protocol):
    return ((flow != NULL) and ((((NDPI_COMPARE_PROTOCOL_TO_BITMASK (((ndpi_struct.contents.detection_bitmask).value), protocol)).value) == 0) or (((NDPI_COMPARE_PROTOCOL_TO_BITMASK (((flow.contents.excluded_protocol_bitmask).value), protocol)).value) != 0)))

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 156
try:
    NDPI_DEFAULT_MAX_TCP_RETRANSMISSION_WINDOW_SIZE = 65536
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 162
try:
    NDPI_MAX_PARSE_LINES_PER_PACKET = 64
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 164
try:
    MAX_PACKET_COUNTER = 65000
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 165
try:
    MAX_DEFAULT_PORTS = 5
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 167
try:
    NDPI_DIRECTCONNECT_CONNECTION_IP_TICK_TIMEOUT = 600
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 168
try:
    NDPI_IRC_CONNECTION_TIMEOUT = 120
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 169
try:
    NDPI_GNUTELLA_CONNECTION_TIMEOUT = 60
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 170
try:
    NDPI_BATTLEFIELD_CONNECTION_TIMEOUT = 60
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 171
try:
    NDPI_THUNDER_CONNECTION_TIMEOUT = 30
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 172
try:
    NDPI_RTSP_CONNECTION_TIMEOUT = 5
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 173
try:
    NDPI_TVANTS_CONNECTION_TIMEOUT = 5
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 174
try:
    NDPI_YAHOO_DETECT_HTTP_CONNECTIONS = 1
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 175
try:
    NDPI_YAHOO_LAN_VIDEO_TIMEOUT = 30
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 176
try:
    NDPI_ZATTOO_CONNECTION_TIMEOUT = 120
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 177
try:
    NDPI_ZATTOO_FLASH_TIMEOUT = 5
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 178
try:
    NDPI_JABBER_STUN_TIMEOUT = 30
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 179
try:
    NDPI_JABBER_FT_TIMEOUT = 5
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 180
try:
    NDPI_SOULSEEK_CONNECTION_IP_TICK_TIMEOUT = 600
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 249
def NDPI_STATICSTRING_LEN(s):
    return (sizeof(s) - 1)

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 252
def NDPI_COMPARE_IPV6_ADDRESS_STRUCTS(x, y):
    return (((x [0]) < (y [0])) or (((x [0]) == (y [0])) and ((x [1]) < (y [1]))))

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 255
try:
    NDPI_NUM_BITS = 512
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 257
try:
    NDPI_BITS = (sizeof(ndpi_ndpi_mask) * 8)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 258
def howmanybits(x, y):
    return ((x + (y - 1)) / y)

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 261
def NDPI_SET(p, n):
    return (((p.contents.fds_bits) [(n / NDPI_BITS)]) | (1 << (n % NDPI_BITS)))

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 262
def NDPI_CLR(p, n):
    return (((p.contents.fds_bits) [(n / NDPI_BITS)]) & (~(1 << (n % NDPI_BITS))))

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 263
def NDPI_ISSET(p, n):
    return ((((p.contents.fds_bits).value) [(n / NDPI_BITS)]) & (1 << (n % NDPI_BITS)))

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 264
def NDPI_ZERO(p):
    return (memset (p, 0, sizeof((p[0]))))

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 265
def NDPI_ONE(p):
    return (memset (p, 255, sizeof((p[0]))))

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 267
try:
    NDPI_NUM_FDS_BITS = (howmanybits (NDPI_NUM_BITS, NDPI_BITS))
except:
    pass

NDPI_PROTOCOL_BITMASK = ndpi_protocol_bitmask_struct_t # /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 269

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 271
def NDPI_BITMASK_ADD(a, b):
    return (NDPI_SET (pointer(a), b))

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 272
def NDPI_BITMASK_DEL(a, b):
    return (NDPI_CLR (pointer(a), b))

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 273
def NDPI_BITMASK_RESET(a):
    return (NDPI_ZERO (pointer(a)))

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 274
def NDPI_BITMASK_SET_ALL(a):
    return (NDPI_ONE (pointer(a)))

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 280
def NDPI_ADD_PROTOCOL_TO_BITMASK(bmask, value):
    return (NDPI_SET (pointer(bmask), value))

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 281
def NDPI_DEL_PROTOCOL_FROM_BITMASK(bmask, value):
    return (NDPI_CLR (pointer(bmask), value))

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 282
def NDPI_COMPARE_PROTOCOL_TO_BITMASK(bmask, value):
    return (NDPI_ISSET (pointer(bmask), value))

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 287
def ndpi_min(a, b):
    return (a < b) and a or b

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 288
def ndpi_max(a, b):
    return (a > b) and a or b

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 295
try:
    NDPI_IPSEC_PROTOCOL_ESP = 50
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 296
try:
    NDPI_IPSEC_PROTOCOL_AH = 51
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 297
try:
    NDPI_GRE_PROTOCOL_TYPE = 47
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 298
try:
    NDPI_ICMP_PROTOCOL_TYPE = 1
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 299
try:
    NDPI_IGMP_PROTOCOL_TYPE = 2
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 300
try:
    NDPI_EGP_PROTOCOL_TYPE = 8
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 301
try:
    NDPI_OSPF_PROTOCOL_TYPE = 89
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 302
try:
    NDPI_SCTP_PROTOCOL_TYPE = 132
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 303
try:
    NDPI_IPIP_PROTOCOL_TYPE = 4
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 304
try:
    NDPI_ICMPV6_PROTOCOL_TYPE = 58
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 307
def get_u_int8_t(X, O):
    return ((X + O)[0])

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 308
def get_u_int16_t(X, O):
    return ((X + O)[0])

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 309
def get_u_int32_t(X, O):
    return ((X + O)[0])

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 310
def get_u_int64_t(X, O):
    return ((X + O)[0])

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 313
def get_ul8(X, O):
    return (get_u_int8_t (X, O))

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 317
def get_l16(X, O):
    return (get_u_int16_t (X, O))

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 318
def get_l32(X, O):
    return (get_u_int32_t (X, O))

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 328
def match_first_bytes(payload, st):
    return (((memcmp (payload, st, (sizeof(st) - 1))).value) == 0)

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 334
try:
    NDPI_MAX_DNS_REQUESTS = 16
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 335
try:
    NDPI_MIN_NUM_STUN_DETECTION = 8
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 337
try:
    NDPI_MAJOR = 2
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 338
try:
    NDPI_MINOR = 9
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 339
try:
    NDPI_PATCH = 0
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 342
try:
    NDPI_CIPHER_SAFE = 0
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 343
try:
    NDPI_CIPHER_WEAK = 1
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_define.h: 344
try:
    NDPI_CIPHER_INSECURE = 2
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 34
try:
    NDPI_PROTOCOL_SIZE = 2
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 292
try:
    NDPI_PROTOCOL_NO_MASTER_PROTO = NDPI_PROTOCOL_UNKNOWN
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 293
try:
    NDPI_MAX_SUPPORTED_PROTOCOLS = NDPI_LAST_IMPLEMENTED_PROTOCOL
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_protocol_ids.h: 294
try:
    NDPI_MAX_NUM_CUSTOM_PROTOCOLS = (NDPI_NUM_BITS - NDPI_LAST_IMPLEMENTED_PROTOCOL)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 350
try:
    TINC_CACHE_MAX_SIZE = 10
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 391
try:
    NDPI_PROTOCOL_IRC_MAXPORT = 8
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 429
try:
    NDPI_BT_PORTS = 8
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 434
try:
    JABBER_MAX_STUN_PORTS = 6
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 766
try:
    NUM_BREEDS = (NDPI_PROTOCOL_UNRATED + 1)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 878
try:
    NUM_CUSTOM_CATEGORIES = 5
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 879
try:
    CUSTOM_CATEGORY_LABEL_LEN = 32
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_main.h: 150
def ndpi_match_strprefix(payload, payload_len, str):
    return (ndpi_match_prefix (payload, payload_len, str, (sizeof(str) - 1)))

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 37
try:
    NDPI_API_VERSION = 1
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 39
try:
    SIZEOF_ID_STRUCT = sizeof(struct_ndpi_id_struct)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 40
try:
    SIZEOF_FLOW_STRUCT = sizeof(struct_ndpi_flow_struct)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 42
try:
    NDPI_DETECTION_ONLY_IPV4 = (1 << 0)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 43
try:
    NDPI_DETECTION_ONLY_IPV6 = (1 << 1)
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 45
try:
    ADD_TO_DETECTION_BITMASK = 1
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 46
try:
    NO_ADD_TO_DETECTION_BITMASK = 0
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 47
try:
    SAVE_DETECTION_BITMASK_AS_UNKNOWN = 1
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_api.h: 48
try:
    NO_SAVE_DETECTION_BITMASK_AS_UNKNOWN = 0
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_config.h: 5
try:
    HAVE_DLFCN_H = 1
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_config.h: 11
try:
    HAVE_INTTYPES_H = 1
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_config.h: 23
try:
    HAVE_MEMORY_H = 1
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_config.h: 26
try:
    HAVE_NETINET_IN_H = 1
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_config.h: 29
try:
    HAVE_PTHREAD = 1
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_config.h: 32
try:
    HAVE_PTHREAD_PRIO_INHERIT = 1
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_config.h: 35
try:
    HAVE_PTHREAD_SETAFFINITY_NP = 1
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_config.h: 38
try:
    HAVE_STDINT_H = 1
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_config.h: 41
try:
    HAVE_STDLIB_H = 1
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_config.h: 44
try:
    HAVE_STRINGS_H = 1
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_config.h: 47
try:
    HAVE_STRING_H = 1
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_config.h: 50
try:
    HAVE_SYS_STAT_H = 1
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_config.h: 53
try:
    HAVE_SYS_TYPES_H = 1
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_config.h: 56
try:
    HAVE_UNISTD_H = 1
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_config.h: 59
try:
    LT_OBJDIR = '.libs/'
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_config.h: 65
try:
    NDPI_GIT_DATE = 'Sun Jun 30 15:34:00 2019 +0200'
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_config.h: 68
try:
    NDPI_GIT_RELEASE = '2.9.0-1583-65e842e'
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_config.h: 71
try:
    NDPI_MAJOR_RELEASE = '2'
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_config.h: 74
try:
    NDPI_MINOR_RELEASE = '9'
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_config.h: 77
try:
    NDPI_PATCH_LEVEL = '0'
except:
    pass

# /home/massimo/Desktop/nDPI/src/include/ndpi_config.h: 105
try:
    STDC_HEADERS = 1
except:
    pass

node_t = struct_node_t # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 47

ndpi_protocol_bitmask_struct = struct_ndpi_protocol_bitmask_struct # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 58

ndpi_chdlc = struct_ndpi_chdlc # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 89

ndpi_slarp = struct_ndpi_slarp # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 102

ndpi_cdp = struct_ndpi_cdp # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 113

ndpi_ethhdr = struct_ndpi_ethhdr # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 123

ndpi_snap_extension = struct_ndpi_snap_extension # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 133

ndpi_llc_header_snap = struct_ndpi_llc_header_snap # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 142

ndpi_radiotap_header = struct_ndpi_radiotap_header # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 154

ndpi_wifi_header = struct_ndpi_wifi_header # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 167

ndpi_mpls_header = struct_ndpi_mpls_header # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 183

ndpi_iphdr = struct_ndpi_iphdr # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 205

ndpi_in6_addr = struct_ndpi_in6_addr # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 210

ndpi_ip6_hdrctl = struct_ndpi_ip6_hdrctl # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 218

ndpi_ipv6hdr = struct_ndpi_ipv6hdr # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 226

ndpi_tcphdr = struct_ndpi_tcphdr # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 251

ndpi_udphdr = struct_ndpi_udphdr # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 262

ndpi_dns_packet_header = struct_ndpi_dns_packet_header # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 272

ndpi_icmphdr = struct_ndpi_icmphdr # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 303

spinlock = struct_spinlock # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 312

atomic = struct_atomic # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 316

hash_ip4p_node = struct_hash_ip4p_node # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 318

hash_ip4p = struct_hash_ip4p # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 326

hash_ip4p_table = struct_hash_ip4p_table # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 332

bt_announce = struct_bt_announce # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 340

tinc_cache_entry = struct_tinc_cache_entry # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 356

ndpi_lru_cache = struct_ndpi_lru_cache # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 371

ndpi_id_struct = struct_ndpi_id_struct # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 375

ndpi_flow_tcp_struct = struct_ndpi_flow_tcp_struct # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 471

ndpi_flow_udp_struct = struct_ndpi_flow_udp_struct # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 618

ndpi_int_one_line_struct = struct_ndpi_int_one_line_struct # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 673

ndpi_packet_struct = struct_ndpi_packet_struct # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 678

ndpi_detection_module_struct = struct_ndpi_detection_module_struct # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 737

ndpi_flow_struct = struct_ndpi_flow_struct # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 1036

ndpi_call_function_struct = struct_ndpi_call_function_struct # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 740

ndpi_subprotocol_conf_struct = struct_ndpi_subprotocol_conf_struct # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 748

ndpi_proto_defaults = struct_ndpi_proto_defaults # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 853

ndpi_default_ports_tree_node = struct_ndpi_default_ports_tree_node # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 859

_ndpi_automa = struct__ndpi_automa # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 864

ndpi_proto = struct_ndpi_proto # /home/massimo/Desktop/nDPI/src/include/ndpi_typedefs.h: 874

# No inserted files

