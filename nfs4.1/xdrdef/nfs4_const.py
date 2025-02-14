# Generated by rpcgen.py from /home/pentest/Documents/linux-pynfs/nfs4.1/./xdrdef/nfs4.x on Fri Feb 14 09:26:47 2025
NFSPROC4_NULL = 0
NFSPROC4_COMPOUND = 1
CB_NULL = 0
CB_COMPOUND = 1
FALSE = 0
TRUE = 1
AUTH_NONE = 0
AUTH_SYS = 1
RPCSEC_GSS = 6
NFS4_FHSIZE = 128
NFS4_VERIFIER_SIZE = 8
NFS4_OTHER_SIZE = 12
NFS4_OPAQUE_LIMIT = 1024
NFS4_SESSIONID_SIZE = 16
NFS4_INT64_MAX = 0x7fffffffffffffff
NFS4_UINT64_MAX = 0xffffffffffffffff
NFS4_INT32_MAX = 0x7fffffff
NFS4_UINT32_MAX = 0xffffffff
NFS4_MAXFILELEN = 0xffffffffffffffff
NFS4_MAXFILEOFF = 0xfffffffffffffffe
NF4REG = 1
NF4DIR = 2
NF4BLK = 3
NF4CHR = 4
NF4LNK = 5
NF4SOCK = 6
NF4FIFO = 7
NF4ATTRDIR = 8
NF4NAMEDATTR = 9
nfs_ftype4 = {
    1 : 'NF4REG',
    2 : 'NF4DIR',
    3 : 'NF4BLK',
    4 : 'NF4CHR',
    5 : 'NF4LNK',
    6 : 'NF4SOCK',
    7 : 'NF4FIFO',
    8 : 'NF4ATTRDIR',
    9 : 'NF4NAMEDATTR',
}
NFS4_OK = 0
NFS4ERR_PERM = 1
NFS4ERR_NOENT = 2
NFS4ERR_IO = 5
NFS4ERR_NXIO = 6
NFS4ERR_ACCESS = 13
NFS4ERR_EXIST = 17
NFS4ERR_XDEV = 18
NFS4ERR_NOTDIR = 20
NFS4ERR_ISDIR = 21
NFS4ERR_INVAL = 22
NFS4ERR_FBIG = 27
NFS4ERR_NOSPC = 28
NFS4ERR_ROFS = 30
NFS4ERR_MLINK = 31
NFS4ERR_NAMETOOLONG = 63
NFS4ERR_NOTEMPTY = 66
NFS4ERR_DQUOT = 69
NFS4ERR_STALE = 70
NFS4ERR_BADHANDLE = 10001
NFS4ERR_BAD_COOKIE = 10003
NFS4ERR_NOTSUPP = 10004
NFS4ERR_TOOSMALL = 10005
NFS4ERR_SERVERFAULT = 10006
NFS4ERR_BADTYPE = 10007
NFS4ERR_DELAY = 10008
NFS4ERR_SAME = 10009
NFS4ERR_DENIED = 10010
NFS4ERR_EXPIRED = 10011
NFS4ERR_LOCKED = 10012
NFS4ERR_GRACE = 10013
NFS4ERR_FHEXPIRED = 10014
NFS4ERR_SHARE_DENIED = 10015
NFS4ERR_WRONGSEC = 10016
NFS4ERR_CLID_INUSE = 10017
NFS4ERR_RESOURCE = 10018
NFS4ERR_MOVED = 10019
NFS4ERR_NOFILEHANDLE = 10020
NFS4ERR_MINOR_VERS_MISMATCH = 10021
NFS4ERR_STALE_CLIENTID = 10022
NFS4ERR_STALE_STATEID = 10023
NFS4ERR_OLD_STATEID = 10024
NFS4ERR_BAD_STATEID = 10025
NFS4ERR_BAD_SEQID = 10026
NFS4ERR_NOT_SAME = 10027
NFS4ERR_LOCK_RANGE = 10028
NFS4ERR_SYMLINK = 10029
NFS4ERR_RESTOREFH = 10030
NFS4ERR_LEASE_MOVED = 10031
NFS4ERR_ATTRNOTSUPP = 10032
NFS4ERR_NO_GRACE = 10033
NFS4ERR_RECLAIM_BAD = 10034
NFS4ERR_RECLAIM_CONFLICT = 10035
NFS4ERR_BADXDR = 10036
NFS4ERR_LOCKS_HELD = 10037
NFS4ERR_OPENMODE = 10038
NFS4ERR_BADOWNER = 10039
NFS4ERR_BADCHAR = 10040
NFS4ERR_BADNAME = 10041
NFS4ERR_BAD_RANGE = 10042
NFS4ERR_LOCK_NOTSUPP = 10043
NFS4ERR_OP_ILLEGAL = 10044
NFS4ERR_DEADLOCK = 10045
NFS4ERR_FILE_OPEN = 10046
NFS4ERR_ADMIN_REVOKED = 10047
NFS4ERR_CB_PATH_DOWN = 10048
NFS4ERR_BADIOMODE = 10049
NFS4ERR_BADLAYOUT = 10050
NFS4ERR_BAD_SESSION_DIGEST = 10051
NFS4ERR_BADSESSION = 10052
NFS4ERR_BADSLOT = 10053
NFS4ERR_COMPLETE_ALREADY = 10054
NFS4ERR_CONN_NOT_BOUND_TO_SESSION = 10055
NFS4ERR_DELEG_ALREADY_WANTED = 10056
NFS4ERR_BACK_CHAN_BUSY = 10057
NFS4ERR_LAYOUTTRYLATER = 10058
NFS4ERR_LAYOUTUNAVAILABLE = 10059
NFS4ERR_NOMATCHING_LAYOUT = 10060
NFS4ERR_RECALLCONFLICT = 10061
NFS4ERR_UNKNOWN_LAYOUTTYPE = 10062
NFS4ERR_SEQ_MISORDERED = 10063
NFS4ERR_SEQUENCE_POS = 10064
NFS4ERR_REQ_TOO_BIG = 10065
NFS4ERR_REP_TOO_BIG = 10066
NFS4ERR_REP_TOO_BIG_TO_CACHE = 10067
NFS4ERR_RETRY_UNCACHED_REP = 10068
NFS4ERR_UNSAFE_COMPOUND = 10069
NFS4ERR_TOO_MANY_OPS = 10070
NFS4ERR_OP_NOT_IN_SESSION = 10071
NFS4ERR_HASH_ALG_UNSUPP = 10072
NFS4ERR_CLIENTID_BUSY = 10074
NFS4ERR_PNFS_IO_HOLE = 10075
NFS4ERR_SEQ_FALSE_RETRY = 10076
NFS4ERR_BAD_HIGH_SLOT = 10077
NFS4ERR_DEADSESSION = 10078
NFS4ERR_ENCR_ALG_UNSUPP = 10079
NFS4ERR_PNFS_NO_LAYOUT = 10080
NFS4ERR_NOT_ONLY_OP = 10081
NFS4ERR_WRONG_CRED = 10082
NFS4ERR_WRONG_TYPE = 10083
NFS4ERR_DIRDELEG_UNAVAIL = 10084
NFS4ERR_REJECT_DELEG = 10085
NFS4ERR_RETURNCONFLICT = 10086
NFS4ERR_DELEG_REVOKED = 10087
NFS4ERR_PARTNER_NOTSUPP = 10088
NFS4ERR_PARTNER_NO_AUTH = 10089
NFS4ERR_UNION_NOTSUPP = 10090
NFS4ERR_OFFLOAD_DENIED = 10091
NFS4ERR_WRONG_LFS = 10092
NFS4ERR_BADLABEL = 10093
NFS4ERR_OFFLOAD_NO_REQS = 10094
NFS4ERR_NOXATTR = 10095
NFS4ERR_XATTR2BIG = 10096
nfsstat4 = {
    0 : 'NFS4_OK',
    1 : 'NFS4ERR_PERM',
    2 : 'NFS4ERR_NOENT',
    5 : 'NFS4ERR_IO',
    6 : 'NFS4ERR_NXIO',
    13 : 'NFS4ERR_ACCESS',
    17 : 'NFS4ERR_EXIST',
    18 : 'NFS4ERR_XDEV',
    20 : 'NFS4ERR_NOTDIR',
    21 : 'NFS4ERR_ISDIR',
    22 : 'NFS4ERR_INVAL',
    27 : 'NFS4ERR_FBIG',
    28 : 'NFS4ERR_NOSPC',
    30 : 'NFS4ERR_ROFS',
    31 : 'NFS4ERR_MLINK',
    63 : 'NFS4ERR_NAMETOOLONG',
    66 : 'NFS4ERR_NOTEMPTY',
    69 : 'NFS4ERR_DQUOT',
    70 : 'NFS4ERR_STALE',
    10001 : 'NFS4ERR_BADHANDLE',
    10003 : 'NFS4ERR_BAD_COOKIE',
    10004 : 'NFS4ERR_NOTSUPP',
    10005 : 'NFS4ERR_TOOSMALL',
    10006 : 'NFS4ERR_SERVERFAULT',
    10007 : 'NFS4ERR_BADTYPE',
    10008 : 'NFS4ERR_DELAY',
    10009 : 'NFS4ERR_SAME',
    10010 : 'NFS4ERR_DENIED',
    10011 : 'NFS4ERR_EXPIRED',
    10012 : 'NFS4ERR_LOCKED',
    10013 : 'NFS4ERR_GRACE',
    10014 : 'NFS4ERR_FHEXPIRED',
    10015 : 'NFS4ERR_SHARE_DENIED',
    10016 : 'NFS4ERR_WRONGSEC',
    10017 : 'NFS4ERR_CLID_INUSE',
    10018 : 'NFS4ERR_RESOURCE',
    10019 : 'NFS4ERR_MOVED',
    10020 : 'NFS4ERR_NOFILEHANDLE',
    10021 : 'NFS4ERR_MINOR_VERS_MISMATCH',
    10022 : 'NFS4ERR_STALE_CLIENTID',
    10023 : 'NFS4ERR_STALE_STATEID',
    10024 : 'NFS4ERR_OLD_STATEID',
    10025 : 'NFS4ERR_BAD_STATEID',
    10026 : 'NFS4ERR_BAD_SEQID',
    10027 : 'NFS4ERR_NOT_SAME',
    10028 : 'NFS4ERR_LOCK_RANGE',
    10029 : 'NFS4ERR_SYMLINK',
    10030 : 'NFS4ERR_RESTOREFH',
    10031 : 'NFS4ERR_LEASE_MOVED',
    10032 : 'NFS4ERR_ATTRNOTSUPP',
    10033 : 'NFS4ERR_NO_GRACE',
    10034 : 'NFS4ERR_RECLAIM_BAD',
    10035 : 'NFS4ERR_RECLAIM_CONFLICT',
    10036 : 'NFS4ERR_BADXDR',
    10037 : 'NFS4ERR_LOCKS_HELD',
    10038 : 'NFS4ERR_OPENMODE',
    10039 : 'NFS4ERR_BADOWNER',
    10040 : 'NFS4ERR_BADCHAR',
    10041 : 'NFS4ERR_BADNAME',
    10042 : 'NFS4ERR_BAD_RANGE',
    10043 : 'NFS4ERR_LOCK_NOTSUPP',
    10044 : 'NFS4ERR_OP_ILLEGAL',
    10045 : 'NFS4ERR_DEADLOCK',
    10046 : 'NFS4ERR_FILE_OPEN',
    10047 : 'NFS4ERR_ADMIN_REVOKED',
    10048 : 'NFS4ERR_CB_PATH_DOWN',
    10049 : 'NFS4ERR_BADIOMODE',
    10050 : 'NFS4ERR_BADLAYOUT',
    10051 : 'NFS4ERR_BAD_SESSION_DIGEST',
    10052 : 'NFS4ERR_BADSESSION',
    10053 : 'NFS4ERR_BADSLOT',
    10054 : 'NFS4ERR_COMPLETE_ALREADY',
    10055 : 'NFS4ERR_CONN_NOT_BOUND_TO_SESSION',
    10056 : 'NFS4ERR_DELEG_ALREADY_WANTED',
    10057 : 'NFS4ERR_BACK_CHAN_BUSY',
    10058 : 'NFS4ERR_LAYOUTTRYLATER',
    10059 : 'NFS4ERR_LAYOUTUNAVAILABLE',
    10060 : 'NFS4ERR_NOMATCHING_LAYOUT',
    10061 : 'NFS4ERR_RECALLCONFLICT',
    10062 : 'NFS4ERR_UNKNOWN_LAYOUTTYPE',
    10063 : 'NFS4ERR_SEQ_MISORDERED',
    10064 : 'NFS4ERR_SEQUENCE_POS',
    10065 : 'NFS4ERR_REQ_TOO_BIG',
    10066 : 'NFS4ERR_REP_TOO_BIG',
    10067 : 'NFS4ERR_REP_TOO_BIG_TO_CACHE',
    10068 : 'NFS4ERR_RETRY_UNCACHED_REP',
    10069 : 'NFS4ERR_UNSAFE_COMPOUND',
    10070 : 'NFS4ERR_TOO_MANY_OPS',
    10071 : 'NFS4ERR_OP_NOT_IN_SESSION',
    10072 : 'NFS4ERR_HASH_ALG_UNSUPP',
    10074 : 'NFS4ERR_CLIENTID_BUSY',
    10075 : 'NFS4ERR_PNFS_IO_HOLE',
    10076 : 'NFS4ERR_SEQ_FALSE_RETRY',
    10077 : 'NFS4ERR_BAD_HIGH_SLOT',
    10078 : 'NFS4ERR_DEADSESSION',
    10079 : 'NFS4ERR_ENCR_ALG_UNSUPP',
    10080 : 'NFS4ERR_PNFS_NO_LAYOUT',
    10081 : 'NFS4ERR_NOT_ONLY_OP',
    10082 : 'NFS4ERR_WRONG_CRED',
    10083 : 'NFS4ERR_WRONG_TYPE',
    10084 : 'NFS4ERR_DIRDELEG_UNAVAIL',
    10085 : 'NFS4ERR_REJECT_DELEG',
    10086 : 'NFS4ERR_RETURNCONFLICT',
    10087 : 'NFS4ERR_DELEG_REVOKED',
    10088 : 'NFS4ERR_PARTNER_NOTSUPP',
    10089 : 'NFS4ERR_PARTNER_NO_AUTH',
    10090 : 'NFS4ERR_UNION_NOTSUPP',
    10091 : 'NFS4ERR_OFFLOAD_DENIED',
    10092 : 'NFS4ERR_WRONG_LFS',
    10093 : 'NFS4ERR_BADLABEL',
    10094 : 'NFS4ERR_OFFLOAD_NO_REQS',
    10095 : 'NFS4ERR_NOXATTR',
    10096 : 'NFS4ERR_XATTR2BIG',
}
SET_TO_SERVER_TIME4 = 0
SET_TO_CLIENT_TIME4 = 1
time_how4 = {
    0 : 'SET_TO_SERVER_TIME4',
    1 : 'SET_TO_CLIENT_TIME4',
}
ACL4_SUPPORT_ALLOW_ACL = 0x00000001
ACL4_SUPPORT_DENY_ACL = 0x00000002
ACL4_SUPPORT_AUDIT_ACL = 0x00000004
ACL4_SUPPORT_ALARM_ACL = 0x00000008
ACE4_ACCESS_ALLOWED_ACE_TYPE = 0x00000000
ACE4_ACCESS_DENIED_ACE_TYPE = 0x00000001
ACE4_SYSTEM_AUDIT_ACE_TYPE = 0x00000002
ACE4_SYSTEM_ALARM_ACE_TYPE = 0x00000003
ACE4_FILE_INHERIT_ACE = 0x00000001
ACE4_DIRECTORY_INHERIT_ACE = 0x00000002
ACE4_NO_PROPAGATE_INHERIT_ACE = 0x00000004
ACE4_INHERIT_ONLY_ACE = 0x00000008
ACE4_SUCCESSFUL_ACCESS_ACE_FLAG = 0x00000010
ACE4_FAILED_ACCESS_ACE_FLAG = 0x00000020
ACE4_IDENTIFIER_GROUP = 0x00000040
ACE4_INHERITED_ACE = 0x00000080
ACE4_READ_DATA = 0x00000001
ACE4_LIST_DIRECTORY = 0x00000001
ACE4_WRITE_DATA = 0x00000002
ACE4_ADD_FILE = 0x00000002
ACE4_APPEND_DATA = 0x00000004
ACE4_ADD_SUBDIRECTORY = 0x00000004
ACE4_READ_NAMED_ATTRS = 0x00000008
ACE4_WRITE_NAMED_ATTRS = 0x00000010
ACE4_EXECUTE = 0x00000020
ACE4_DELETE_CHILD = 0x00000040
ACE4_READ_ATTRIBUTES = 0x00000080
ACE4_WRITE_ATTRIBUTES = 0x00000100
ACE4_WRITE_RETENTION = 0x00000200
ACE4_WRITE_RETENTION_HOLD = 0x00000400
ACE4_DELETE = 0x00010000
ACE4_READ_ACL = 0x00020000
ACE4_WRITE_ACL = 0x00040000
ACE4_WRITE_OWNER = 0x00080000
ACE4_SYNCHRONIZE = 0x00100000
ACE4_GENERIC_READ = 0x00120081
ACE4_GENERIC_WRITE = 0x00160106
ACE4_GENERIC_EXECUTE = 0x001200A0
ACL4_AUTO_INHERIT = 0x00000001
ACL4_PROTECTED = 0x00000002
ACL4_DEFAULTED = 0x00000004
MODE4_SUID = 0x800
MODE4_SGID = 0x400
MODE4_SVTX = 0x200
MODE4_RUSR = 0x100
MODE4_WUSR = 0x080
MODE4_XUSR = 0x040
MODE4_RGRP = 0x020
MODE4_WGRP = 0x010
MODE4_XGRP = 0x008
MODE4_ROTH = 0x004
MODE4_WOTH = 0x002
MODE4_XOTH = 0x001
FH4_PERSISTENT = 0x00000000
FH4_NOEXPIRE_WITH_OPEN = 0x00000001
FH4_VOLATILE_ANY = 0x00000002
FH4_VOL_MIGRATION = 0x00000004
FH4_VOL_RENAME = 0x00000008
LAYOUT4_NFSV4_1_FILES = 0x1
LAYOUT4_OSD2_OBJECTS = 0x2
LAYOUT4_BLOCK_VOLUME = 0x3
LAYOUT4_FLEX_FILES = 0x4
layouttype4 = {
    0x1 : 'LAYOUT4_NFSV4_1_FILES',
    0x2 : 'LAYOUT4_OSD2_OBJECTS',
    0x3 : 'LAYOUT4_BLOCK_VOLUME',
    0x4 : 'LAYOUT4_FLEX_FILES',
}
LAYOUTIOMODE4_READ = 1
LAYOUTIOMODE4_RW = 2
LAYOUTIOMODE4_ANY = 3
layoutiomode4 = {
    1 : 'LAYOUTIOMODE4_READ',
    2 : 'LAYOUTIOMODE4_RW',
    3 : 'LAYOUTIOMODE4_ANY',
}
NFS4_DEVICEID4_SIZE = 16
LAYOUT4_RET_REC_FILE = 1
LAYOUT4_RET_REC_FSID = 2
LAYOUT4_RET_REC_ALL = 3
LAYOUTRETURN4_FILE = LAYOUT4_RET_REC_FILE
LAYOUTRETURN4_FSID = LAYOUT4_RET_REC_FSID
LAYOUTRETURN4_ALL = LAYOUT4_RET_REC_ALL
layoutreturn_type4 = {
    LAYOUT4_RET_REC_FILE : 'LAYOUTRETURN4_FILE',
    LAYOUT4_RET_REC_FSID : 'LAYOUTRETURN4_FSID',
    LAYOUT4_RET_REC_ALL : 'LAYOUTRETURN4_ALL',
}
STATUS4_FIXED = 1
STATUS4_UPDATED = 2
STATUS4_VERSIONED = 3
STATUS4_WRITABLE = 4
STATUS4_REFERRAL = 5
fs4_status_type = {
    1 : 'STATUS4_FIXED',
    2 : 'STATUS4_UPDATED',
    3 : 'STATUS4_VERSIONED',
    4 : 'STATUS4_WRITABLE',
    5 : 'STATUS4_REFERRAL',
}
TH4_READ_SIZE = 0
TH4_WRITE_SIZE = 1
TH4_READ_IOSIZE = 2
TH4_WRITE_IOSIZE = 3
RET4_DURATION_INFINITE = 0xffffffffffffffff
FSCHARSET_CAP4_CONTAINS_NON_UTF8 = 0x1
FSCHARSET_CAP4_ALLOWS_ONLY_UTF8 = 0x2
NL4_NAME = 1
NL4_URL = 2
NL4_NETADDR = 3
netloc_type4 = {
    1 : 'NL4_NAME',
    2 : 'NL4_URL',
    3 : 'NL4_NETADDR',
}
NFS4_CHANGE_TYPE_IS_MONOTONIC_INCR = 0
NFS4_CHANGE_TYPE_IS_VERSION_COUNTER = 1
NFS4_CHANGE_TYPE_IS_VERSION_COUNTER_NOPNFS = 2
NFS4_CHANGE_TYPE_IS_TIME_METADATA = 3
NFS4_CHANGE_TYPE_IS_UNDEFINED = 4
change_attr_type4 = {
    0 : 'NFS4_CHANGE_TYPE_IS_MONOTONIC_INCR',
    1 : 'NFS4_CHANGE_TYPE_IS_VERSION_COUNTER',
    2 : 'NFS4_CHANGE_TYPE_IS_VERSION_COUNTER_NOPNFS',
    3 : 'NFS4_CHANGE_TYPE_IS_TIME_METADATA',
    4 : 'NFS4_CHANGE_TYPE_IS_UNDEFINED',
}
NFS4_CONTENT_DATA = 0
NFS4_CONTENT_HOLE = 1
data_content4 = {
    0 : 'NFS4_CONTENT_DATA',
    1 : 'NFS4_CONTENT_HOLE',
}
UNSTABLE4 = 0
DATA_SYNC4 = 1
FILE_SYNC4 = 2
stable_how4 = {
    0 : 'UNSTABLE4',
    1 : 'DATA_SYNC4',
    2 : 'FILE_SYNC4',
}
FATTR4_SUPPORTED_ATTRS = 0
FATTR4_TYPE = 1
FATTR4_FH_EXPIRE_TYPE = 2
FATTR4_CHANGE = 3
FATTR4_SIZE = 4
FATTR4_LINK_SUPPORT = 5
FATTR4_SYMLINK_SUPPORT = 6
FATTR4_NAMED_ATTR = 7
FATTR4_FSID = 8
FATTR4_UNIQUE_HANDLES = 9
FATTR4_LEASE_TIME = 10
FATTR4_RDATTR_ERROR = 11
FATTR4_FILEHANDLE = 19
FATTR4_SUPPATTR_EXCLCREAT = 75
FATTR4_ACL = 12
FATTR4_ACLSUPPORT = 13
FATTR4_ARCHIVE = 14
FATTR4_CANSETTIME = 15
FATTR4_CASE_INSENSITIVE = 16
FATTR4_CASE_PRESERVING = 17
FATTR4_CHOWN_RESTRICTED = 18
FATTR4_FILEID = 20
FATTR4_FILES_AVAIL = 21
FATTR4_FILES_FREE = 22
FATTR4_FILES_TOTAL = 23
FATTR4_FS_LOCATIONS = 24
FATTR4_HIDDEN = 25
FATTR4_HOMOGENEOUS = 26
FATTR4_MAXFILESIZE = 27
FATTR4_MAXLINK = 28
FATTR4_MAXNAME = 29
FATTR4_MAXREAD = 30
FATTR4_MAXWRITE = 31
FATTR4_MIMETYPE = 32
FATTR4_MODE = 33
FATTR4_NO_TRUNC = 34
FATTR4_NUMLINKS = 35
FATTR4_OWNER = 36
FATTR4_OWNER_GROUP = 37
FATTR4_QUOTA_AVAIL_HARD = 38
FATTR4_QUOTA_AVAIL_SOFT = 39
FATTR4_QUOTA_USED = 40
FATTR4_RAWDEV = 41
FATTR4_SPACE_AVAIL = 42
FATTR4_SPACE_FREE = 43
FATTR4_SPACE_TOTAL = 44
FATTR4_SPACE_USED = 45
FATTR4_SYSTEM = 46
FATTR4_TIME_ACCESS = 47
FATTR4_TIME_ACCESS_SET = 48
FATTR4_TIME_BACKUP = 49
FATTR4_TIME_CREATE = 50
FATTR4_TIME_DELTA = 51
FATTR4_TIME_METADATA = 52
FATTR4_TIME_MODIFY = 53
FATTR4_TIME_MODIFY_SET = 54
FATTR4_MOUNTED_ON_FILEID = 55
FATTR4_DIR_NOTIF_DELAY = 56
FATTR4_DIRENT_NOTIF_DELAY = 57
FATTR4_DACL = 58
FATTR4_SACL = 59
FATTR4_CHANGE_POLICY = 60
FATTR4_FS_STATUS = 61
FATTR4_FS_LAYOUT_TYPES = 62
FATTR4_LAYOUT_HINT = 63
FATTR4_LAYOUT_TYPES = 64
FATTR4_LAYOUT_BLKSIZE = 65
FATTR4_LAYOUT_ALIGNMENT = 66
FATTR4_FS_LOCATIONS_INFO = 67
FATTR4_MDSTHRESHOLD = 68
FATTR4_RETENTION_GET = 69
FATTR4_RETENTION_SET = 70
FATTR4_RETENTEVT_GET = 71
FATTR4_RETENTEVT_SET = 72
FATTR4_RETENTION_HOLD = 73
FATTR4_MODE_SET_MASKED = 74
FATTR4_FS_CHARSET_CAP = 76
FATTR4_CLONE_BLKSIZE = 77
FATTR4_SPACE_FREED = 78
FATTR4_CHANGE_ATTR_TYPE = 79
FATTR4_SEC_LABEL = 80
FATTR4_XATTR_SUPPORT = 82
READ_LT = 1
WRITE_LT = 2
READW_LT = 3
WRITEW_LT = 4
nfs_lock_type4 = {
    1 : 'READ_LT',
    2 : 'WRITE_LT',
    3 : 'READW_LT',
    4 : 'WRITEW_LT',
}
SSV4_SUBKEY_MIC_I2T = 1
SSV4_SUBKEY_MIC_T2I = 2
SSV4_SUBKEY_SEAL_I2T = 3
SSV4_SUBKEY_SEAL_T2I = 4
ssv_subkey4 = {
    1 : 'SSV4_SUBKEY_MIC_I2T',
    2 : 'SSV4_SUBKEY_MIC_T2I',
    3 : 'SSV4_SUBKEY_SEAL_I2T',
    4 : 'SSV4_SUBKEY_SEAL_T2I',
}
FSLI4BX_GFLAGS = 0
FSLI4BX_TFLAGS = 1
FSLI4BX_CLSIMUL = 2
FSLI4BX_CLHANDLE = 3
FSLI4BX_CLFILEID = 4
FSLI4BX_CLWRITEVER = 5
FSLI4BX_CLCHANGE = 6
FSLI4BX_CLREADDIR = 7
FSLI4BX_READRANK = 8
FSLI4BX_WRITERANK = 9
FSLI4BX_READORDER = 10
FSLI4BX_WRITEORDER = 11
FSLI4GF_WRITABLE = 0x01
FSLI4GF_CUR_REQ = 0x02
FSLI4GF_ABSENT = 0x04
FSLI4GF_GOING = 0x08
FSLI4GF_SPLIT = 0x10
FSLI4TF_RDMA = 0x01
FSLI4IF_VAR_SUB = 0x00000001
NFL4_UFLG_MASK = 0x0000003F
NFL4_UFLG_DENSE = 0x00000001
NFL4_UFLG_COMMIT_THRU_MDS = 0x00000002
NFL42_UFLG_IO_ADVISE_THRU_MDS = 0x00000004
NFL4_UFLG_STRIPE_UNIT_SIZE_MASK = 0xFFFFFFC0
NFLH4_CARE_DENSE = NFL4_UFLG_DENSE
NFLH4_CARE_COMMIT_THRU_MDS = NFL4_UFLG_COMMIT_THRU_MDS
NFL42_CARE_IO_ADVISE_THRU_MDS = NFL42_UFLG_IO_ADVISE_THRU_MDS
NFLH4_CARE_STRIPE_UNIT_SIZE = 0x00000040
NFLH4_CARE_STRIPE_COUNT = 0x00000080
filelayout_hint_care4 = {
    NFL4_UFLG_DENSE : 'NFLH4_CARE_DENSE',
    NFL4_UFLG_COMMIT_THRU_MDS : 'NFLH4_CARE_COMMIT_THRU_MDS',
    NFL42_UFLG_IO_ADVISE_THRU_MDS : 'NFL42_CARE_IO_ADVISE_THRU_MDS',
    0x00000040 : 'NFLH4_CARE_STRIPE_UNIT_SIZE',
    0x00000080 : 'NFLH4_CARE_STRIPE_COUNT',
}
OP_ACCESS = 3
OP_CLOSE = 4
OP_COMMIT = 5
OP_CREATE = 6
OP_DELEGPURGE = 7
OP_DELEGRETURN = 8
OP_GETATTR = 9
OP_GETFH = 10
OP_LINK = 11
OP_LOCK = 12
OP_LOCKT = 13
OP_LOCKU = 14
OP_LOOKUP = 15
OP_LOOKUPP = 16
OP_NVERIFY = 17
OP_OPEN = 18
OP_OPENATTR = 19
OP_OPEN_CONFIRM = 20
OP_OPEN_DOWNGRADE = 21
OP_PUTFH = 22
OP_PUTPUBFH = 23
OP_PUTROOTFH = 24
OP_READ = 25
OP_READDIR = 26
OP_READLINK = 27
OP_REMOVE = 28
OP_RENAME = 29
OP_RENEW = 30
OP_RESTOREFH = 31
OP_SAVEFH = 32
OP_SECINFO = 33
OP_SETATTR = 34
OP_SETCLIENTID = 35
OP_SETCLIENTID_CONFIRM = 36
OP_VERIFY = 37
OP_WRITE = 38
OP_RELEASE_LOCKOWNER = 39
OP_BACKCHANNEL_CTL = 40
OP_BIND_CONN_TO_SESSION = 41
OP_EXCHANGE_ID = 42
OP_CREATE_SESSION = 43
OP_DESTROY_SESSION = 44
OP_FREE_STATEID = 45
OP_GET_DIR_DELEGATION = 46
OP_GETDEVICEINFO = 47
OP_GETDEVICELIST = 48
OP_LAYOUTCOMMIT = 49
OP_LAYOUTGET = 50
OP_LAYOUTRETURN = 51
OP_SECINFO_NO_NAME = 52
OP_SEQUENCE = 53
OP_SET_SSV = 54
OP_TEST_STATEID = 55
OP_WANT_DELEGATION = 56
OP_DESTROY_CLIENTID = 57
OP_RECLAIM_COMPLETE = 58
OP_ALLOCATE = 59
OP_COPY = 60
OP_COPY_NOTIFY = 61
OP_DEALLOCATE = 62
OP_IO_ADVISE = 63
OP_LAYOUTERROR = 64
OP_LAYOUTSTATS = 65
OP_OFFLOAD_CANCEL = 66
OP_OFFLOAD_STATUS = 67
OP_READ_PLUS = 68
OP_SEEK = 69
OP_WRITE_SAME = 70
OP_CLONE = 71
OP_GETXATTR = 72
OP_SETXATTR = 73
OP_LISTXATTRS = 74
OP_REMOVEXATTR = 75
OP_ILLEGAL = 10044
nfs_opnum4 = {
    3 : 'OP_ACCESS',
    4 : 'OP_CLOSE',
    5 : 'OP_COMMIT',
    6 : 'OP_CREATE',
    7 : 'OP_DELEGPURGE',
    8 : 'OP_DELEGRETURN',
    9 : 'OP_GETATTR',
    10 : 'OP_GETFH',
    11 : 'OP_LINK',
    12 : 'OP_LOCK',
    13 : 'OP_LOCKT',
    14 : 'OP_LOCKU',
    15 : 'OP_LOOKUP',
    16 : 'OP_LOOKUPP',
    17 : 'OP_NVERIFY',
    18 : 'OP_OPEN',
    19 : 'OP_OPENATTR',
    20 : 'OP_OPEN_CONFIRM',
    21 : 'OP_OPEN_DOWNGRADE',
    22 : 'OP_PUTFH',
    23 : 'OP_PUTPUBFH',
    24 : 'OP_PUTROOTFH',
    25 : 'OP_READ',
    26 : 'OP_READDIR',
    27 : 'OP_READLINK',
    28 : 'OP_REMOVE',
    29 : 'OP_RENAME',
    30 : 'OP_RENEW',
    31 : 'OP_RESTOREFH',
    32 : 'OP_SAVEFH',
    33 : 'OP_SECINFO',
    34 : 'OP_SETATTR',
    35 : 'OP_SETCLIENTID',
    36 : 'OP_SETCLIENTID_CONFIRM',
    37 : 'OP_VERIFY',
    38 : 'OP_WRITE',
    39 : 'OP_RELEASE_LOCKOWNER',
    40 : 'OP_BACKCHANNEL_CTL',
    41 : 'OP_BIND_CONN_TO_SESSION',
    42 : 'OP_EXCHANGE_ID',
    43 : 'OP_CREATE_SESSION',
    44 : 'OP_DESTROY_SESSION',
    45 : 'OP_FREE_STATEID',
    46 : 'OP_GET_DIR_DELEGATION',
    47 : 'OP_GETDEVICEINFO',
    48 : 'OP_GETDEVICELIST',
    49 : 'OP_LAYOUTCOMMIT',
    50 : 'OP_LAYOUTGET',
    51 : 'OP_LAYOUTRETURN',
    52 : 'OP_SECINFO_NO_NAME',
    53 : 'OP_SEQUENCE',
    54 : 'OP_SET_SSV',
    55 : 'OP_TEST_STATEID',
    56 : 'OP_WANT_DELEGATION',
    57 : 'OP_DESTROY_CLIENTID',
    58 : 'OP_RECLAIM_COMPLETE',
    59 : 'OP_ALLOCATE',
    60 : 'OP_COPY',
    61 : 'OP_COPY_NOTIFY',
    62 : 'OP_DEALLOCATE',
    63 : 'OP_IO_ADVISE',
    64 : 'OP_LAYOUTERROR',
    65 : 'OP_LAYOUTSTATS',
    66 : 'OP_OFFLOAD_CANCEL',
    67 : 'OP_OFFLOAD_STATUS',
    68 : 'OP_READ_PLUS',
    69 : 'OP_SEEK',
    70 : 'OP_WRITE_SAME',
    71 : 'OP_CLONE',
    72 : 'OP_GETXATTR',
    73 : 'OP_SETXATTR',
    74 : 'OP_LISTXATTRS',
    75 : 'OP_REMOVEXATTR',
    10044 : 'OP_ILLEGAL',
}
ACCESS4_READ = 0x00000001
ACCESS4_LOOKUP = 0x00000002
ACCESS4_MODIFY = 0x00000004
ACCESS4_EXTEND = 0x00000008
ACCESS4_DELETE = 0x00000010
ACCESS4_EXECUTE = 0x00000020
UNCHECKED4 = 0
GUARDED4 = 1
EXCLUSIVE4 = 2
EXCLUSIVE4_1 = 3
createmode4 = {
    0 : 'UNCHECKED4',
    1 : 'GUARDED4',
    2 : 'EXCLUSIVE4',
    3 : 'EXCLUSIVE4_1',
}
OPEN4_NOCREATE = 0
OPEN4_CREATE = 1
opentype4 = {
    0 : 'OPEN4_NOCREATE',
    1 : 'OPEN4_CREATE',
}
NFS_LIMIT_SIZE = 1
NFS_LIMIT_BLOCKS = 2
limit_by4 = {
    1 : 'NFS_LIMIT_SIZE',
    2 : 'NFS_LIMIT_BLOCKS',
}
OPEN4_SHARE_ACCESS_READ = 0x00000001
OPEN4_SHARE_ACCESS_WRITE = 0x00000002
OPEN4_SHARE_ACCESS_BOTH = 0x00000003
OPEN4_SHARE_DENY_NONE = 0x00000000
OPEN4_SHARE_DENY_READ = 0x00000001
OPEN4_SHARE_DENY_WRITE = 0x00000002
OPEN4_SHARE_DENY_BOTH = 0x00000003
OPEN4_SHARE_ACCESS_WANT_DELEG_MASK = 0xFF00
OPEN4_SHARE_ACCESS_WANT_NO_PREFERENCE = 0x0000
OPEN4_SHARE_ACCESS_WANT_READ_DELEG = 0x0100
OPEN4_SHARE_ACCESS_WANT_WRITE_DELEG = 0x0200
OPEN4_SHARE_ACCESS_WANT_ANY_DELEG = 0x0300
OPEN4_SHARE_ACCESS_WANT_NO_DELEG = 0x0400
OPEN4_SHARE_ACCESS_WANT_CANCEL = 0x0500
OPEN4_SHARE_ACCESS_WANT_SIGNAL_DELEG_WHEN_RESRC_AVAIL = 0x10000
OPEN4_SHARE_ACCESS_WANT_PUSH_DELEG_WHEN_UNCONTENDED = 0x20000
OPEN_DELEGATE_NONE = 0
OPEN_DELEGATE_READ = 1
OPEN_DELEGATE_WRITE = 2
OPEN_DELEGATE_NONE_EXT = 3
OPEN_DELEGATE_READ_ATTRS_DELEG = 4
OPEN_DELEGATE_WRITE_ATTRS_DELEG = 5
open_delegation_type4 = {
    0 : 'OPEN_DELEGATE_NONE',
    1 : 'OPEN_DELEGATE_READ',
    2 : 'OPEN_DELEGATE_WRITE',
    3 : 'OPEN_DELEGATE_NONE_EXT',
    4 : 'OPEN_DELEGATE_READ_ATTRS_DELEG',
    5 : 'OPEN_DELEGATE_WRITE_ATTRS_DELEG',
}
CLAIM_NULL = 0
CLAIM_PREVIOUS = 1
CLAIM_DELEGATE_CUR = 2
CLAIM_DELEGATE_PREV = 3
CLAIM_FH = 4
CLAIM_DELEG_CUR_FH = 5
CLAIM_DELEG_PREV_FH = 6
open_claim_type4 = {
    0 : 'CLAIM_NULL',
    1 : 'CLAIM_PREVIOUS',
    2 : 'CLAIM_DELEGATE_CUR',
    3 : 'CLAIM_DELEGATE_PREV',
    4 : 'CLAIM_FH',
    5 : 'CLAIM_DELEG_CUR_FH',
    6 : 'CLAIM_DELEG_PREV_FH',
}
WND4_NOT_WANTED = 0
WND4_CONTENTION = 1
WND4_RESOURCE = 2
WND4_NOT_SUPP_FTYPE = 3
WND4_WRITE_DELEG_NOT_SUPP_FTYPE = 4
WND4_NOT_SUPP_UPGRADE = 5
WND4_NOT_SUPP_DOWNGRADE = 6
WND4_CANCELLED = 7
WND4_IS_DIR = 8
why_no_delegation4 = {
    0 : 'WND4_NOT_WANTED',
    1 : 'WND4_CONTENTION',
    2 : 'WND4_RESOURCE',
    3 : 'WND4_NOT_SUPP_FTYPE',
    4 : 'WND4_WRITE_DELEG_NOT_SUPP_FTYPE',
    5 : 'WND4_NOT_SUPP_UPGRADE',
    6 : 'WND4_NOT_SUPP_DOWNGRADE',
    7 : 'WND4_CANCELLED',
    8 : 'WND4_IS_DIR',
}
OPEN4_RESULT_CONFIRM = 0x00000002
OPEN4_RESULT_LOCKTYPE_POSIX = 0x00000004
OPEN4_RESULT_PRESERVE_UNLINKED = 0x00000008
OPEN4_RESULT_MAY_NOTIFY_LOCK = 0x00000020
RPC_GSS_SVC_NONE = 1
RPC_GSS_SVC_INTEGRITY = 2
RPC_GSS_SVC_PRIVACY = 3
rpc_gss_svc_t = {
    1 : 'RPC_GSS_SVC_NONE',
    2 : 'RPC_GSS_SVC_INTEGRITY',
    3 : 'RPC_GSS_SVC_PRIVACY',
}
CDFC4_FORE = 0x1
CDFC4_BACK = 0x2
CDFC4_FORE_OR_BOTH = 0x3
CDFC4_BACK_OR_BOTH = 0x7
channel_dir_from_client4 = {
    0x1 : 'CDFC4_FORE',
    0x2 : 'CDFC4_BACK',
    0x3 : 'CDFC4_FORE_OR_BOTH',
    0x7 : 'CDFC4_BACK_OR_BOTH',
}
CDFS4_FORE = 0x1
CDFS4_BACK = 0x2
CDFS4_BOTH = 0x3
channel_dir_from_server4 = {
    0x1 : 'CDFS4_FORE',
    0x2 : 'CDFS4_BACK',
    0x3 : 'CDFS4_BOTH',
}
EXCHGID4_FLAG_SUPP_MOVED_REFER = 0x00000001
EXCHGID4_FLAG_SUPP_MOVED_MIGR = 0x00000002
EXCHGID4_FLAG_SUPP_FENCE_OPS = 0x00000004
EXCHGID4_FLAG_BIND_PRINC_STATEID = 0x00000100
EXCHGID4_FLAG_USE_NON_PNFS = 0x00010000
EXCHGID4_FLAG_USE_PNFS_MDS = 0x00020000
EXCHGID4_FLAG_USE_PNFS_DS = 0x00040000
EXCHGID4_FLAG_MASK_PNFS = 0x00070000
EXCHGID4_FLAG_UPD_CONFIRMED_REC_A = 0x40000000
EXCHGID4_FLAG_CONFIRMED_R = 0x80000000
SP4_NONE = 0
SP4_MACH_CRED = 1
SP4_SSV = 2
state_protect_how4 = {
    0 : 'SP4_NONE',
    1 : 'SP4_MACH_CRED',
    2 : 'SP4_SSV',
}
CREATE_SESSION4_FLAG_PERSIST = 0x00000001
CREATE_SESSION4_FLAG_CONN_BACK_CHAN = 0x00000002
CREATE_SESSION4_FLAG_CONN_RDMA = 0x00000004
GDD4_OK = 0
GDD4_UNAVAIL = 1
gddrnf4_status = {
    0 : 'GDD4_OK',
    1 : 'GDD4_UNAVAIL',
}
SECINFO_STYLE4_CURRENT_FH = 0
SECINFO_STYLE4_PARENT = 1
secinfo_style4 = {
    0 : 'SECINFO_STYLE4_CURRENT_FH',
    1 : 'SECINFO_STYLE4_PARENT',
}
SEQ4_STATUS_CB_PATH_DOWN = 0x00000001
SEQ4_STATUS_CB_GSS_CONTEXTS_EXPIRING = 0x00000002
SEQ4_STATUS_CB_GSS_CONTEXTS_EXPIRED = 0x00000004
SEQ4_STATUS_EXPIRED_ALL_STATE_REVOKED = 0x00000008
SEQ4_STATUS_EXPIRED_SOME_STATE_REVOKED = 0x00000010
SEQ4_STATUS_ADMIN_STATE_REVOKED = 0x00000020
SEQ4_STATUS_RECALLABLE_STATE_REVOKED = 0x00000040
SEQ4_STATUS_LEASE_MOVED = 0x00000080
SEQ4_STATUS_RESTART_RECLAIM_NEEDED = 0x00000100
SEQ4_STATUS_CB_PATH_DOWN_SESSION = 0x00000200
SEQ4_STATUS_BACKCHANNEL_FAULT = 0x00000400
SEQ4_STATUS_DEVID_CHANGED = 0x00000800
SEQ4_STATUS_DEVID_DELETED = 0x00001000
IO_ADVISE4_NORMAL = 0
IO_ADVISE4_SEQUENTIAL = 1
IO_ADVISE4_SEQUENTIAL_BACKWARDS = 2
IO_ADVISE4_RANDOM = 3
IO_ADVISE4_WILLNEED = 4
IO_ADVISE4_WILLNEED_OPPORTUNISTIC = 5
IO_ADVISE4_DONTNEED = 6
IO_ADVISE4_NOREUSE = 7
IO_ADVISE4_READ = 8
IO_ADVISE4_WRITE = 9
IO_ADVISE4_INIT_PROXIMITY = 10
IO_ADVISE_type4 = {
    0 : 'IO_ADVISE4_NORMAL',
    1 : 'IO_ADVISE4_SEQUENTIAL',
    2 : 'IO_ADVISE4_SEQUENTIAL_BACKWARDS',
    3 : 'IO_ADVISE4_RANDOM',
    4 : 'IO_ADVISE4_WILLNEED',
    5 : 'IO_ADVISE4_WILLNEED_OPPORTUNISTIC',
    6 : 'IO_ADVISE4_DONTNEED',
    7 : 'IO_ADVISE4_NOREUSE',
    8 : 'IO_ADVISE4_READ',
    9 : 'IO_ADVISE4_WRITE',
    10 : 'IO_ADVISE4_INIT_PROXIMITY',
}
FF_FLAGS_NO_LAYOUTCOMMIT = 0x00000001
FF_FLAGS_NO_IO_THRU_MDS = 0x00000002
FF_FLAGS_NO_READ_IO = 0x00000004
FF_RCA4_TYPE_MASK_READ = -2
FF_RCA4_TYPE_MASK_RW = -1
ff_cb_recall_any_mask = {
    -2 : 'FF_RCA4_TYPE_MASK_READ',
    -1 : 'FF_RCA4_TYPE_MASK_RW',
}
SETXATTR4_EITHER = 0
SETXATTR4_CREATE = 1
SETXATTR4_REPLACE = 2
setxattr_option4 = {
    0 : 'SETXATTR4_EITHER',
    1 : 'SETXATTR4_CREATE',
    2 : 'SETXATTR4_REPLACE',
}
NFS4_PROGRAM = 100003
NFS_V4 = 4
LAYOUTRECALL4_FILE = LAYOUT4_RET_REC_FILE
LAYOUTRECALL4_FSID = LAYOUT4_RET_REC_FSID
LAYOUTRECALL4_ALL = LAYOUT4_RET_REC_ALL
layoutrecall_type4 = {
    LAYOUT4_RET_REC_FILE : 'LAYOUTRECALL4_FILE',
    LAYOUT4_RET_REC_FSID : 'LAYOUTRECALL4_FSID',
    LAYOUT4_RET_REC_ALL : 'LAYOUTRECALL4_ALL',
}
NOTIFY4_CHANGE_CHILD_ATTRS = 0
NOTIFY4_CHANGE_DIR_ATTRS = 1
NOTIFY4_REMOVE_ENTRY = 2
NOTIFY4_ADD_ENTRY = 3
NOTIFY4_RENAME_ENTRY = 4
NOTIFY4_CHANGE_COOKIE_VERIFIER = 5
notify_type4 = {
    0 : 'NOTIFY4_CHANGE_CHILD_ATTRS',
    1 : 'NOTIFY4_CHANGE_DIR_ATTRS',
    2 : 'NOTIFY4_REMOVE_ENTRY',
    3 : 'NOTIFY4_ADD_ENTRY',
    4 : 'NOTIFY4_RENAME_ENTRY',
    5 : 'NOTIFY4_CHANGE_COOKIE_VERIFIER',
}
RCA4_TYPE_MASK_RDATA_DLG = 0
RCA4_TYPE_MASK_WDATA_DLG = 1
RCA4_TYPE_MASK_DIR_DLG = 2
RCA4_TYPE_MASK_FILE_LAYOUT = 3
RCA4_TYPE_MASK_BLK_LAYOUT = 4
RCA4_TYPE_MASK_OBJ_LAYOUT_MIN = 8
RCA4_TYPE_MASK_OBJ_LAYOUT_MAX = 9
RCA4_TYPE_MASK_OTHER_LAYOUT_MIN = 12
RCA4_TYPE_MASK_OTHER_LAYOUT_MAX = 15
NOTIFY_DEVICEID4_CHANGE = 1
NOTIFY_DEVICEID4_DELETE = 2
notify_deviceid_type4 = {
    1 : 'NOTIFY_DEVICEID4_CHANGE',
    2 : 'NOTIFY_DEVICEID4_DELETE',
}
OP_CB_GETATTR = 3
OP_CB_RECALL = 4
OP_CB_LAYOUTRECALL = 5
OP_CB_NOTIFY = 6
OP_CB_PUSH_DELEG = 7
OP_CB_RECALL_ANY = 8
OP_CB_RECALLABLE_OBJ_AVAIL = 9
OP_CB_RECALL_SLOT = 10
OP_CB_SEQUENCE = 11
OP_CB_WANTS_CANCELLED = 12
OP_CB_NOTIFY_LOCK = 13
OP_CB_NOTIFY_DEVICEID = 14
OP_CB_OFFLOAD = 15
OP_CB_ILLEGAL = 10044
nfs_cb_opnum4 = {
    3 : 'OP_CB_GETATTR',
    4 : 'OP_CB_RECALL',
    5 : 'OP_CB_LAYOUTRECALL',
    6 : 'OP_CB_NOTIFY',
    7 : 'OP_CB_PUSH_DELEG',
    8 : 'OP_CB_RECALL_ANY',
    9 : 'OP_CB_RECALLABLE_OBJ_AVAIL',
    10 : 'OP_CB_RECALL_SLOT',
    11 : 'OP_CB_SEQUENCE',
    12 : 'OP_CB_WANTS_CANCELLED',
    13 : 'OP_CB_NOTIFY_LOCK',
    14 : 'OP_CB_NOTIFY_DEVICEID',
    15 : 'OP_CB_OFFLOAD',
    10044 : 'OP_CB_ILLEGAL',
}
NFS4_CALLBACK = 0x40000000
NFS_CB = 1
FATTR4_OFFLINE = 83
OPEN_ARGS_SHARE_ACCESS_READ = 1
OPEN_ARGS_SHARE_ACCESS_WRITE = 2
OPEN_ARGS_SHARE_ACCESS_BOTH = 3
open_args_share_access4 = {
    1 : 'OPEN_ARGS_SHARE_ACCESS_READ',
    2 : 'OPEN_ARGS_SHARE_ACCESS_WRITE',
    3 : 'OPEN_ARGS_SHARE_ACCESS_BOTH',
}
OPEN_ARGS_SHARE_DENY_NONE = 0
OPEN_ARGS_SHARE_DENY_READ = 1
OPEN_ARGS_SHARE_DENY_WRITE = 2
OPEN_ARGS_SHARE_DENY_BOTH = 3
open_args_share_deny4 = {
    0 : 'OPEN_ARGS_SHARE_DENY_NONE',
    1 : 'OPEN_ARGS_SHARE_DENY_READ',
    2 : 'OPEN_ARGS_SHARE_DENY_WRITE',
    3 : 'OPEN_ARGS_SHARE_DENY_BOTH',
}
OPEN_ARGS_SHARE_ACCESS_WANT_ANY_DELEG = 3
OPEN_ARGS_SHARE_ACCESS_WANT_NO_DELEG = 4
OPEN_ARGS_SHARE_ACCESS_WANT_CANCEL = 5
OPEN_ARGS_SHARE_ACCESS_WANT_SIGNAL_DELEG_WHEN_RESRC_AVAIL = 17
OPEN_ARGS_SHARE_ACCESS_WANT_PUSH_DELEG_WHEN_UNCONTENDED = 18
OPEN_ARGS_SHARE_ACCESS_WANT_DELEG_TIMESTAMPS = 20
OPEN_ARGS_SHARE_ACCESS_WANT_OPEN_XOR_DELEGATION = 21
open_args_share_access_want4 = {
    3 : 'OPEN_ARGS_SHARE_ACCESS_WANT_ANY_DELEG',
    4 : 'OPEN_ARGS_SHARE_ACCESS_WANT_NO_DELEG',
    5 : 'OPEN_ARGS_SHARE_ACCESS_WANT_CANCEL',
    17 : 'OPEN_ARGS_SHARE_ACCESS_WANT_SIGNAL_DELEG_WHEN_RESRC_AVAIL',
    18 : 'OPEN_ARGS_SHARE_ACCESS_WANT_PUSH_DELEG_WHEN_UNCONTENDED',
    20 : 'OPEN_ARGS_SHARE_ACCESS_WANT_DELEG_TIMESTAMPS',
    21 : 'OPEN_ARGS_SHARE_ACCESS_WANT_OPEN_XOR_DELEGATION',
}
OPEN_ARGS_OPEN_CLAIM_NULL = 0
OPEN_ARGS_OPEN_CLAIM_PREVIOUS = 1
OPEN_ARGS_OPEN_CLAIM_DELEGATE_CUR = 2
OPEN_ARGS_OPEN_CLAIM_DELEGATE_PREV = 3
OPEN_ARGS_OPEN_CLAIM_FH = 4
OPEN_ARGS_OPEN_CLAIM_DELEG_CUR_FH = 5
OPEN_ARGS_OPEN_CLAIM_DELEG_PREV_FH = 6
open_args_open_claim4 = {
    0 : 'OPEN_ARGS_OPEN_CLAIM_NULL',
    1 : 'OPEN_ARGS_OPEN_CLAIM_PREVIOUS',
    2 : 'OPEN_ARGS_OPEN_CLAIM_DELEGATE_CUR',
    3 : 'OPEN_ARGS_OPEN_CLAIM_DELEGATE_PREV',
    4 : 'OPEN_ARGS_OPEN_CLAIM_FH',
    5 : 'OPEN_ARGS_OPEN_CLAIM_DELEG_CUR_FH',
    6 : 'OPEN_ARGS_OPEN_CLAIM_DELEG_PREV_FH',
}
OPEN_ARGS_CREATEMODE_UNCHECKED4 = 0
OPEN_ARGS_CREATE_MODE_GUARDED = 1
OPEN_ARGS_CREATEMODE_EXCLUSIVE4 = 2
OPEN_ARGS_CREATE_MODE_EXCLUSIVE4_1 = 3
open_args_createmode4 = {
    0 : 'OPEN_ARGS_CREATEMODE_UNCHECKED4',
    1 : 'OPEN_ARGS_CREATE_MODE_GUARDED',
    2 : 'OPEN_ARGS_CREATEMODE_EXCLUSIVE4',
    3 : 'OPEN_ARGS_CREATE_MODE_EXCLUSIVE4_1',
}
FATTR4_OPEN_ARGUMENTS = 86
OPEN4_SHARE_ACCESS_WANT_OPEN_XOR_DELEGATION = 0x200000
OPEN4_RESULT_NO_OPEN_STATEID = 0x00000010
FATTR4_TIME_DELEG_ACCESS = 84
FATTR4_TIME_DELEG_MODIFY = 85
OPEN4_SHARE_ACCESS_WANT_DELEG_TIMESTAMPS = 0x100000
