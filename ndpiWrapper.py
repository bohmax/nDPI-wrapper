import sys
from ctypes import *

class timeval(Structure):
    _fields_ = [("tv_sec", c_long), ("tv_usec", c_long)]

ndpi = CDLL('/home/massimo/Desktop/nDPI/example/ndpiReader.so')

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

length = len(sys.argv)

#crea un array di ctypes
arr = (c_char_p * length)()
arr[0] = './ndpiReader'.encode('utf-8')
for i in range(1, length):
    arr[i] = sys.argv[i].encode('utf-8')

#ndpi.main(length, arr)

#verifica la versione di ndpi
if ndpi.ndpi_get_api_version() != ndpi.ndpi_wrap_get_api_version():
    print("nDPI Library version mismatch: please make sure this code and the nDPI library are in sync\n")
    sys.exit(-1)

#timestamp
startup_time = timeval(0, 0)
ndpi.gettimeofday(byref(startup_time), None)

#creazione struttura dati di ndpi
ndpi_info_mod = ndpi.ndpi_init_detection_module()
if ndpi_info_mod == None:
    sys.exit(-1)
print(ndpi_info_mod.detection_bitmask)
