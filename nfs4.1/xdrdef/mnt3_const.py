# Generated by rpcgen.py from /home/pentest/Documents/linux-pynfs/nfs4.1/./xdrdef/mnt3.x on Fri Feb 14 09:26:47 2025
MOUNTPROC3_NULL = 0
MOUNTPROC3_MNT = 1
MOUNTPROC3_DUMP = 2
MOUNTPROC3_UMNT = 3
MOUNTPROC3_UMNTALL = 4
MOUNTPROC3_EXPORT = 5
MNTPATHLEN = 1024
MNTNAMLEN = 255
FHSIZE3 = 64
MNT3_OK = 0
MNT3ERR_PERM = 1
MNT3ERR_NOENT = 2
MNT3ERR_IO = 5
MNT3ERR_ACCES = 13
MNT3ERR_NOTDIR = 20
MNT3ERR_INVAL = 22
MNT3ERR_NAMETOOLONG = 63
MNT3ERR_NOTSUPP = 10004
MNT3ERR_SERVERFAULT = 10006
mountstat3 = {
    0 : 'MNT3_OK',
    1 : 'MNT3ERR_PERM',
    2 : 'MNT3ERR_NOENT',
    5 : 'MNT3ERR_IO',
    13 : 'MNT3ERR_ACCES',
    20 : 'MNT3ERR_NOTDIR',
    22 : 'MNT3ERR_INVAL',
    63 : 'MNT3ERR_NAMETOOLONG',
    10004 : 'MNT3ERR_NOTSUPP',
    10006 : 'MNT3ERR_SERVERFAULT',
}
MOUNT_PROGRAM = 100005
MOUNT_V3 = 3
