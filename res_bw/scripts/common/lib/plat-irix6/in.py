# 2016.08.04 20:00:56 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/plat-irix6/IN.py
from warnings import warnpy3k
warnpy3k('the IN module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
_MIPS_ISA_MIPS1 = 1
_MIPS_ISA_MIPS2 = 2
_MIPS_ISA_MIPS3 = 3
_MIPS_ISA_MIPS4 = 4
_MIPS_SIM_ABI32 = 1
_MIPS_SIM_NABI32 = 2
_MIPS_SIM_ABI64 = 3
ONBITSMAJOR = 7
ONBITSMINOR = 8
OMAXMAJ = 127
OMAXMIN = 255
NBITSMAJOR = 14
NBITSMINOR = 18
MAXMAJ = 511
MAXMIN = 262143
OLDDEV = 0
NEWDEV = 1
MKDEV_VER = NEWDEV

def IS_STRING_SPEC_DEV(x):
    return dev_t(x) == __makedev(MKDEV_VER, 0, 0)


def major(dev):
    return __major(MKDEV_VER, dev)


def minor(dev):
    return __minor(MKDEV_VER, dev)


FD_SETSIZE = 1024
__NBBY = 8
NULL = 0L
NBBY = 8
LITTLE_ENDIAN = 1234
BIG_ENDIAN = 4321
PDP_ENDIAN = 3412
_LITTLE_ENDIAN = 1234
_BIG_ENDIAN = 4321
_PDP_ENDIAN = 3412
_BYTE_ORDER = _BIG_ENDIAN
_BYTE_ORDER = _LITTLE_ENDIAN

def ntohl(x):
    return x


def ntohs(x):
    return x


def htonl(x):
    return x


def htons(x):
    return x


def htonl(x):
    return ntohl(x)


def htons(x):
    return ntohs(x)


P_MYID = -1
P_MYHOSTID = -1
MAXCPU = 128

def CPUMASK_INDEX(bit):
    return bit >> 6


def CPUMASK_SHFT(bit):
    return bit & 63


def CPUMASK_IS_ZERO(p):
    return p == 0


def CPUMASK_IS_NONZERO(p):
    return p != 0


def CNODEMASK_IS_ZERO(p):
    return p == 0


def CNODEMASK_IS_NONZERO(p):
    return p != 0


IPPROTO_IP = 0
IPPROTO_HOPOPTS = 0
IPPROTO_ICMP = 1
IPPROTO_IGMP = 2
IPPROTO_GGP = 3
IPPROTO_IPIP = 4
IPPROTO_ENCAP = IPPROTO_IPIP
IPPROTO_ST = 5
IPPROTO_TCP = 6
IPPROTO_UCL = 7
IPPROTO_EGP = 8
IPPROTO_IGP = 9
IPPROTO_BBN_RCC_MON = 10
IPPROTO_NVP_II = 11
IPPROTO_PUP = 12
IPPROTO_ARGUS = 13
IPPROTO_EMCON = 14
IPPROTO_XNET = 15
IPPROTO_CHAOS = 16
IPPROTO_UDP = 17
IPPROTO_MUX = 18
IPPROTO_DCN_MEAS = 19
IPPROTO_HMP = 20
IPPROTO_PRM = 21
IPPROTO_IDP = 22
IPPROTO_TRUNK_1 = 23
IPPROTO_TRUNK_2 = 24
IPPROTO_LEAF_1 = 25
IPPROTO_LEAF_2 = 26
IPPROTO_RDP = 27
IPPROTO_IRTP = 28
IPPROTO_TP = 29
IPPROTO_NETBLT = 30
IPPROTO_MFE_NSP = 31
IPPROTO_MERIT_INP = 32
IPPROTO_SEP = 33
IPPROTO_3PC = 34
IPPROTO_IDPR = 35
IPPROTO_XTP = 36
IPPROTO_DDP = 37
IPPROTO_IDPR_CMTP = 38
IPPROTO_TPPP = 39
IPPROTO_IL = 40
IPPROTO_IPV6 = 41
IPPROTO_ROUTING = 43
IPPROTO_FRAGMENT = 44
IPPROTO_RSVP = 46
IPPROTO_ESP = 50
IPPROTO_AH = 51
IPPROTO_ICMPV6 = 58
IPPROTO_NONE = 59
IPPROTO_DSTOPTS = 60
IPPROTO_CFTP = 62
IPPROTO_HELLO = 63
IPPROTO_SAT_EXPAK = 64
IPPROTO_KRYPTOLAN = 65
IPPROTO_RVD = 66
IPPROTO_IPPC = 67
IPPROTO_SAT_MON = 69
IPPROTO_VISA = 70
IPPROTO_IPCV = 71
IPPROTO_CPNX = 72
IPPROTO_CPHB = 73
IPPROTO_WSN = 74
IPPROTO_PVP = 75
IPPROTO_BR_SAT_MON = 76
IPPROTO_ND = 77
IPPROTO_WB_MON = 78
IPPROTO_WB_EXPAK = 79
IPPROTO_EON = 80
IPPROTO_VMTP = 81
IPPROTO_SECURE_VMTP = 82
IPPROTO_VINES = 83
IPPROTO_TTP = 84
IPPROTO_NSFNET_IGP = 85
IPPROTO_DGP = 86
IPPROTO_TCF = 87
IPPROTO_IGRP = 88
IPPROTO_OSPF = 89
IPPROTO_SPRITE_RPC = 90
IPPROTO_LARP = 91
IPPROTO_MTP = 92
IPPROTO_AX25 = 93
IPPROTO_SWIPE = 94
IPPROTO_MICP = 95
IPPROTO_AES_SP3_D = 96
IPPROTO_ETHERIP = 97
IPPROTO_ENCAPHDR = 98
IPPROTO_RAW = 255
IPPROTO_MAX = 256
IPPROTO_STP = 257
IPPORT_RESERVED = 1024
IPPORT_MAXPORT = 65535
INET_ADDRSTRLEN = 16
INET6_ADDRSTRLEN = 46

def IN_CLASSA(i):
    return __int32_t(i) & 2147483648L == 0


IN_CLASSA_NET = 4278190080L
IN_CLASSA_NSHIFT = 24
IN_CLASSA_HOST = 16777215
IN_CLASSA_MAX = 128

def IN_CLASSB(i):
    return __int32_t(i) & 3221225472L == 2147483648L


IN_CLASSB_NET = 4294901760L
IN_CLASSB_NSHIFT = 16
IN_CLASSB_HOST = 65535
IN_CLASSB_MAX = 65536

def IN_CLASSC(i):
    return __int32_t(i) & 3758096384L == 3221225472L


IN_CLASSC_NET = 4294967040L
IN_CLASSC_NSHIFT = 8
IN_CLASSC_HOST = 255

def IN_CLASSD(i):
    return __int32_t(i) & 4026531840L == 3758096384L


IN_CLASSD_NET = 4026531840L
IN_CLASSD_NSHIFT = 28
IN_CLASSD_HOST = 268435455

def IN_MULTICAST(i):
    return IN_CLASSD(i)


def IN_EXPERIMENTAL(i):
    return __int32_t(i) & 4026531840L == 4026531840L


def IN_BADCLASS(i):
    return __int32_t(i) & 4026531840L == 4026531840L


INADDR_NONE = 4294967295L
IN_LOOPBACKNET = 127
IPNGVERSION = 6
IPV6_FLOWINFO_FLOWLABEL = 16777215
IPV6_FLOWINFO_PRIORITY = 251658240
IPV6_FLOWINFO_PRIFLOW = 268435455
IPV6_FLOWINFO_SRFLAG = 268435456
IPV6_FLOWINFO_VERSION = 4026531840L
IPV6_PRIORITY_UNCHARACTERIZED = 0
IPV6_PRIORITY_FILLER = 16777216
IPV6_PRIORITY_UNATTENDED = 33554432
IPV6_PRIORITY_RESERVED1 = 50331648
IPV6_PRIORITY_BULK = 67108864
IPV6_PRIORITY_RESERVED2 = 83886080
IPV6_PRIORITY_INTERACTIVE = 100663296
IPV6_PRIORITY_CONTROL = 117440512
IPV6_PRIORITY_8 = 134217728
IPV6_PRIORITY_9 = 150994944
IPV6_PRIORITY_10 = 167772160
IPV6_PRIORITY_11 = 184549376
IPV6_PRIORITY_12 = 201326592
IPV6_PRIORITY_13 = 218103808
IPV6_PRIORITY_14 = 234881024
IPV6_PRIORITY_15 = 251658240
IPV6_SRFLAG_STRICT = 268435456
IPV6_SRFLAG_LOOSE = 0
IPV6_VERSION = 1610612736
IPV6_FLOWINFO_FLOWLABEL = 4294967040L
IPV6_FLOWINFO_PRIORITY = 15
IPV6_FLOWINFO_PRIFLOW = 4294967055L
IPV6_FLOWINFO_SRFLAG = 16
IPV6_FLOWINFO_VERSION = 240
IPV6_PRIORITY_UNCHARACTERIZED = 0
IPV6_PRIORITY_FILLER = 1
IPV6_PRIORITY_UNATTENDED = 2
IPV6_PRIORITY_RESERVED1 = 3
IPV6_PRIORITY_BULK = 4
IPV6_PRIORITY_RESERVED2 = 5
IPV6_PRIORITY_INTERACTIVE = 6
IPV6_PRIORITY_CONTROL = 7
IPV6_PRIORITY_8 = 8
IPV6_PRIORITY_9 = 9
IPV6_PRIORITY_10 = 10
IPV6_PRIORITY_11 = 11
IPV6_PRIORITY_12 = 12
IPV6_PRIORITY_13 = 13
IPV6_PRIORITY_14 = 14
IPV6_PRIORITY_15 = 15
IPV6_SRFLAG_STRICT = 16
IPV6_SRFLAG_LOOSE = 0
IPV6_VERSION = 96

def IPV6_GET_FLOWLABEL(x):
    return ntohl(x) & 16777215


def IPV6_GET_PRIORITY(x):
    return ntohl(x) >> 24 & 15


def IPV6_GET_VERSION(x):
    return ntohl(x) >> 28 & 15


def IPV6_SET_FLOWLABEL(x):
    return htonl(x) & IPV6_FLOWINFO_FLOWLABEL


def IPV6_SET_PRIORITY(x):
    return htonl((x & 15) << 24)


def CLR_ADDR6(a):
    pass


def IS_ANYSOCKADDR(a):
    pass


def IS_ANYADDR6(a):
    pass


def IS_COMPATSOCKADDR(a):
    pass


def IS_COMPATADDR6(a):
    pass


def IS_LOOPSOCKADDR(a):
    pass


def IS_LOOPADDR6(a):
    pass


def IS_IPV4SOCKADDR(a):
    pass


def IS_IPV4ADDR6(a):
    pass


def IS_LOOPSOCKADDR(a):
    pass


def IS_LOOPADDR6(a):
    pass


def IS_IPV4SOCKADDR(a):
    pass


def IS_IPV4ADDR6(a):
    pass


def IS_LOCALADDR6(a):
    return a.s6_addr8[0] == 254


def IS_LINKLADDR6(a):
    pass


def IS_SITELADDR6(a):
    pass


def IS_MULTIADDR6(a):
    return a.s6_addr8[0] == 255


def MADDR6_FLAGS(a):
    return a.s6_addr8[1] >> 4


MADDR6_FLG_WK = 0
MADDR6_FLG_TS = 1

def MADDR6_SCOPE(a):
    return a.s6_addr8[1] & 15


MADDR6_SCP_NODE = 1
MADDR6_SCP_LINK = 2
MADDR6_SCP_SITE = 5
MADDR6_SCP_ORG = 8
MADDR6_SCP_GLO = 14
MADDR6_ALLNODES = 1
MADDR6_ALLROUTERS = 2
MADDR6_ALLHOSTS = 3

def IN6_IS_ADDR_UNSPECIFIED(p):
    return IS_ANYADDR6(*p)


def IN6_IS_ADDR_LOOPBACK(p):
    return IS_LOOPADDR6(*p)


def IN6_IS_ADDR_MULTICAST(p):
    return IS_MULTIADDR6(*p)


def IN6_IS_ADDR_LINKLOCAL(p):
    return IS_LINKLADDR6(*p)


def IN6_IS_ADDR_SITELOCAL(p):
    return IS_SITELADDR6(*p)


def IN6_IS_ADDR_V4MAPPED(p):
    return IS_IPV4ADDR6(*p)


def IN6_IS_ADDR_V4COMPAT(p):
    return IS_COMPATADDR6(*p)


def IN6_IS_ADDR_MC_NODELOCAL(p):
    pass


def IN6_IS_ADDR_MC_LINKLOCAL(p):
    pass


def IN6_IS_ADDR_MC_SITELOCAL(p):
    pass


def IN6_IS_ADDR_MC_ORGLOCAL(p):
    pass


def IN6_IS_ADDR_MC_GLOBAL(p):
    pass


IP_OPTIONS = 1
IP_HDRINCL = 2
IP_TOS = 3
IP_TTL = 4
IP_RECVOPTS = 5
IP_RECVRETOPTS = 6
IP_RECVDSTADDR = 7
IP_RETOPTS = 8
IP_MULTICAST_IF = 20
IP_MULTICAST_TTL = 21
IP_MULTICAST_LOOP = 22
IP_ADD_MEMBERSHIP = 23
IP_DROP_MEMBERSHIP = 24
IP_MULTICAST_VIF = 25
IP_RSVP_VIF_ON = 26
IP_RSVP_VIF_OFF = 27
IP_RSVP_ON = 28
IP_SENDSRCADDR = 36
IPV6_UNICAST_HOPS = IP_TTL
IPV6_MULTICAST_IF = IP_MULTICAST_IF
IPV6_MULTICAST_HOPS = IP_MULTICAST_TTL
IPV6_MULTICAST_LOOP = IP_MULTICAST_LOOP
IPV6_ADD_MEMBERSHIP = IP_ADD_MEMBERSHIP
IPV6_DROP_MEMBERSHIP = IP_DROP_MEMBERSHIP
IPV6_SENDIF = 40
IPV6_NOPROBE = 42
IPV6_RECVPKTINFO = 43
IPV6_PKTINFO = 44
IP_RECVTTL = 45
IPV6_RECVHOPS = IP_RECVTTL
IPV6_CHECKSUM = 46
ICMP6_FILTER = 47
IPV6_HOPLIMIT = 48
IPV6_HOPOPTS = 49
IPV6_DSTOPTS = 50
IPV6_RTHDR = 51
IPV6_PKTOPTIONS = 52
IPV6_NEXTHOP = 53
IP_DEFAULT_MULTICAST_TTL = 1
IP_DEFAULT_MULTICAST_LOOP = 1
IPV6_RTHDR_LOOSE = 0
IPV6_RTHDR_STRICT = 1
IPV6_RTHDR_TYPE_0 = 0
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\plat-irix6\in.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 20:00:56 St�edn� Evropa (letn� �as)
