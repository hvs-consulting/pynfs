# Generated by rpcgen.py from rpc.x on Fri May  3 15:00:31 2024
AUTH_NONE = 0
AUTH_SYS = 1
AUTH_SHORT = 2
AUTH_DH = 3
RPCSEC_GSS = 6
auth_flavor = {
    0 : 'AUTH_NONE',
    1 : 'AUTH_SYS',
    2 : 'AUTH_SHORT',
    3 : 'AUTH_DH',
    6 : 'RPCSEC_GSS',
}
CALL = 0
REPLY = 1
msg_type = {
    0 : 'CALL',
    1 : 'REPLY',
}
MSG_ACCEPTED = 0
MSG_DENIED = 1
reply_stat = {
    0 : 'MSG_ACCEPTED',
    1 : 'MSG_DENIED',
}
SUCCESS = 0
PROG_UNAVAIL = 1
PROG_MISMATCH = 2
PROC_UNAVAIL = 3
GARBAGE_ARGS = 4
SYSTEM_ERR = 5
accept_stat = {
    0 : 'SUCCESS',
    1 : 'PROG_UNAVAIL',
    2 : 'PROG_MISMATCH',
    3 : 'PROC_UNAVAIL',
    4 : 'GARBAGE_ARGS',
    5 : 'SYSTEM_ERR',
}
RPC_MISMATCH = 0
AUTH_ERROR = 1
reject_stat = {
    0 : 'RPC_MISMATCH',
    1 : 'AUTH_ERROR',
}
AUTH_OK = 0
AUTH_BADCRED = 1
AUTH_REJECTEDCRED = 2
AUTH_BADVERF = 3
AUTH_REJECTEDVERF = 4
AUTH_TOOWEAK = 5
AUTH_INVALIDRESP = 6
AUTH_FAILED = 7
AUTH_KERB_GENERIC = 8
AUTH_TIMEEXPIRE = 9
AUTH_TKT_FILE = 10
AUTH_DECODE = 11
AUTH_NET_ADDR = 12
RPCSEC_GSS_CREDPROBLEM = 13
RPCSEC_GSS_CTXPROBLEM = 14
auth_stat = {
    0 : 'AUTH_OK',
    1 : 'AUTH_BADCRED',
    2 : 'AUTH_REJECTEDCRED',
    3 : 'AUTH_BADVERF',
    4 : 'AUTH_REJECTEDVERF',
    5 : 'AUTH_TOOWEAK',
    6 : 'AUTH_INVALIDRESP',
    7 : 'AUTH_FAILED',
    8 : 'AUTH_KERB_GENERIC',
    9 : 'AUTH_TIMEEXPIRE',
    10 : 'AUTH_TKT_FILE',
    11 : 'AUTH_DECODE',
    12 : 'AUTH_NET_ADDR',
    13 : 'RPCSEC_GSS_CREDPROBLEM',
    14 : 'RPCSEC_GSS_CTXPROBLEM',
}
