# Generated by rpcgen.py from /home/pentest/Documents/pynfs/nfs4.1/xdrdef/sctrl.x on Fri May  3 15:00:32 2024
import sys,os
from . import sctrl_const as const
class resdata_t:
    # XDR definition:
    # union resdata_t switch(ctrl_opnum ctrlop) {
    #     case CTRL_GRAB:
    #         GRABres grab;
    #     default:
    #         void;
    # };
    def __init__(self, ctrlop=None, grab=None):
        self.ctrlop = ctrlop
        self.grab = grab

    switch = property(lambda s: {const.CTRL_GRAB:s.grab,}.get(s.ctrlop, None))

    def __getattr__(self, attr):
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.ctrlop is not None:
            out += ['ctrlop=%s' % const.ctrl_opnum.get(self.ctrlop, self.ctrlop)]
        if self.grab is not None:
            out += ['grab=%s' % repr(self.grab)]
        return 'resdata_t(%s)' % ', '.join(out)
    __str__ = __repr__

class CTRLres:
    # XDR definition:
    # struct CTRLres {
    #     stat_t status;
    #     resdata_t data;
    # };
    def __init__(self, status=None, data=None):
        self.status = status
        self.data = data

    def __getattr__(self, attr):
        return getattr(self.data, attr)

    def __repr__(self):
        out = []
        if self.status is not None:
            out += ['status=%s' % const.stat_t.get(self.status, self.status)]
        if self.data is not None:
            out += ['data=%s' % repr(self.data)]
        return 'CTRLres(%s)' % ', '.join(out)
    __str__ = __repr__

class RECORDarg:
    # XDR definition:
    # struct RECORDarg {
    #     str stamp;
    # };
    def __init__(self, stamp=None):
        self.stamp = stamp

    def __repr__(self):
        out = []
        if self.stamp is not None:
            out += ['stamp=%s' % repr(self.stamp)]
        return 'RECORDarg(%s)' % ', '.join(out)
    __str__ = __repr__

class GRABarg:
    # XDR definition:
    # struct GRABarg {
    #     int32_t number;
    #     dir_t dir;
    #     str stamp;
    # };
    def __init__(self, number=None, dir=None, stamp=None):
        self.number = number
        self.dir = dir
        self.stamp = stamp

    def __repr__(self):
        out = []
        if self.number is not None:
            out += ['number=%s' % repr(self.number)]
        if self.dir is not None:
            out += ['dir=%s' % const.dir_t.get(self.dir, self.dir)]
        if self.stamp is not None:
            out += ['stamp=%s' % repr(self.stamp)]
        return 'GRABarg(%s)' % ', '.join(out)
    __str__ = __repr__

class GRABres:
    # XDR definition:
    # struct GRABres {
    #     str calls<>;
    #     str replies<>;
    # };
    def __init__(self, calls=None, replies=None):
        self.calls = calls
        self.replies = replies

    def __repr__(self):
        out = []
        if self.calls is not None:
            out += ['calls=%s' % repr(self.calls)]
        if self.replies is not None:
            out += ['replies=%s' % repr(self.replies)]
        return 'GRABres(%s)' % ', '.join(out)
    __str__ = __repr__

class CTRLarg:
    # XDR definition:
    # union CTRLarg switch(ctrl_opnum ctrlop) {
    #     case CTRL_RESET:
    #         void;
    #     case CTRL_RECORD:
    #         RECORDarg record;
    #     case CTRL_PAUSE:
    #         void;
    #     case CTRL_GRAB:
    #         GRABarg grab;
    # };
    def __init__(self, ctrlop=None, record=None, grab=None):
        self.ctrlop = ctrlop
        self.record = record
        self.grab = grab

    switch = property(lambda s: {const.CTRL_RESET:None,const.CTRL_RECORD:s.record,const.CTRL_PAUSE:None,const.CTRL_GRAB:s.grab,}[s.ctrlop])

    def __getattr__(self, attr):
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.ctrlop is not None:
            out += ['ctrlop=%s' % const.ctrl_opnum.get(self.ctrlop, self.ctrlop)]
        if self.record is not None:
            out += ['record=%s' % repr(self.record)]
        if self.grab is not None:
            out += ['grab=%s' % repr(self.grab)]
        return 'CTRLarg(%s)' % ', '.join(out)
    __str__ = __repr__

