import argparse
import sys
import datetime
import socket
import struct
from ndpi_typestruct import *
from scapy.all import *


# ------- return type & pcapstruct to declare -------


class pcap_pkthdr(Structure):
    _fields_ = [("ts", timeval), ("caplen", c_uint32), ("len", c_uint32)]


class workflow(Structure):
    _fields_ = [("src_ip", c_uint32),
                ("dst_ip", c_uint32),
                ("src_port", c_uint16),
                ("dst_port", c_uint16),
                ("protocol", c_uint8),
                ("packets", c_uint32),
                ("detected_protocol", ndpi_protocol),
                ("detection_completed", c_uint8),
                ("id", c_uint32),
                ("src_id", POINTER(ndpi_id_struct)),
                ("dst_id", POINTER(ndpi_id_struct)),
                ("flow", POINTER(ndpi_flow_struct))]


CMCFUN = CFUNCTYPE(c_int, c_void_p, c_void_p)
GUESS = CFUNCTYPE(None, c_void_p, c_int32, c_int, c_void_p)
FREE = CFUNCTYPE(None,c_void_p)


def node_proto_guess_walker(nodo, which, depth, user_data):
    global ndpi_info_mod

    flow = cast(nodo, POINTER(POINTER(workflow))).contents.contents
    if which == 0 or which == 3:
        if flow.detection_completed == 0:  # order for tree operation
            print('ip src ' + str(socket.ntohl(flow.src_ip)) + ' porta ' + str(flow.src_port) + ' ip dst ' + str(flow.dst_ip) + ' porta ' + str(
                flow.dst_port) + ' proto ' + str(flow.protocol))
            flow.detected_protocol = ndpi.ndpi_detection_giveup(ndpi_info_mod, flow.flow, flow.protocol,
                                                                int(socket.ntohl(flow.src_ip)), 1)
        print('protocol ' + str(flow.detected_protocol.app_protocol) + ' numero pacchetti ' + str(flow.packets) + ' il suo src è ' + str(flow.dst_ip))
        count_protocol[flow.detected_protocol.app_protocol] += flow.packets


def py_cmp_fun(a, b):
    fa = cast(a, POINTER(workflow))
    fb = cast(b, POINTER(workflow))

    if fa.contents.src_ip < fb.contents.src_ip: return -1
    elif fa.contents.src_ip > fb.contents.src_ip: return 1
    if fa.contents.src_port < fb.contents.src_port: return -1
    elif fa.contents.src_port > fb.contents.src_port: return 1
    if fa.contents.dst_ip < fb.contents.dst_ip: return -1
    elif fa.contents.dst_ip > fb.contents.dst_ip: return 1
    if fa.contents.dst_port < fb.contents.dst_port: return -1
    elif fa.contents.dst_port > fb.contents.dst_port: return 1
    if fa.contents.protocol < fb.contents.protocol: return -1
    elif fa.contents.protocol > fb.contents.protocol: return 1
    return 0


def freer(a):
    pass

ndpi.ndpi_revision.restype = c_void_p
ndpi.ndpi_tfind.restype = c_void_p
ndpi.ndpi_tsearch.restype = c_void_p
ndpi.ndpi_get_proto_name.restype = c_void_p
ndpi.ndpi_get_num_supported_protocols.restype = c_uint
ndpi.ndpi_detection_process_packet.restype = ndpi_protocol
ndpi.ndpi_guess_undetected_protocol.restype = ndpi_protocol
ndpi.ndpi_init_detection_module.restype = POINTER(ndpi_detection_module_struct)
ndpi.ndpi_wrap_NDPI_BITMASK_SET_ALL.argtypes = [POINTER(NDPI_PROTOCOL_BITMASK)]
ndpi.ndpi_set_protocol_detection_bitmask2.argtypes = [POINTER(ndpi_detection_module_struct), POINTER(NDPI_PROTOCOL_BITMASK)]
ndpi.ndpi_tsearch.argtypes = [c_void_p, POINTER(c_void_p), CMCFUN]
ndpi.ndpi_twalk.argtypes = [c_void_p, GUESS, c_void_p]
ndpi.ndpi_detection_giveup.restype = ndpi_protocol
ndpi.ndpi_detection_giveup.argtypes = [POINTER(ndpi_detection_module_struct), POINTER(ndpi_flow_struct), c_uint8]
ndpi.ndpi_guess_undetected_protocol.argtypes = [POINTER(ndpi_detection_module_struct), POINTER(ndpi_flow_struct), c_uint8, c_uint32, c_uint32, c_uint32, c_uint32]
ndpi.ndpi_detection_process_packet.argtypes = [POINTER(ndpi_detection_module_struct), POINTER(ndpi_flow_struct), POINTER(c_ubyte), c_ushort, c_uint64, POINTER(ndpi_id_struct), POINTER(ndpi_id_struct)]
cmp_func = CMCFUN(py_cmp_fun)
guess_walker = GUESS(node_proto_guess_walker)
free_walk = FREE(freer)

# --------------------------------------

#number of anylized packet
packet_number = 0
flow_count = 0
max_num_udp_dissected_pkts = 16
max_num_tcp_dissected_pkts = 10
flows_root = c_void_p(None)
flows_root_ref = pointer(flows_root)
count_protocol = (c_int32 * (ndpi.ndpi_wrap_ndpi_max_supported_protocols() + ndpi.ndpi_wrap_ndpi_max_num_custom_protocols() + 1))()
lista = []  # used to avoid impropriate memory allocation from python


#check ndpi version
if ndpi.ndpi_get_api_version() != ndpi.ndpi_wrap_get_api_version():
    print("nDPI Library version mismatch: please make sure this code and the nDPI library are in sync\n")
    sys.exit(-1)

# create data structure of ndpi
all = NDPI_PROTOCOL_BITMASK()
ndpi_info_mod = ndpi.ndpi_init_detection_module()
if ndpi_info_mod is None:
    sys.exit(-1)


def ip2int(ip):
    """
    Convert an IP string to long and then c_uint32
    """
    packedIP = socket.inet_aton(ip)
    return int(struct.unpack("!I", packedIP)[0])


def get_flow(packet):
    global flows_root
    global flows_root_ref
    global flow_count

    ip_packet = packet[1]
    ip_protocol = ip_packet.proto
    transport_packet = None

    if ip_protocol == 6 or ip_protocol == 17: transport_packet = packet[2]
    if transport_packet is not None:
        # to avoid two nodes in one binary tree for a flow
        ip_src = ip2int(ip_packet.src)
        ip_dst = ip2int(ip_packet.dst)
        src_port = transport_packet.sport
        dst_port = transport_packet.dport
    else: return None
    # set flows to correct type and data
    ndpi_flow = pointer(ndpi_flow_struct())
    memset(ndpi_flow, 0, sizeof(ndpi_flow_struct))
    if ip_src > ip_dst:
        flow = workflow(ip_src, ip_dst, src_port, dst_port, int(ip_packet.proto), 0, ndpi_protocol(), 0, 0, pointer(ndpi_id_struct()), pointer(ndpi_id_struct()), ndpi_flow)
    else:
        flow = workflow(ip_dst, ip_src, dst_port, src_port, int(ip_packet.proto), 0, ndpi_protocol(), 0, 0, pointer(ndpi_id_struct()), pointer(ndpi_id_struct()), ndpi_flow)
    flow_ref = pointer(flow)
    res = ndpi.ndpi_tfind(flow_ref, flows_root_ref, cmp_func)
    if res is None:
        ndpi.ndpi_tsearch(flow_ref, pointer(flows_root), cmp_func)  # add
        print('ip src ' + str(flow.src_ip) + ' porta ' + str(flow.src_port) + ' ip dst ' +
              str(flow.dst_ip) + ' porta ' + str(flow.dst_port))
        lista.append(flow)
        flow_count += 1
        return pointer(flow)
    flow = cast(res, POINTER(POINTER(workflow))).contents
    return flow


def packetcaptured(packet):
    global packet_number
    global start_time
    global ndpi_info_mod

    flow = None
    h = pcap_pkthdr()

    #getting flow
    try:
        flow = get_flow(packet)
    except AttributeError:
        #ignore packet
        pass
    if flow is None: return

    #filling pcap_pkthdr
    h.len = h.caplen = len(packet)
    h.ts.tv_sec = int(packet["IP"].time/1000000)
    h.ts.tv_usec = round(packet["IP"].time)

    # real work
    if int(packet[1].frag) == 0:  # not fragmented packet
        flow.contents.packets += 1
        packet_number += 1
        # get ndpi_iphdr address
        iphdr_addr = cast(c_char_p(packet[1].build()), c_void_p)
        ndpi_flow = flow.contents.flow

        if flow.contents.detection_completed is 0:
            flow.contents.detected_protocol = ndpi.ndpi_detection_process_packet(ndpi_info_mod, ndpi_flow, cast(iphdr_addr, POINTER(c_uint8)),
                    int(packet[1].len), h.ts.tv_usec, flow.contents.src_id, flow.contents.dst_id)

            flow1 = flow.contents.detected_protocol

            valid = False
            if flow.contents.protocol == 6: valid = flow.contents.packets > max_num_tcp_dissected_pkts
            elif flow.contents.protocol == 17: valid = flow.contents.packets > max_num_udp_dissected_pkts
            if valid or flow1.app_protocol is not 0:
                if valid or flow1.master_protocol is not 91: #or # 91 is NDPI_PROTOCOL_TLS
                    flow.contents.detection_completed = 1
                    if flow1.app_protocol is 0:
                        flow.contents.detected_protocol = ndpi.ndpi_detection_giveup(ndpi_info_mod, ndpi_flow, 1)



def result():
    global flows_root_ref
    global ndpi_info_mod
    print('\n\n\n\n\n')
    print('number of anylized packet ' + str(packet_number))
    print('number of flows ' + str(flow_count))

    ndpi.ndpi_twalk(flows_root_ref.contents, guess_walker, None)

    print('\nDetected protocols:')
    for i in range(0, ndpi.ndpi_get_num_supported_protocols(ndpi_info_mod)):
        if count_protocol[i] > 0:
            print(cast(ndpi.ndpi_get_proto_name(ndpi_info_mod, i), c_char_p).value + ': '.encode('UTF-8') + str(count_protocol[i]).encode('UTF-8'))


def free(ndpi_struct):
    ndpi.ndpi_tdestroy(flows_root, free_walk)
    ndpi.ndpi_exit_detection_module(ndpi_struct)


#inizialize(ndpi_info_mod, all)
ndpi.ndpi_wrap_NDPI_BITMASK_SET_ALL(pointer(all))
ndpi.ndpi_set_protocol_detection_bitmask2(ndpi_info_mod, pointer(all))

print('Using nDPI ' + str(cast(ndpi.ndpi_revision(), c_char_p).value))
print('Capturing live traffic from device ' + sys.argv[1] + '...')

scapy_cap = rdpcap(sys.argv[1])
for packet in scapy_cap:
    packetcaptured(packet)
'''
try:
    sniff(iface=sys.argv[1], prn=packetcaptured)
except KeyboardInterrupt:
    print('\nInterrupted\n')
'''
result()
free(ndpi_info_mod)
