# Generated by rpcgen.py from /home/pentest/Documents/pynfs/nfs4.1/xdrdef/pnfs_block.x on Fri May  3 15:00:32 2024
NFS4_DEVICEID4_SIZE = 16
PNFS_BLOCK_VOLUME_SIMPLE = 0
PNFS_BLOCK_VOLUME_SLICE = 1
PNFS_BLOCK_VOLUME_CONCAT = 2
PNFS_BLOCK_VOLUME_STRIPE = 3
pnfs_block_volume_type4 = {
    0 : 'PNFS_BLOCK_VOLUME_SIMPLE',
    1 : 'PNFS_BLOCK_VOLUME_SLICE',
    2 : 'PNFS_BLOCK_VOLUME_CONCAT',
    3 : 'PNFS_BLOCK_VOLUME_STRIPE',
}
PNFS_BLOCK_MAX_SIG_COMP = 16
PNFS_BLOCK_READWRITE_DATA = 0
PNFS_BLOCK_READ_DATA = 1
PNFS_BLOCK_INVALID_DATA = 2
PNFS_BLOCK_NONE_DATA = 3
pnfs_block_extent_state4 = {
    0 : 'PNFS_BLOCK_READWRITE_DATA',
    1 : 'PNFS_BLOCK_READ_DATA',
    2 : 'PNFS_BLOCK_INVALID_DATA',
    3 : 'PNFS_BLOCK_NONE_DATA',
}
RCA4_BLK_LAYOUT_RECALL_ANY_LAYOUTS = 4