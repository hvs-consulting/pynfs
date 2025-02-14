# Generated by rpcgen.py from ./rpc.x on Fri Feb 14 09:26:47 2025
import sys,os
from . import rpc_const as const
class opaque_auth:
    # XDR definition:
    # struct opaque_auth {
    #     auth_flavor flavor;
    #     opaque body<400>;
    # };
    def __init__(self, flavor=None, body=None):
        self.flavor = flavor
        self.body = body

    def __repr__(self):
        out = []
        if self.flavor is not None:
            out += ['flavor=%s' % const.auth_flavor.get(self.flavor, self.flavor)]
        if self.body is not None:
            out += ['body=%s' % repr(self.body)]
        return 'opaque_auth(%s)' % ', '.join(out)
    __str__ = __repr__

class rpc_msg:
    # XDR definition:
    # struct rpc_msg {
    #     uint xid;
    #     rpc_msg_body body;
    # };
    def __init__(self, xid=None, body=None):
        self.xid = xid
        self.body = body

    def __getattr__(self, attr):
        return getattr(self.body, attr)

    def __repr__(self):
        out = []
        if self.xid is not None:
            out += ['xid=%s' % repr(self.xid)]
        if self.body is not None:
            out += ['body=%s' % repr(self.body)]
        return 'rpc_msg(%s)' % ', '.join(out)
    __str__ = __repr__

class rpc_msg_body:
    # XDR definition:
    # union rpc_msg_body switch(msg_type mtype) {
    #     case CALL:
    #         call_body cbody;
    #     case REPLY:
    #         reply_body rbody;
    # };
    def __init__(self, mtype=None, cbody=None, rbody=None):
        self.mtype = mtype
        self.cbody = cbody
        self.rbody = rbody

    switch = property(lambda s: {const.CALL:s.cbody,const.REPLY:s.rbody,}[s.mtype])

    def __getattr__(self, attr):
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.mtype is not None:
            out += ['mtype=%s' % const.msg_type.get(self.mtype, self.mtype)]
        if self.cbody is not None:
            out += ['cbody=%s' % repr(self.cbody)]
        if self.rbody is not None:
            out += ['rbody=%s' % repr(self.rbody)]
        return 'rpc_msg_body(%s)' % ', '.join(out)
    __str__ = __repr__

class call_body:
    # XDR definition:
    # struct call_body {
    #     uint rpcvers;
    #     uint prog;
    #     uint vers;
    #     uint proc;
    #     opaque_auth cred;
    #     opaque_auth verf;
    # };
    def __init__(self, rpcvers=None, prog=None, vers=None, proc=None, cred=None, verf=None):
        self.rpcvers = rpcvers
        self.prog = prog
        self.vers = vers
        self.proc = proc
        self.cred = cred
        self.verf = verf

    def __repr__(self):
        out = []
        if self.rpcvers is not None:
            out += ['rpcvers=%s' % repr(self.rpcvers)]
        if self.prog is not None:
            out += ['prog=%s' % repr(self.prog)]
        if self.vers is not None:
            out += ['vers=%s' % repr(self.vers)]
        if self.proc is not None:
            out += ['proc=%s' % repr(self.proc)]
        if self.cred is not None:
            out += ['cred=%s' % repr(self.cred)]
        if self.verf is not None:
            out += ['verf=%s' % repr(self.verf)]
        return 'call_body(%s)' % ', '.join(out)
    __str__ = __repr__

class reply_body:
    # XDR definition:
    # union reply_body switch(reply_stat stat) {
    #     case MSG_ACCEPTED:
    #         accepted_reply areply;
    #     case MSG_DENIED:
    #         rejected_reply rreply;
    # };
    def __init__(self, stat=None, areply=None, rreply=None):
        self.stat = stat
        self.areply = areply
        self.rreply = rreply

    switch = property(lambda s: {const.MSG_ACCEPTED:s.areply,const.MSG_DENIED:s.rreply,}[s.stat])

    def __getattr__(self, attr):
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.stat is not None:
            out += ['stat=%s' % const.reply_stat.get(self.stat, self.stat)]
        if self.areply is not None:
            out += ['areply=%s' % repr(self.areply)]
        if self.rreply is not None:
            out += ['rreply=%s' % repr(self.rreply)]
        return 'reply_body(%s)' % ', '.join(out)
    __str__ = __repr__

class rpc_mismatch_info:
    # XDR definition:
    # struct rpc_mismatch_info {
    #     uint low;
    #     uint high;
    # };
    def __init__(self, low=None, high=None):
        self.low = low
        self.high = high

    def __repr__(self):
        out = []
        if self.low is not None:
            out += ['low=%s' % repr(self.low)]
        if self.high is not None:
            out += ['high=%s' % repr(self.high)]
        return 'rpc_mismatch_info(%s)' % ', '.join(out)
    __str__ = __repr__

class rpc_reply_data:
    # XDR definition:
    # union rpc_reply_data switch(accept_stat stat) {
    #     case SUCCESS:
    #         opaque results[0];
    #     case PROG_MISMATCH:
    #         rpc_mismatch_info mismatch_info;
    #     default:
    #         void;
    # };
    def __init__(self, stat=None, results=None, mismatch_info=None):
        self.stat = stat
        self.results = results
        self.mismatch_info = mismatch_info

    switch = property(lambda s: {const.SUCCESS:s.results,const.PROG_MISMATCH:s.mismatch_info,}.get(s.stat, None))

    def __getattr__(self, attr):
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.stat is not None:
            out += ['stat=%s' % const.accept_stat.get(self.stat, self.stat)]
        if self.results is not None:
            out += ['results=%s' % repr(self.results)]
        if self.mismatch_info is not None:
            out += ['mismatch_info=%s' % repr(self.mismatch_info)]
        return 'rpc_reply_data(%s)' % ', '.join(out)
    __str__ = __repr__

class accepted_reply:
    # XDR definition:
    # struct accepted_reply {
    #     opaque_auth verf;
    #     rpc_reply_data reply_data;
    # };
    def __init__(self, verf=None, reply_data=None):
        self.verf = verf
        self.reply_data = reply_data

    def __repr__(self):
        out = []
        if self.verf is not None:
            out += ['verf=%s' % repr(self.verf)]
        if self.reply_data is not None:
            out += ['reply_data=%s' % repr(self.reply_data)]
        return 'accepted_reply(%s)' % ', '.join(out)
    __str__ = __repr__

class rejected_reply:
    # XDR definition:
    # union rejected_reply switch(reject_stat stat) {
    #     case RPC_MISMATCH:
    #         rpc_mismatch_info mismatch_info;
    #     case AUTH_ERROR:
    #         auth_stat astat;
    # };
    def __init__(self, stat=None, mismatch_info=None, astat=None):
        self.stat = stat
        self.mismatch_info = mismatch_info
        self.astat = astat

    switch = property(lambda s: {const.RPC_MISMATCH:s.mismatch_info,const.AUTH_ERROR:s.astat,}[s.stat])

    def __getattr__(self, attr):
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.stat is not None:
            out += ['stat=%s' % const.reject_stat.get(self.stat, self.stat)]
        if self.mismatch_info is not None:
            out += ['mismatch_info=%s' % repr(self.mismatch_info)]
        if self.astat is not None:
            out += ['astat=%s' % const.auth_stat.get(self.astat, self.astat)]
        return 'rejected_reply(%s)' % ', '.join(out)
    __str__ = __repr__

class authsys_parms:
    # XDR definition:
    # struct authsys_parms {
    #     uint stamp;
    #     string machinename<255>;
    #     uint uid;
    #     uint gid;
    #     uint gids<16>;
    # };
    def __init__(self, stamp=None, machinename=None, uid=None, gid=None, gids=None):
        self.stamp = stamp
        self.machinename = machinename
        self.uid = uid
        self.gid = gid
        self.gids = gids

    def __repr__(self):
        out = []
        if self.stamp is not None:
            out += ['stamp=%s' % repr(self.stamp)]
        if self.machinename is not None:
            out += ['machinename=%s' % repr(self.machinename)]
        if self.uid is not None:
            out += ['uid=%s' % repr(self.uid)]
        if self.gid is not None:
            out += ['gid=%s' % repr(self.gid)]
        if self.gids is not None:
            out += ['gids=%s' % repr(self.gids)]
        return 'authsys_parms(%s)' % ', '.join(out)
    __str__ = __repr__

