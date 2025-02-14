# Generated by rpcgen.py from /home/pentest/Documents/linux-pynfs/nfs4.1/./xdrdef/mnt3.x on Fri Feb 14 09:26:47 2025
import sys,os
from . import mnt3_const as const
class mountres3_ok:
    # XDR definition:
    # struct mountres3_ok {
    #     fhandle3 fhandle;
    #     int auth_flavors<>;
    # };
    def __init__(self, fhandle=None, auth_flavors=None):
        self.fhandle = fhandle
        self.auth_flavors = auth_flavors

    def __repr__(self):
        out = []
        if self.fhandle is not None:
            out += ['fhandle=%s' % repr(self.fhandle)]
        if self.auth_flavors is not None:
            out += ['auth_flavors=%s' % repr(self.auth_flavors)]
        return 'mountres3_ok(%s)' % ', '.join(out)
    __str__ = __repr__

class mountres3:
    # XDR definition:
    # union mountres3 switch(mountstat3 fhs_status) {
    #     case MNT3_OK:
    #         mountres3_ok mountinfo;
    #     default:
    #         void;
    # };
    def __init__(self, fhs_status=None, mountinfo=None):
        self.fhs_status = fhs_status
        self.mountinfo = mountinfo

    switch = property(lambda s: {const.MNT3_OK:s.mountinfo,}.get(s.fhs_status, None))

    def __getattr__(self, attr):
        return getattr(self.switch, attr)

    def __repr__(self):
        out = []
        if self.fhs_status is not None:
            out += ['fhs_status=%s' % const.mountstat3.get(self.fhs_status, self.fhs_status)]
        if self.mountinfo is not None:
            out += ['mountinfo=%s' % repr(self.mountinfo)]
        return 'mountres3(%s)' % ', '.join(out)
    __str__ = __repr__

class mountbody:
    # XDR definition:
    # struct mountbody {
    #     name ml_hostname;
    #     dirpath ml_directory;
    #     mountlist ml_next;
    # };
    def __init__(self, ml_hostname=None, ml_directory=None, ml_next=None):
        self.ml_hostname = ml_hostname
        self.ml_directory = ml_directory
        self.ml_next = ml_next

    def __repr__(self):
        out = []
        if self.ml_hostname is not None:
            out += ['ml_hostname=%s' % repr(self.ml_hostname)]
        if self.ml_directory is not None:
            out += ['ml_directory=%s' % repr(self.ml_directory)]
        if self.ml_next is not None:
            out += ['ml_next=%s' % repr(self.ml_next)]
        return 'mountbody(%s)' % ', '.join(out)
    __str__ = __repr__

class groupnode:
    # XDR definition:
    # struct groupnode {
    #     name gr_name;
    #     groups gr_next;
    # };
    def __init__(self, gr_name=None, gr_next=None):
        self.gr_name = gr_name
        self.gr_next = gr_next

    def __repr__(self):
        out = []
        if self.gr_name is not None:
            out += ['gr_name=%s' % repr(self.gr_name)]
        if self.gr_next is not None:
            out += ['gr_next=%s' % repr(self.gr_next)]
        return 'groupnode(%s)' % ', '.join(out)
    __str__ = __repr__

class exportnode:
    # XDR definition:
    # struct exportnode {
    #     dirpath ex_dir;
    #     groups ex_groups;
    #     exports ex_next;
    # };
    def __init__(self, ex_dir=None, ex_groups=None, ex_next=None):
        self.ex_dir = ex_dir
        self.ex_groups = ex_groups
        self.ex_next = ex_next

    def __repr__(self):
        out = []
        if self.ex_dir is not None:
            out += ['ex_dir=%s' % repr(self.ex_dir)]
        if self.ex_groups is not None:
            out += ['ex_groups=%s' % repr(self.ex_groups)]
        if self.ex_next is not None:
            out += ['ex_next=%s' % repr(self.ex_next)]
        return 'exportnode(%s)' % ', '.join(out)
    __str__ = __repr__

