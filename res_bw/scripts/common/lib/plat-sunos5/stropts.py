# 2016.08.04 20:01:31 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/plat-sunos5/STROPTS.py
_CHAR_ALIGNMENT = 1
_SHORT_ALIGNMENT = 2
_INT_ALIGNMENT = 4
_LONG_ALIGNMENT = 8
_LONG_LONG_ALIGNMENT = 8
_DOUBLE_ALIGNMENT = 8
_LONG_DOUBLE_ALIGNMENT = 16
_POINTER_ALIGNMENT = 8
_MAX_ALIGNMENT = 16
_ALIGNMENT_REQUIRED = 1
_CHAR_ALIGNMENT = 1
_SHORT_ALIGNMENT = 2
_INT_ALIGNMENT = 4
_LONG_ALIGNMENT = 4
_LONG_LONG_ALIGNMENT = 4
_DOUBLE_ALIGNMENT = 4
_LONG_DOUBLE_ALIGNMENT = 4
_POINTER_ALIGNMENT = 4
_MAX_ALIGNMENT = 4
_ALIGNMENT_REQUIRED = 0
_CHAR_ALIGNMENT = 1
_SHORT_ALIGNMENT = 2
_INT_ALIGNMENT = 4
_LONG_LONG_ALIGNMENT = 8
_DOUBLE_ALIGNMENT = 8
_ALIGNMENT_REQUIRED = 1
_LONG_ALIGNMENT = 4
_LONG_DOUBLE_ALIGNMENT = 8
_POINTER_ALIGNMENT = 4
_MAX_ALIGNMENT = 8
_LONG_ALIGNMENT = 8
_LONG_DOUBLE_ALIGNMENT = 16
_POINTER_ALIGNMENT = 8
_MAX_ALIGNMENT = 16
_POSIX_C_SOURCE = 1
_LARGEFILE64_SOURCE = 1
_LARGEFILE_SOURCE = 1
_FILE_OFFSET_BITS = 64
_FILE_OFFSET_BITS = 32
_POSIX_C_SOURCE = 199506L
_POSIX_PTHREAD_SEMANTICS = 1
_XOPEN_VERSION = 500
_XOPEN_VERSION = 4
_XOPEN_VERSION = 3
from TYPES import *
from TYPES import *
LOCK_HELD_VALUE = 255

def SPIN_LOCK(pl):
    return pl > ipltospl(LOCK_LEVEL)


def LOCK_SAMPLE_INTERVAL(i):
    return i & 255 == 0


CLOCK_LEVEL = 10
LOCK_LEVEL = 10
DISP_LEVEL = LOCK_LEVEL + 1
PTR24_LSB = 5
PTR24_MSB = PTR24_LSB + 24
PTR24_ALIGN = 32
PTR24_BASE = 3758096384L
from TYPES import *
_POSIX_VDISABLE = 0
MAX_INPUT = 512
MAX_CANON = 256
UID_NOBODY = 60001
GID_NOBODY = UID_NOBODY
UID_NOACCESS = 60002
MAX_TASKID = 999999
MAX_MAXPID = 999999
DEFAULT_MAXPID = 999999
DEFAULT_JUMPPID = 100000
DEFAULT_MAXPID = 30000
DEFAULT_JUMPPID = 0
MAXUID = 2147483647
MAXPROJID = MAXUID
MAXLINK = 32767
NMOUNT = 40
CANBSIZ = 256
NOFILE = 20
NGROUPS_UMIN = 0
NGROUPS_UMAX = 32
NGROUPS_MAX_DEFAULT = 16
NZERO = 20
NULL = 0L
NULL = 0
CMASK = 18
CDLIMIT = 2048L
NBPS = 131072
NBPSCTR = 512
UBSIZE = 512
SCTRSHFT = 9
SYSNAME = 9
PREMOTE = 39
MAXPATHLEN = 1024
MAXSYMLINKS = 20
MAXNAMELEN = 256
NADDR = 13
PIPE_BUF = 5120
PIPE_MAX = 5120
NBBY = 8
MAXBSIZE = 8192
DEV_BSIZE = 512
DEV_BSHIFT = 9
MAXFRAG = 8
MAXOFF32_T = 2147483647
MAXOFF_T = 9223372036854775807L
MAXOFFSET_T = 9223372036854775807L
MAXOFF_T = 2147483647L
MAXOFFSET_T = 2147483647

def btodb(bytes):
    pass


def dbtob(db):
    pass


def lbtodb(bytes):
    pass


def ldbtob(db):
    pass


NCARGS32 = 1048576
NCARGS64 = 2097152
NCARGS = NCARGS64
NCARGS = NCARGS32
FSHIFT = 8
FSCALE = 1 << FSHIFT

def DELAY(n):
    return drv_usecwait(n)


def mmu_ptob(x):
    return x << MMU_PAGESHIFT


def mmu_btop(x):
    return x >> MMU_PAGESHIFT


def mmu_btopr(x):
    return x + MMU_PAGEOFFSET >> MMU_PAGESHIFT


def mmu_ptod(x):
    return x << MMU_PAGESHIFT - DEV_BSHIFT


def ptod(x):
    return x << PAGESHIFT - DEV_BSHIFT


def ptob(x):
    return x << PAGESHIFT


def btop(x):
    return x >> PAGESHIFT


def btopr(x):
    return x + PAGEOFFSET >> PAGESHIFT


def dtop(DD):
    return DD + NDPP - 1 >> PAGESHIFT - DEV_BSHIFT


def dtopt(DD):
    return DD >> PAGESHIFT - DEV_BSHIFT


_AIO_LISTIO_MAX = 4096
_AIO_MAX = -1
_MQ_OPEN_MAX = 32
_MQ_PRIO_MAX = 32
_SEM_NSEMS_MAX = INT_MAX
_SEM_VALUE_MAX = INT_MAX
_CS_PATH = 65
_CS_LFS_CFLAGS = 68
_CS_LFS_LDFLAGS = 69
_CS_LFS_LIBS = 70
_CS_LFS_LINTFLAGS = 71
_CS_LFS64_CFLAGS = 72
_CS_LFS64_LDFLAGS = 73
_CS_LFS64_LIBS = 74
_CS_LFS64_LINTFLAGS = 75
_CS_XBS5_ILP32_OFF32_CFLAGS = 700
_CS_XBS5_ILP32_OFF32_LDFLAGS = 701
_CS_XBS5_ILP32_OFF32_LIBS = 702
_CS_XBS5_ILP32_OFF32_LINTFLAGS = 703
_CS_XBS5_ILP32_OFFBIG_CFLAGS = 705
_CS_XBS5_ILP32_OFFBIG_LDFLAGS = 706
_CS_XBS5_ILP32_OFFBIG_LIBS = 707
_CS_XBS5_ILP32_OFFBIG_LINTFLAGS = 708
_CS_XBS5_LP64_OFF64_CFLAGS = 709
_CS_XBS5_LP64_OFF64_LDFLAGS = 710
_CS_XBS5_LP64_OFF64_LIBS = 711
_CS_XBS5_LP64_OFF64_LINTFLAGS = 712
_CS_XBS5_LPBIG_OFFBIG_CFLAGS = 713
_CS_XBS5_LPBIG_OFFBIG_LDFLAGS = 714
_CS_XBS5_LPBIG_OFFBIG_LIBS = 715
_CS_XBS5_LPBIG_OFFBIG_LINTFLAGS = 716
_SC_ARG_MAX = 1
_SC_CHILD_MAX = 2
_SC_CLK_TCK = 3
_SC_NGROUPS_MAX = 4
_SC_OPEN_MAX = 5
_SC_JOB_CONTROL = 6
_SC_SAVED_IDS = 7
_SC_VERSION = 8
_SC_PASS_MAX = 9
_SC_LOGNAME_MAX = 10
_SC_PAGESIZE = 11
_SC_XOPEN_VERSION = 12
_SC_NPROCESSORS_CONF = 14
_SC_NPROCESSORS_ONLN = 15
_SC_STREAM_MAX = 16
_SC_TZNAME_MAX = 17
_SC_AIO_LISTIO_MAX = 18
_SC_AIO_MAX = 19
_SC_AIO_PRIO_DELTA_MAX = 20
_SC_ASYNCHRONOUS_IO = 21
_SC_DELAYTIMER_MAX = 22
_SC_FSYNC = 23
_SC_MAPPED_FILES = 24
_SC_MEMLOCK = 25
_SC_MEMLOCK_RANGE = 26
_SC_MEMORY_PROTECTION = 27
_SC_MESSAGE_PASSING = 28
_SC_MQ_OPEN_MAX = 29
_SC_MQ_PRIO_MAX = 30
_SC_PRIORITIZED_IO = 31
_SC_PRIORITY_SCHEDULING = 32
_SC_REALTIME_SIGNALS = 33
_SC_RTSIG_MAX = 34
_SC_SEMAPHORES = 35
_SC_SEM_NSEMS_MAX = 36
_SC_SEM_VALUE_MAX = 37
_SC_SHARED_MEMORY_OBJECTS = 38
_SC_SIGQUEUE_MAX = 39
_SC_SIGRT_MIN = 40
_SC_SIGRT_MAX = 41
_SC_SYNCHRONIZED_IO = 42
_SC_TIMERS = 43
_SC_TIMER_MAX = 44
_SC_2_C_BIND = 45
_SC_2_C_DEV = 46
_SC_2_C_VERSION = 47
_SC_2_FORT_DEV = 48
_SC_2_FORT_RUN = 49
_SC_2_LOCALEDEF = 50
_SC_2_SW_DEV = 51
_SC_2_UPE = 52
_SC_2_VERSION = 53
_SC_BC_BASE_MAX = 54
_SC_BC_DIM_MAX = 55
_SC_BC_SCALE_MAX = 56
_SC_BC_STRING_MAX = 57
_SC_COLL_WEIGHTS_MAX = 58
_SC_EXPR_NEST_MAX = 59
_SC_LINE_MAX = 60
_SC_RE_DUP_MAX = 61
_SC_XOPEN_CRYPT = 62
_SC_XOPEN_ENH_I18N = 63
_SC_XOPEN_SHM = 64
_SC_2_CHAR_TERM = 66
_SC_XOPEN_XCU_VERSION = 67
_SC_ATEXIT_MAX = 76
_SC_IOV_MAX = 77
_SC_XOPEN_UNIX = 78
_SC_PAGE_SIZE = _SC_PAGESIZE
_SC_T_IOV_MAX = 79
_SC_PHYS_PAGES = 500
_SC_AVPHYS_PAGES = 501
_SC_COHER_BLKSZ = 503
_SC_SPLIT_CACHE = 504
_SC_ICACHE_SZ = 505
_SC_DCACHE_SZ = 506
_SC_ICACHE_LINESZ = 507
_SC_DCACHE_LINESZ = 508
_SC_ICACHE_BLKSZ = 509
_SC_DCACHE_BLKSZ = 510
_SC_DCACHE_TBLKSZ = 511
_SC_ICACHE_ASSOC = 512
_SC_DCACHE_ASSOC = 513
_SC_MAXPID = 514
_SC_STACK_PROT = 515
_SC_THREAD_DESTRUCTOR_ITERATIONS = 568
_SC_GETGR_R_SIZE_MAX = 569
_SC_GETPW_R_SIZE_MAX = 570
_SC_LOGIN_NAME_MAX = 571
_SC_THREAD_KEYS_MAX = 572
_SC_THREAD_STACK_MIN = 573
_SC_THREAD_THREADS_MAX = 574
_SC_TTY_NAME_MAX = 575
_SC_THREADS = 576
_SC_THREAD_ATTR_STACKADDR = 577
_SC_THREAD_ATTR_STACKSIZE = 578
_SC_THREAD_PRIORITY_SCHEDULING = 579
_SC_THREAD_PRIO_INHERIT = 580
_SC_THREAD_PRIO_PROTECT = 581
_SC_THREAD_PROCESS_SHARED = 582
_SC_THREAD_SAFE_FUNCTIONS = 583
_SC_XOPEN_LEGACY = 717
_SC_XOPEN_REALTIME = 718
_SC_XOPEN_REALTIME_THREADS = 719
_SC_XBS5_ILP32_OFF32 = 720
_SC_XBS5_ILP32_OFFBIG = 721
_SC_XBS5_LP64_OFF64 = 722
_SC_XBS5_LPBIG_OFFBIG = 723
_PC_LINK_MAX = 1
_PC_MAX_CANON = 2
_PC_MAX_INPUT = 3
_PC_NAME_MAX = 4
_PC_PATH_MAX = 5
_PC_PIPE_BUF = 6
_PC_NO_TRUNC = 7
_PC_VDISABLE = 8
_PC_CHOWN_RESTRICTED = 9
_PC_ASYNC_IO = 10
_PC_PRIO_IO = 11
_PC_SYNC_IO = 12
_PC_FILESIZEBITS = 67
_PC_LAST = 67
_POSIX_VERSION = 199506L
_POSIX2_VERSION = 199209L
_POSIX2_C_VERSION = 199209L
_XOPEN_XCU_VERSION = 4
_XOPEN_REALTIME = 1
_XOPEN_ENH_I18N = 1
_XOPEN_SHM = 1
_POSIX2_C_BIND = 1
_POSIX2_CHAR_TERM = 1
_POSIX2_LOCALEDEF = 1
_POSIX2_C_DEV = 1
_POSIX2_SW_DEV = 1
_POSIX2_UPE = 1
from TYPES import *

def MUTEX_HELD(x):
    return mutex_owned(x)


from TYPES import *

def RW_READ_HELD(x):
    return rw_read_held(x)


def RW_WRITE_HELD(x):
    return rw_write_held(x)


def RW_LOCK_HELD(x):
    return rw_lock_held(x)


def RW_ISWRITER(x):
    return rw_iswriter(x)


from TYPES import *
from TYPES import *
from TYPES import *
TIME32_MAX = INT32_MAX
TIME32_MIN = INT32_MIN

def TIMEVAL_OVERFLOW(tv):
    pass


from TYPES import *
DST_NONE = 0
DST_USA = 1
DST_AUST = 2
DST_WET = 3
DST_MET = 4
DST_EET = 5
DST_CAN = 6
DST_GB = 7
DST_RUM = 8
DST_TUR = 9
DST_AUSTALT = 10
ITIMER_REAL = 0
ITIMER_VIRTUAL = 1
ITIMER_PROF = 2
ITIMER_REALPROF = 3

def ITIMERVAL_OVERFLOW(itv):
    pass


SEC = 1
MILLISEC = 1000
MICROSEC = 1000000
NANOSEC = 1000000000

def TIMESPEC_OVERFLOW(ts):
    pass


def ITIMERSPEC_OVERFLOW(it):
    pass


__CLOCK_REALTIME0 = 0
CLOCK_VIRTUAL = 1
CLOCK_PROF = 2
__CLOCK_REALTIME3 = 3
CLOCK_HIGHRES = 4
CLOCK_MAX = 5
CLOCK_REALTIME = __CLOCK_REALTIME3
CLOCK_REALTIME = __CLOCK_REALTIME0
TIMER_RELTIME = 0
TIMER_ABSTIME = 1

def TICK_TO_SEC(tick):
    return tick / hz


def SEC_TO_TICK(sec):
    return sec * hz


def TICK_TO_MSEC(tick):
    pass


def MSEC_TO_TICK(msec):
    pass


def MSEC_TO_TICK_ROUNDUP(msec):
    pass


def TICK_TO_USEC(tick):
    return tick * usec_per_tick


def USEC_TO_TICK(usec):
    return usec / usec_per_tick


def USEC_TO_TICK_ROUNDUP(usec):
    pass


def TICK_TO_NSEC(tick):
    return tick * nsec_per_tick


def NSEC_TO_TICK(nsec):
    return nsec / nsec_per_tick


def NSEC_TO_TICK_ROUNDUP(nsec):
    pass


def TIMEVAL_TO_TICK(tvp):
    pass


def TIMESTRUC_TO_TICK(tsp):
    pass


from TYPES import *
NULL = 0L
NULL = 0
CLOCKS_PER_SEC = 1000000
FD_SETSIZE = 65536
FD_SETSIZE = 1024
_NBBY = 8
NBBY = _NBBY

def FD_ZERO(p):
    return bzero(p, sizeof(*p))


SIGHUP = 1
SIGINT = 2
SIGQUIT = 3
SIGILL = 4
SIGTRAP = 5
SIGIOT = 6
SIGABRT = 6
SIGEMT = 7
SIGFPE = 8
SIGKILL = 9
SIGBUS = 10
SIGSEGV = 11
SIGSYS = 12
SIGPIPE = 13
SIGALRM = 14
SIGTERM = 15
SIGUSR1 = 16
SIGUSR2 = 17
SIGCLD = 18
SIGCHLD = 18
SIGPWR = 19
SIGWINCH = 20
SIGURG = 21
SIGPOLL = 22
SIGIO = SIGPOLL
SIGSTOP = 23
SIGTSTP = 24
SIGCONT = 25
SIGTTIN = 26
SIGTTOU = 27
SIGVTALRM = 28
SIGPROF = 29
SIGXCPU = 30
SIGXFSZ = 31
SIGWAITING = 32
SIGLWP = 33
SIGFREEZE = 34
SIGTHAW = 35
SIGCANCEL = 36
SIGLOST = 37
_SIGRTMIN = 38
_SIGRTMAX = 45
SIG_BLOCK = 1
SIG_UNBLOCK = 2
SIG_SETMASK = 3
SIGNO_MASK = 255
SIGDEFER = 256
SIGHOLD = 512
SIGRELSE = 1024
SIGIGNORE = 2048
SIGPAUSE = 4096
from TYPES import *
SIGEV_NONE = 1
SIGEV_SIGNAL = 2
SIGEV_THREAD = 3
SI_NOINFO = 32767
SI_USER = 0
SI_LWP = -1
SI_QUEUE = -2
SI_TIMER = -3
SI_ASYNCIO = -4
SI_MESGQ = -5
ILL_ILLOPC = 1
ILL_ILLOPN = 2
ILL_ILLADR = 3
ILL_ILLTRP = 4
ILL_PRVOPC = 5
ILL_PRVREG = 6
ILL_COPROC = 7
ILL_BADSTK = 8
NSIGILL = 8
EMT_TAGOVF = 1
EMT_CPCOVF = 2
NSIGEMT = 2
FPE_INTDIV = 1
FPE_INTOVF = 2
FPE_FLTDIV = 3
FPE_FLTOVF = 4
FPE_FLTUND = 5
FPE_FLTRES = 6
FPE_FLTINV = 7
FPE_FLTSUB = 8
NSIGFPE = 8
SEGV_MAPERR = 1
SEGV_ACCERR = 2
NSIGSEGV = 2
BUS_ADRALN = 1
BUS_ADRERR = 2
BUS_OBJERR = 3
NSIGBUS = 3
TRAP_BRKPT = 1
TRAP_TRACE = 2
TRAP_RWATCH = 3
TRAP_WWATCH = 4
TRAP_XWATCH = 5
NSIGTRAP = 5
CLD_EXITED = 1
CLD_KILLED = 2
CLD_DUMPED = 3
CLD_TRAPPED = 4
CLD_STOPPED = 5
CLD_CONTINUED = 6
NSIGCLD = 6
POLL_IN = 1
POLL_OUT = 2
POLL_MSG = 3
POLL_ERR = 4
POLL_PRI = 5
POLL_HUP = 6
NSIGPOLL = 6
PROF_SIG = 1
NSIGPROF = 1
SI_MAXSZ = 256
SI_MAXSZ = 128
from TYPES import *
SI32_MAXSZ = 128

def SI_CANQUEUE(c):
    return c <= SI_QUEUE


SA_NOCLDSTOP = 131072
SA_ONSTACK = 1
SA_RESETHAND = 2
SA_RESTART = 4
SA_SIGINFO = 8
SA_NODEFER = 16
SA_NOCLDWAIT = 65536
SA_WAITSIG = 65536
NSIG = 46
MAXSIG = 45
S_SIGNAL = 1
S_SIGSET = 2
S_SIGACTION = 3
S_NONE = 4
MINSIGSTKSZ = 2048
SIGSTKSZ = 8192
SS_ONSTACK = 1
SS_DISABLE = 2
SN_PROC = 1
SN_CANCEL = 2
SN_SEND = 3
from TYPES import *
REG_CCR = 0
REG_PSR = 0
REG_PSR = 0
REG_PC = 1
REG_nPC = 2
REG_Y = 3
REG_G1 = 4
REG_G2 = 5
REG_G3 = 6
REG_G4 = 7
REG_G5 = 8
REG_G6 = 9
REG_G7 = 10
REG_O0 = 11
REG_O1 = 12
REG_O2 = 13
REG_O3 = 14
REG_O4 = 15
REG_O5 = 16
REG_O6 = 17
REG_O7 = 18
REG_ASI = 19
REG_FPRS = 20
REG_PS = REG_PSR
REG_SP = REG_O6
REG_R0 = REG_O0
REG_R1 = REG_O1
_NGREG = 21
_NGREG = 19
NGREG = _NGREG
_NGREG32 = 19
_NGREG64 = 21
SPARC_MAXREGWINDOW = 31
MAXFPQ = 16
XRS_ID = 2020766464
PSR_CWP = 31
PSR_ET = 32
PSR_PS = 64
PSR_S = 128
PSR_PIL = 3840
PSR_EF = 4096
PSR_EC = 8192
PSR_RSV = 1032192
PSR_ICC = 15728640
PSR_C = 1048576
PSR_V = 2097152
PSR_Z = 4194304
PSR_N = 8388608
PSR_VER = 251658240
PSR_IMPL = 4026531840L
PSL_ALLCC = PSR_ICC
PSL_USER = PSR_S
PSL_USERMASK = PSR_ICC
PSL_UBITS = PSR_ICC | PSR_EF

def USERMODE(ps):
    return ps & PSR_PS == 0


FSR_CEXC = 31
FSR_AEXC = 992
FSR_FCC = 3072
FSR_PR = 4096
FSR_QNE = 8192
FSR_FTT = 114688
FSR_VER = 917504
FSR_TEM = 260046848
FSR_RP = 805306368
FSR_RD = 3221225472L
FSR_VER_SHIFT = 17
FSR_FCC1 = 3
FSR_FCC2 = 12
FSR_FCC3 = 48
FSR_CEXC_NX = 1
FSR_CEXC_DZ = 2
FSR_CEXC_UF = 4
FSR_CEXC_OF = 8
FSR_CEXC_NV = 16
FSR_AEXC_NX = 32
FSR_AEXC_DZ = 64
FSR_AEXC_UF = 128
FSR_AEXC_OF = 256
FSR_AEXC_NV = 512
FTT_NONE = 0
FTT_IEEE = 1
FTT_UNFIN = 2
FTT_UNIMP = 3
FTT_SEQ = 4
FTT_ALIGN = 5
FTT_DFAULT = 6
FSR_FTT_SHIFT = 14
FSR_FTT_IEEE = FTT_IEEE << FSR_FTT_SHIFT
FSR_FTT_UNFIN = FTT_UNFIN << FSR_FTT_SHIFT
FSR_FTT_UNIMP = FTT_UNIMP << FSR_FTT_SHIFT
FSR_FTT_SEQ = FTT_SEQ << FSR_FTT_SHIFT
FSR_FTT_ALIGN = FTT_ALIGN << FSR_FTT_SHIFT
FSR_FTT_DFAULT = FTT_DFAULT << FSR_FTT_SHIFT
FSR_TEM_NX = 8388608
FSR_TEM_DZ = 16777216
FSR_TEM_UF = 33554432
FSR_TEM_OF = 67108864
FSR_TEM_NV = 134217728
RP_DBLEXT = 0
RP_SINGLE = 1
RP_DOUBLE = 2
RP_RESERVED = 3
RD_NEAR = 0
RD_ZER0 = 1
RD_POSINF = 2
RD_NEGINF = 3
FPRS_DL = 1
FPRS_DU = 2
FPRS_FEF = 4
PIL_MAX = 15

def SAVE_GLOBALS(RP):
    pass


def RESTORE_GLOBALS(RP):
    pass


def SAVE_OUTS(RP):
    pass


def RESTORE_OUTS(RP):
    pass


def SAVE_WINDOW(SBP):
    pass


def RESTORE_WINDOW(SBP):
    pass


def STORE_FPREGS(FP):
    pass


def LOAD_FPREGS(FP):
    pass


_SPARC_MAXREGWINDOW = 31
_XRS_ID = 2020766464
GETCONTEXT = 0
SETCONTEXT = 1
UC_SIGMASK = 1
UC_STACK = 2
UC_CPU = 4
UC_MAU = 8
UC_FPU = UC_MAU
UC_INTR = 16
UC_ASR = 32
UC_MCONTEXT = UC_CPU | UC_FPU | UC_ASR
UC_ALL = UC_SIGMASK | UC_STACK | UC_MCONTEXT
_SIGQUEUE_MAX = 32
_SIGNOTIFY_MAX = 32
INSTR_VALID = 2
NORMAL_STEP = 4
WATCH_STEP = 8
CPC_OVERFLOW = 16
ASYNC_HWERR = 32
STEP_NONE = 0
STEP_REQUESTED = 1
STEP_ACTIVE = 2
STEP_WASACTIVE = 3
LMS_USER = 0
LMS_SYSTEM = 1
LMS_TRAP = 2
LMS_TFAULT = 3
LMS_DFAULT = 4
LMS_KFAULT = 5
LMS_USER_LOCK = 6
LMS_SLEEP = 7
LMS_WAIT_CPU = 8
LMS_STOPPED = 9
NMSTATES = 10
from TYPES import *
USYNC_THREAD = 0
USYNC_PROCESS = 1
LOCK_NORMAL = 0
LOCK_ERRORCHECK = 2
LOCK_RECURSIVE = 4
USYNC_PROCESS_ROBUST = 8
LOCK_PRIO_NONE = 0
LOCK_PRIO_INHERIT = 16
LOCK_PRIO_PROTECT = 32
LOCK_STALL_NP = 0
LOCK_ROBUST_NP = 64
LOCK_OWNERDEAD = 1
LOCK_NOTRECOVERABLE = 2
LOCK_INITED = 4
LOCK_UNMAPPED = 8
LWP_DETACHED = 64
LWP_SUSPENDED = 128
__LWP_ASLWP = 256
MAXSYSARGS = 8
NORMALRETURN = 0
JUSTRETURN = 1
LWP_USER = 1
LWP_SYS = 2
TS_FREE = 0
TS_SLEEP = 1
TS_RUN = 2
TS_ONPROC = 4
TS_ZOMB = 8
TS_STOPPED = 16
T_INTR_THREAD = 1
T_WAKEABLE = 2
T_TOMASK = 4
T_TALLOCSTK = 8
T_WOULDBLOCK = 32
T_DONTBLOCK = 64
T_DONTPEND = 128
T_SYS_PROF = 256
T_WAITCVSEM = 512
T_WATCHPT = 1024
T_PANIC = 2048
TP_HOLDLWP = 2
TP_TWAIT = 4
TP_LWPEXIT = 8
TP_PRSTOP = 16
TP_CHKPT = 32
TP_EXITLWP = 64
TP_PRVSTOP = 128
TP_MSACCT = 256
TP_STOPPING = 512
TP_WATCHPT = 1024
TP_PAUSE = 2048
TP_CHANGEBIND = 4096
TS_LOAD = 1
TS_DONT_SWAP = 2
TS_SWAPENQ = 4
TS_ON_SWAPQ = 8
TS_CSTART = 256
TS_UNPAUSE = 512
TS_XSTART = 1024
TS_PSTART = 2048
TS_RESUME = 4096
TS_CREATE = 8192
TS_ALLSTART = TS_CSTART | TS_UNPAUSE | TS_XSTART | TS_PSTART | TS_RESUME | TS_CREATE

def CPR_VSTOPPED(t):
    pass


def THREAD_TRANSITION(tp):
    return thread_transition(tp)


def THREAD_STOP(tp):
    pass


def THREAD_ZOMB(tp):
    return THREAD_SET_STATE(tp, TS_ZOMB, NULL)


def SEMA_HELD(x):
    return sema_held(x)


NO_LOCKS_HELD = 1
NO_COMPETING_THREADS = 1
FMNAMESZ = 8
from TYPES import *
from TYPES import *
from TYPES import *
PRIO_PROCESS = 0
PRIO_PGRP = 1
PRIO_USER = 2
RLIMIT_CPU = 0
RLIMIT_FSIZE = 1
RLIMIT_DATA = 2
RLIMIT_STACK = 3
RLIMIT_CORE = 4
RLIMIT_NOFILE = 5
RLIMIT_VMEM = 6
RLIMIT_AS = RLIMIT_VMEM
RLIM_NLIMITS = 7
RLIM_INFINITY = -3L
RLIM_SAVED_MAX = -2L
RLIM_SAVED_CUR = -1L
RLIM_INFINITY = 2147483647
RLIM_SAVED_MAX = 2147483646
RLIM_SAVED_CUR = 2147483645
RLIM32_INFINITY = 2147483647
RLIM32_SAVED_MAX = 2147483646
RLIM32_SAVED_CUR = 2147483645

def ASSERT64(x):
    return ASSERT(x)


def ASSERT32(x):
    return ASSERT(x)


DATAMODEL_MASK = 267386880
DATAMODEL_ILP32 = 1048576
DATAMODEL_LP64 = 2097152
DATAMODEL_NONE = 0
DATAMODEL_NATIVE = DATAMODEL_LP64
DATAMODEL_NATIVE = DATAMODEL_ILP32

def STRUCT_SIZE(handle):
    pass


def STRUCT_BUF(handle):
    return handle.ptr.m64


def SIZEOF_PTR(umodel):
    pass


def STRUCT_SIZE(handle):
    return sizeof(*handle.ptr)


def STRUCT_BUF(handle):
    return handle.ptr


def SIZEOF_PTR(umodel):
    return sizeof(caddr_t)


def lwp_getdatamodel(t):
    return DATAMODEL_ILP32


RUSAGE_SELF = 0
RUSAGE_CHILDREN = -1
AT_NULL = 0
AT_IGNORE = 1
AT_EXECFD = 2
AT_PHDR = 3
AT_PHENT = 4
AT_PHNUM = 5
AT_PAGESZ = 6
AT_BASE = 7
AT_FLAGS = 8
AT_ENTRY = 9
AT_DCACHEBSIZE = 10
AT_ICACHEBSIZE = 11
AT_UCACHEBSIZE = 12
AT_SUN_UID = 2000
AT_SUN_RUID = 2001
AT_SUN_GID = 2002
AT_SUN_RGID = 2003
AT_SUN_LDELF = 2004
AT_SUN_LDSHDR = 2005
AT_SUN_LDNAME = 2006
AT_SUN_LPAGESZ = 2007
AT_SUN_PLATFORM = 2008
AT_SUN_HWCAP = 2009
AT_SUN_IFLUSH = 2010
AT_SUN_CPU = 2011
AT_SUN_EMUL_ENTRY = 2012
AT_SUN_EMUL_EXECFD = 2013
AT_SUN_EXECNAME = 2014
AT_SUN_MMU = 2015
EPERM = 1
ENOENT = 2
ESRCH = 3
EINTR = 4
EIO = 5
ENXIO = 6
E2BIG = 7
ENOEXEC = 8
EBADF = 9
ECHILD = 10
EAGAIN = 11
ENOMEM = 12
EACCES = 13
EFAULT = 14
ENOTBLK = 15
EBUSY = 16
EEXIST = 17
EXDEV = 18
ENODEV = 19
ENOTDIR = 20
EISDIR = 21
EINVAL = 22
ENFILE = 23
EMFILE = 24
ENOTTY = 25
ETXTBSY = 26
EFBIG = 27
ENOSPC = 28
ESPIPE = 29
EROFS = 30
EMLINK = 31
EPIPE = 32
EDOM = 33
ERANGE = 34
ENOMSG = 35
EIDRM = 36
ECHRNG = 37
EL2NSYNC = 38
EL3HLT = 39
EL3RST = 40
ELNRNG = 41
EUNATCH = 42
ENOCSI = 43
EL2HLT = 44
EDEADLK = 45
ENOLCK = 46
ECANCELED = 47
ENOTSUP = 48
EDQUOT = 49
EBADE = 50
EBADR = 51
EXFULL = 52
ENOANO = 53
EBADRQC = 54
EBADSLT = 55
EDEADLOCK = 56
EBFONT = 57
EOWNERDEAD = 58
ENOTRECOVERABLE = 59
ENOSTR = 60
ENODATA = 61
ETIME = 62
ENOSR = 63
ENONET = 64
ENOPKG = 65
EREMOTE = 66
ENOLINK = 67
EADV = 68
ESRMNT = 69
ECOMM = 70
EPROTO = 71
ELOCKUNMAPPED = 72
ENOTACTIVE = 73
EMULTIHOP = 74
EBADMSG = 77
ENAMETOOLONG = 78
EOVERFLOW = 79
ENOTUNIQ = 80
EBADFD = 81
EREMCHG = 82
ELIBACC = 83
ELIBBAD = 84
ELIBSCN = 85
ELIBMAX = 86
ELIBEXEC = 87
EILSEQ = 88
ENOSYS = 89
ELOOP = 90
ERESTART = 91
ESTRPIPE = 92
ENOTEMPTY = 93
EUSERS = 94
ENOTSOCK = 95
EDESTADDRREQ = 96
EMSGSIZE = 97
EPROTOTYPE = 98
ENOPROTOOPT = 99
EPROTONOSUPPORT = 120
ESOCKTNOSUPPORT = 121
EOPNOTSUPP = 122
EPFNOSUPPORT = 123
EAFNOSUPPORT = 124
EADDRINUSE = 125
EADDRNOTAVAIL = 126
ENETDOWN = 127
ENETUNREACH = 128
ENETRESET = 129
ECONNABORTED = 130
ECONNRESET = 131
ENOBUFS = 132
EISCONN = 133
ENOTCONN = 134
ESHUTDOWN = 143
ETOOMANYREFS = 144
ETIMEDOUT = 145
ECONNREFUSED = 146
EHOSTDOWN = 147
EHOSTUNREACH = 148
EWOULDBLOCK = EAGAIN
EALREADY = 149
EINPROGRESS = 150
ESTALE = 151
PSARGSZ = 80
PSCOMSIZ = 14
MAXCOMLEN = 16
__KERN_NAUXV_IMPL = 19
__KERN_NAUXV_IMPL = 21
__KERN_NAUXV_IMPL = 21
PSARGSZ = 80
from TYPES import *
from TYPES import *
from TYPES import *
KSTAT_STRLEN = 31

def KSTAT_ENTER(k):
    pass


def KSTAT_EXIT(k):
    pass


KSTAT_TYPE_RAW = 0
KSTAT_TYPE_NAMED = 1
KSTAT_TYPE_INTR = 2
KSTAT_TYPE_IO = 3
KSTAT_TYPE_TIMER = 4
KSTAT_NUM_TYPES = 5
KSTAT_FLAG_VIRTUAL = 1
KSTAT_FLAG_VAR_SIZE = 2
KSTAT_FLAG_WRITABLE = 4
KSTAT_FLAG_PERSISTENT = 8
KSTAT_FLAG_DORMANT = 16
KSTAT_FLAG_INVALID = 32
KSTAT_READ = 0
KSTAT_WRITE = 1
KSTAT_DATA_CHAR = 0
KSTAT_DATA_INT32 = 1
KSTAT_DATA_UINT32 = 2
KSTAT_DATA_INT64 = 3
KSTAT_DATA_UINT64 = 4
KSTAT_DATA_LONG = KSTAT_DATA_INT32
KSTAT_DATA_ULONG = KSTAT_DATA_UINT32
KSTAT_DATA_LONG = KSTAT_DATA_INT64
KSTAT_DATA_ULONG = KSTAT_DATA_UINT64
KSTAT_DATA_LONG = 7
KSTAT_DATA_ULONG = 8
KSTAT_DATA_LONGLONG = KSTAT_DATA_INT64
KSTAT_DATA_ULONGLONG = KSTAT_DATA_UINT64
KSTAT_DATA_FLOAT = 5
KSTAT_DATA_DOUBLE = 6
KSTAT_INTR_HARD = 0
KSTAT_INTR_SOFT = 1
KSTAT_INTR_WATCHDOG = 2
KSTAT_INTR_SPURIOUS = 3
KSTAT_INTR_MULTSVC = 4
KSTAT_NUM_INTRS = 5
B_BUSY = 1
B_DONE = 2
B_ERROR = 4
B_PAGEIO = 16
B_PHYS = 32
B_READ = 64
B_WRITE = 256
B_KERNBUF = 8
B_WANTED = 128
B_AGE = 512
B_ASYNC = 1024
B_DELWRI = 2048
B_STALE = 4096
B_DONTNEED = 8192
B_REMAPPED = 16384
B_FREE = 32768
B_INVAL = 65536
B_FORCE = 131072
B_HEAD = 262144
B_NOCACHE = 524288
B_TRUNC = 1048576
B_SHADOW = 2097152
B_RETRYWRI = 4194304

def notavail(bp):
    pass


def BWRITE(bp):
    pass


def BWRITE2(bp):
    pass


from TYPES import *
WP_NOWATCH = 1
WP_SETPROT = 2
from TYPES import *
_TIMER_MAX = 32
ITLK_LOCKED = 1
ITLK_WANTED = 2
ITLK_REMOVE = 4
IT_PERLWP = 1
IT_SIGNAL = 2
UT_INSTRUCTION_DISABLED = 1
UT_INSTRUCTION_ERROR = 2
UT_INSTRUCTION_PROTECTION = 3
UT_ILLTRAP_INSTRUCTION = 4
UT_ILLEGAL_INSTRUCTION = 5
UT_PRIVILEGED_OPCODE = 6
UT_FP_DISABLED = 7
UT_FP_EXCEPTION_IEEE_754 = 8
UT_FP_EXCEPTION_OTHER = 9
UT_TAG_OVERFLOW = 10
UT_DIVISION_BY_ZERO = 11
UT_DATA_EXCEPTION = 12
UT_DATA_ERROR = 13
UT_DATA_PROTECTION = 14
UT_MEM_ADDRESS_NOT_ALIGNED = 15
UT_PRIVILEGED_ACTION = 16
UT_ASYNC_DATA_ERROR = 17
UT_TRAP_INSTRUCTION_16 = 18
UT_TRAP_INSTRUCTION_17 = 19
UT_TRAP_INSTRUCTION_18 = 20
UT_TRAP_INSTRUCTION_19 = 21
UT_TRAP_INSTRUCTION_20 = 22
UT_TRAP_INSTRUCTION_21 = 23
UT_TRAP_INSTRUCTION_22 = 24
UT_TRAP_INSTRUCTION_23 = 25
UT_TRAP_INSTRUCTION_24 = 26
UT_TRAP_INSTRUCTION_25 = 27
UT_TRAP_INSTRUCTION_26 = 28
UT_TRAP_INSTRUCTION_27 = 29
UT_TRAP_INSTRUCTION_28 = 30
UT_TRAP_INSTRUCTION_29 = 31
UT_TRAP_INSTRUCTION_30 = 32
UT_TRAP_INSTRUCTION_31 = 33
UTRAP_V8P_FP_DISABLED = UT_FP_DISABLED
UTRAP_V8P_MEM_ADDRESS_NOT_ALIGNED = UT_MEM_ADDRESS_NOT_ALIGNED
UT_PRECISE_MAXTRAPS = 33
from TYPES import *
TASK_NORMAL = 0
TASK_FINAL = 1
TASK_FINALITY = 1
from TYPES import *
from TYPES import *
VM_SLEEP = 0
VM_NOSLEEP = 1
VM_PANIC = 2
VM_KMFLAGS = 255
VM_BESTFIT = 256
VMEM_ALLOC = 1
VMEM_FREE = 2
VMEM_SPAN = 16
ISP_NORMAL = 0
ISP_RESERVE = 1
from TYPES import *
from TYPES import *
KM_SLEEP = 0
KM_NOSLEEP = 1
KM_PANIC = 2
KM_VMFLAGS = 255
KM_FLAGS = 65535
KMC_NOTOUCH = 65536
KMC_NODEBUG = 131072
KMC_NOMAGAZINE = 262144
KMC_NOHASH = 524288
KMC_QCACHE = 1048576
_ISA_IA32 = 0
_ISA_IA64 = 1
SSLEEP = 1
SRUN = 2
SZOMB = 3
SSTOP = 4
SIDL = 5
SONPROC = 6
CLDPEND = 1
CLDCONT = 2
SSYS = 1
STRC = 2
SLOAD = 8
SLOCK = 16
SPREXEC = 32
SPROCTR = 64
SPRFORK = 128
SKILLED = 256
SULOAD = 512
SRUNLCL = 1024
SBPTADJ = 2048
SKILLCL = 4096
SOWEUPC = 8192
SEXECED = 16384
SPASYNC = 32768
SJCTL = 65536
SNOWAIT = 131072
SVFORK = 262144
SVFWAIT = 524288
EXITLWPS = 1048576
HOLDFORK = 2097152
SWAITSIG = 4194304
HOLDFORK1 = 8388608
COREDUMP = 16777216
SMSACCT = 33554432
ASLWP = 67108864
SPRLOCK = 134217728
NOCD = 268435456
HOLDWATCH = 536870912
SMSFORK = 1073741824
SDOCORE = 2147483648L
FORREAL = 0
JUSTLOOKING = 1
SUSPEND_NORMAL = 0
SUSPEND_PAUSE = 1
NOCLASS = -1
DDI_DEVICE_ATTR_V0 = 1
DDI_NEVERSWAP_ACC = 0
DDI_STRUCTURE_LE_ACC = 1
DDI_STRUCTURE_BE_ACC = 2
DDI_STRICTORDER_ACC = 0
DDI_UNORDERED_OK_ACC = 1
DDI_MERGING_OK_ACC = 2
DDI_LOADCACHING_OK_ACC = 3
DDI_STORECACHING_OK_ACC = 4
DDI_DATA_SZ01_ACC = 1
DDI_DATA_SZ02_ACC = 2
DDI_DATA_SZ04_ACC = 4
DDI_DATA_SZ08_ACC = 8
VERS_ACCHDL = 1
DEVID_NONE = 0
DEVID_SCSI3_WWN = 1
DEVID_SCSI_SERIAL = 2
DEVID_FAB = 3
DEVID_ENCAP = 4
DEVID_MAXTYPE = 4
VA_ALIGN = 8

def _ARGSIZEOF(t):
    return sizeof(t) + VA_ALIGN - 1 & ~(VA_ALIGN - 1)


VA_ALIGN = 8

def _ARGSIZEOF(t):
    return sizeof(t) + VA_ALIGN - 1 & ~(VA_ALIGN - 1)


NSYSCALL = 256
SE_32RVAL1 = 0
SE_32RVAL2 = 1
SE_64RVAL = 2
SE_RVAL_MASK = 3
SE_LOADABLE = 8
SE_LOADED = 16
SE_NOUNLOAD = 32
SE_ARGC = 64
from TYPES import *
POLLIN = 1
POLLPRI = 2
POLLOUT = 4
POLLRDNORM = 64
POLLWRNORM = POLLOUT
POLLRDBAND = 128
POLLWRBAND = 256
POLLNORM = POLLRDNORM
POLLERR = 8
POLLHUP = 16
POLLNVAL = 32
POLLREMOVE = 2048
POLLRDDATA = 512
POLLNOERR = 1024
POLLCLOSED = 32768
from TYPES import *
VROOT = 1
VNOCACHE = 2
VNOMAP = 4
VDUP = 8
VNOSWAP = 16
VNOMOUNT = 32
VISSWAP = 64
VSWAPLIKE = 128
VVFSLOCK = 256
VVFSWAIT = 512
VVMLOCK = 1024
VDIROPEN = 2048
VVMEXEC = 4096
VPXFS = 8192
AT_TYPE = 1
AT_MODE = 2
AT_UID = 4
AT_GID = 8
AT_FSID = 16
AT_NODEID = 32
AT_NLINK = 64
AT_SIZE = 128
AT_ATIME = 256
AT_MTIME = 512
AT_CTIME = 1024
AT_RDEV = 2048
AT_BLKSIZE = 4096
AT_NBLOCKS = 8192
AT_VCODE = 16384
AT_ALL = AT_TYPE | AT_MODE | AT_UID | AT_GID | AT_FSID | AT_NODEID | AT_NLINK | AT_SIZE | AT_ATIME | AT_MTIME | AT_CTIME | AT_RDEV | AT_BLKSIZE | AT_NBLOCKS | AT_VCODE
AT_STAT = AT_MODE | AT_UID | AT_GID | AT_FSID | AT_NODEID | AT_NLINK | AT_SIZE | AT_ATIME | AT_MTIME | AT_CTIME | AT_RDEV
AT_TIMES = AT_ATIME | AT_MTIME | AT_CTIME
AT_NOSET = AT_NLINK | AT_RDEV | AT_FSID | AT_NODEID | AT_TYPE | AT_BLKSIZE | AT_NBLOCKS | AT_VCODE
VSUID = 2048
VSGID = 1024
VSVTX = 512
VREAD = 256
VWRITE = 128
VEXEC = 64
MODEMASK = 4095
PERMMASK = 511

def MANDMODE(mode):
    return mode & (VSGID | VEXEC >> 3) == VSGID


VSA_ACL = 1
VSA_ACLCNT = 2
VSA_DFACL = 4
VSA_DFACLCNT = 8
LOOKUP_DIR = 1
DUMP_ALLOC = 0
DUMP_FREE = 1
DUMP_SCAN = 2
ATTR_UTIME = 1
ATTR_EXEC = 2
ATTR_COMM = 4
ATTR_HINT = 8
ATTR_REAL = 16
FC_HWERR = 1
FC_ALIGN = 2
FC_OBJERR = 3
FC_PROT = 4
FC_NOMAP = 5
FC_NOSUPPORT = 6

def FC_MAKE_ERR(e):
    return e << 8 | FC_OBJERR


def FC_CODE(fc):
    return fc & 255


def FC_ERRNO(fc):
    return unsigned(fc) >> 8


from TYPES import *
PAGE_HASHAVELEN = 4
PAGE_HASHVPSHIFT = 6
PG_EXCL = 1
PG_WAIT = 2
PG_PHYSCONTIG = 4
PG_MATCH_COLOR = 8
PG_NORELOC = 16
PG_FREE_LIST = 1
PG_CACHE_LIST = 2
PG_LIST_TAIL = 0
PG_LIST_HEAD = 1

def page_next_raw(PP):
    return page_nextn_raw(PP, 1)


PAGE_IO_INUSE = 1
PAGE_IO_WANTED = 2
PGREL_NOTREL = 1
PGREL_CLEAN = 2
PGREL_MOD = 3
P_FREE = 128
P_NORELOC = 64

def PP_SETAGED(pp):
    return ASSERT(PP_ISAGED(pp))


HAT_FLAGS_RESV = 4278190080L
HAT_LOAD = 0
HAT_LOAD_LOCK = 1
HAT_LOAD_ADV = 4
HAT_LOAD_CONTIG = 16
HAT_LOAD_NOCONSIST = 32
HAT_LOAD_SHARE = 64
HAT_LOAD_REMAP = 128
HAT_RELOAD_SHARE = 256
HAT_PLAT_ATTR_MASK = 15728640
HAT_PROT_MASK = 15
HAT_NOFAULT = 16
HAT_NOSYNC = 32
HAT_STRICTORDER = 0
HAT_UNORDERED_OK = 256
HAT_MERGING_OK = 512
HAT_LOADCACHING_OK = 768
HAT_STORECACHING_OK = 1024
HAT_ORDER_MASK = 1792
HAT_NEVERSWAP = 0
HAT_STRUCTURE_BE = 4096
HAT_STRUCTURE_LE = 8192
HAT_ENDIAN_MASK = 12288
HAT_COW = 1
HAT_UNLOAD = 0
HAT_UNLOAD_NOSYNC = 2
HAT_UNLOAD_UNLOCK = 4
HAT_UNLOAD_OTHER = 8
HAT_UNLOAD_UNMAP = 16
HAT_SYNC_DONTZERO = 0
HAT_SYNC_ZERORM = 1
HAT_SYNC_STOPON_REF = 2
HAT_SYNC_STOPON_MOD = 4
HAT_SYNC_STOPON_RM = HAT_SYNC_STOPON_REF | HAT_SYNC_STOPON_MOD
HAT_DUP_ALL = 1
HAT_DUP_COW = 2
HAT_MAP = 0
HAT_ADV_PGUNLOAD = 0
HAT_FORCE_PGUNLOAD = 1
P_MOD = 1
P_REF = 2
P_RO = 4

def hat_ismod(pp):
    return hat_page_getattr(pp, P_MOD)


def hat_isref(pp):
    return hat_page_getattr(pp, P_REF)


def hat_isro(pp):
    return hat_page_getattr(pp, P_RO)


def hat_setmod(pp):
    return hat_page_setattr(pp, P_MOD)


def hat_setref(pp):
    return hat_page_setattr(pp, P_REF)


def hat_setrefmod(pp):
    return hat_page_setattr(pp, P_REF | P_MOD)


def hat_clrmod(pp):
    return hat_page_clrattr(pp, P_MOD)


def hat_clrref(pp):
    return hat_page_clrattr(pp, P_REF)


def hat_clrrefmod(pp):
    return hat_page_clrattr(pp, P_REF | P_MOD)


def hat_page_is_mapped(pp):
    return hat_page_getshare(pp)


HAT_DONTALLOC = 0
HAT_ALLOC = 1
HRM_SHIFT = 4
HRM_BYTES = 1 << HRM_SHIFT
HRM_PAGES = HRM_BYTES * NBBY / 2
HRM_PGPERBYTE = NBBY / 2
HRM_PGBYTEMASK = HRM_PGPERBYTE - 1
HRM_HASHSIZE = 512
HRM_HASHMASK = HRM_HASHSIZE - 1
HRM_BLIST_INCR = 512
HRM_SWSMONID = 1
SSL_NLEVELS = 4
SSL_BFACTOR = 4
SSL_LOG2BF = 2
SEGP_ASYNC_FLUSH = 1
SEGP_FORCE_WIRED = 2
SEGP_SUCCESS = 0
SEGP_FAIL = 1

def seg_pages(seg):
    pass


IE_NOMEM = -1
AS_PAGLCK = 128
AS_CLAIMGAP = 64
AS_UNMAPWAIT = 32

def AS_TYPE_64BIT(as_):
    pass


AS_LREP_LINKEDLIST = 0
AS_LREP_SKIPLIST = 1
AS_MUTATION_THRESH = 225
AH_DIR = 1
AH_LO = 0
AH_HI = 1
AH_CONTAIN = 2
DMA_UNIT_8 = 1
DMA_UNIT_16 = 2
DMA_UNIT_32 = 4
DMALIM_VER0 = 2248146944L
DDI_DMA_FORCE_PHYSICAL = 256
DMA_ATTR_V0 = 0
DMA_ATTR_VERSION = DMA_ATTR_V0
DDI_DMA_CALLBACK_RUNOUT = 0
DDI_DMA_CALLBACK_DONE = 1
DDI_DMA_WRITE = 1
DDI_DMA_READ = 2
DDI_DMA_RDWR = DDI_DMA_READ | DDI_DMA_WRITE
DDI_DMA_REDZONE = 4
DDI_DMA_PARTIAL = 8
DDI_DMA_CONSISTENT = 16
DDI_DMA_EXCLUSIVE = 32
DDI_DMA_STREAMING = 64
DDI_DMA_SBUS_64BIT = 8192
DDI_DMA_MAPPED = 0
DDI_DMA_MAPOK = 0
DDI_DMA_PARTIAL_MAP = 1
DDI_DMA_DONE = 2
DDI_DMA_NORESOURCES = -1
DDI_DMA_NOMAPPING = -2
DDI_DMA_TOOBIG = -3
DDI_DMA_TOOSMALL = -4
DDI_DMA_LOCKED = -5
DDI_DMA_BADLIMITS = -6
DDI_DMA_STALE = -7
DDI_DMA_BADATTR = -8
DDI_DMA_INUSE = -9
DDI_DMA_SYNC_FORDEV = 0
DDI_DMA_SYNC_FORCPU = 1
DDI_DMA_SYNC_FORKERNEL = 2
PROT_READ = 1
PROT_WRITE = 2
PROT_EXEC = 4
PROT_USER = 8
PROT_ZFOD = PROT_READ | PROT_WRITE | PROT_EXEC | PROT_USER
PROT_ALL = PROT_READ | PROT_WRITE | PROT_EXEC | PROT_USER
PROT_NONE = 0
MAP_SHARED = 1
MAP_PRIVATE = 2
MAP_TYPE = 15
MAP_FIXED = 16
MAP_NORESERVE = 64
MAP_ANON = 256
MAP_ANONYMOUS = MAP_ANON
MAP_RENAME = 32
PROC_TEXT = PROT_EXEC | PROT_READ
PROC_DATA = PROT_READ | PROT_WRITE | PROT_EXEC
SHARED = 16
PRIVATE = 32
VALID_ATTR = PROT_READ | PROT_WRITE | PROT_EXEC | SHARED | PRIVATE
PROT_EXCL = 32
_MAP_LOW32 = 128
_MAP_NEW = 2147483648L
from TYPES import *
MADV_NORMAL = 0
MADV_RANDOM = 1
MADV_SEQUENTIAL = 2
MADV_WILLNEED = 3
MADV_DONTNEED = 4
MADV_FREE = 5
MS_OLDSYNC = 0
MS_SYNC = 4
MS_ASYNC = 1
MS_INVALIDATE = 2
MC_SYNC = 1
MC_LOCK = 2
MC_UNLOCK = 3
MC_ADVISE = 4
MC_LOCKAS = 5
MC_UNLOCKAS = 6
MCL_CURRENT = 1
MCL_FUTURE = 2
DDI_MAP_VERSION = 1
DDI_MF_USER_MAPPING = 1
DDI_MF_KERNEL_MAPPING = 2
DDI_MF_DEVICE_MAPPING = 4
DDI_ME_GENERIC = -1
DDI_ME_UNIMPLEMENTED = -2
DDI_ME_NORESOURCES = -3
DDI_ME_UNSUPPORTED = -4
DDI_ME_REGSPEC_RANGE = -5
DDI_ME_RNUMBER_RANGE = -6
DDI_ME_INVAL = -7

def CELLS_1275_TO_BYTES(n):
    return n * PROP_1275_CELL_SIZE


def BYTES_TO_1275_CELLS(n):
    return n / PROP_1275_CELL_SIZE


PH_FROM_PROM = 1
DDI_PROP_SUCCESS = 0
DDI_PROP_NOT_FOUND = 1
DDI_PROP_UNDEFINED = 2
DDI_PROP_NO_MEMORY = 3
DDI_PROP_INVAL_ARG = 4
DDI_PROP_BUF_TOO_SMALL = 5
DDI_PROP_CANNOT_DECODE = 6
DDI_PROP_CANNOT_ENCODE = 7
DDI_PROP_END_OF_DATA = 8
DDI_PROP_FOUND_1275 = 255
PROP_1275_INT_SIZE = 4
DDI_PROP_DONTPASS = 1
DDI_PROP_CANSLEEP = 2
DDI_PROP_SYSTEM_DEF = 4
DDI_PROP_NOTPROM = 8
DDI_PROP_DONTSLEEP = 16
DDI_PROP_STACK_CREATE = 32
DDI_PROP_UNDEF_IT = 64
DDI_PROP_HW_DEF = 128
DDI_PROP_TYPE_INT = 256
DDI_PROP_TYPE_STRING = 512
DDI_PROP_TYPE_BYTE = 1024
DDI_PROP_TYPE_COMPOSITE = 2048
DDI_PROP_TYPE_ANY = DDI_PROP_TYPE_INT | DDI_PROP_TYPE_STRING | DDI_PROP_TYPE_BYTE | DDI_PROP_TYPE_COMPOSITE
DDI_PROP_TYPE_MASK = DDI_PROP_TYPE_INT | DDI_PROP_TYPE_STRING | DDI_PROP_TYPE_BYTE | DDI_PROP_TYPE_COMPOSITE
DDI_RELATIVE_ADDRESSING = 'relative-addressing'
DDI_GENERIC_ADDRESSING = 'generic-addressing'
KMEM_PAGEABLE = 256
KMEM_NON_PAGEABLE = 512
UMEM_LOCKED = 1024
UMEM_TRASH = 2048
DEVMAP_OPS_REV = 1
DEVMAP_DEFAULTS = 0
DEVMAP_MAPPING_INVALID = 1
DEVMAP_ALLOW_REMAP = 2
DEVMAP_USE_PAGESIZE = 4
DEVMAP_SETUP_FLAGS = DEVMAP_MAPPING_INVALID | DEVMAP_ALLOW_REMAP | DEVMAP_USE_PAGESIZE
DEVMAP_SETUP_DONE = 256
DEVMAP_LOCK_INITED = 512
DEVMAP_FAULTING = 1024
DEVMAP_LOCKED = 2048
DEVMAP_FLAG_LARGE = 4096
DDI_UMEM_SLEEP = 0
DDI_UMEM_NOSLEEP = 1
DDI_UMEM_PAGEABLE = 2
DDI_UMEM_TRASH = 4
DDI_UMEMLOCK_READ = 1
DDI_UMEMLOCK_WRITE = 2
BUSO_REV = 4
BUSO_REV_3 = 3
BUSO_REV_4 = 4
DEVO_REV = 3
CB_REV = 1
DDI_IDENTIFIED = 0
DDI_NOT_IDENTIFIED = -1
DDI_PROBE_FAILURE = ENXIO
DDI_PROBE_DONTCARE = 0
DDI_PROBE_PARTIAL = 1
DDI_PROBE_SUCCESS = 2
MAPDEV_REV = 1
from TYPES import *
D_NEW = 0
_D_OLD = 1
D_TAPE = 8
D_MTSAFE = 32
_D_QNEXTLESS = 64
_D_MTOCSHARED = 128
D_MTOCEXCL = 2048
D_MTPUTSHARED = 4096
D_MTPERQ = 8192
D_MTQPAIR = 16384
D_MTPERMOD = 24576
D_MTOUTPERIM = 32768
_D_MTCBSHARED = 65536
D_MTINNER_MOD = D_MTPUTSHARED | _D_MTOCSHARED | _D_MTCBSHARED
D_MTOUTER_MOD = D_MTOCEXCL
D_MP = D_MTSAFE
D_64BIT = 512
D_SYNCSTR = 1024
D_DEVMAP = 256
D_HOTPLUG = 4
SNDZERO = 1
SNDPIPE = 2
RNORM = 0
RMSGD = 1
RMSGN = 2
RMODEMASK = 3
RPROTDAT = 4
RPROTDIS = 8
RPROTNORM = 16
RPROTMASK = 28
RFLUSHMASK = 32
RFLUSHPCPROT = 32
RERRNORM = 1
RERRNONPERSIST = 2
RERRMASK = RERRNORM | RERRNONPERSIST
WERRNORM = 4
WERRNONPERSIST = 8
WERRMASK = WERRNORM | WERRNONPERSIST
FLUSHR = 1
FLUSHW = 2
FLUSHRW = 3
FLUSHBAND = 4
MAPINOK = 1
NOMAPIN = 2
REMAPOK = 4
NOREMAP = 8
S_INPUT = 1
S_HIPRI = 2
S_OUTPUT = 4
S_MSG = 8
S_ERROR = 16
S_HANGUP = 32
S_RDNORM = 64
S_WRNORM = S_OUTPUT
S_RDBAND = 128
S_WRBAND = 256
S_BANDURG = 512
RS_HIPRI = 1
STRUIO_POSTPONE = 8
STRUIO_MAPIN = 16
MSG_HIPRI = 1
MSG_ANY = 2
MSG_BAND = 4
MSG_XPG4 = 8
MSG_IPEEK = 16
MSG_DISCARDTAIL = 32
MSG_HOLDSIG = 64
MSG_IGNERROR = 128
MSG_DELAYERROR = 256
MSG_IGNFLOW = 512
MSG_NOMARK = 1024
MORECTL = 1
MOREDATA = 2
MUXID_ALL = -1
ANYMARK = 1
LASTMARK = 2
_INFTIM = -1
INFTIM = _INFTIM
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\plat-sunos5\stropts.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 20:01:31 St�edn� Evropa (letn� �as)