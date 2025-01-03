const PMAP_PORT = 111;      /* portmapper port number */

struct mapping {
	unsigned int prog;
	unsigned int vers;
	unsigned int prot;
	unsigned int port;
};

const IPPROTO_TCP = 6;      /* protocol number for TCP/IP */
const IPPROTO_UDP = 17;     /* protocol number for UDP/IP */

struct pmaplist {
	mapping map;
	pmaplistptr next;
};

typedef pmaplist *pmaplistptr;

struct call_args {
	unsigned int prog;
	unsigned int vers;
	unsigned int proc;
	opaque args<>;
};

struct call_result {
	unsigned int port;
	opaque res<>;
};

program PMAP_PROG {
	version PMAP_VERS {
		void
		PMAPPROC_NULL(void)         = 0;

		bool
		PMAPPROC_SET(mapping)       = 1;

		bool
		PMAPPROC_UNSET(mapping)     = 2;

		unsigned int
		PMAPPROC_GETPORT(mapping)   = 3;

		pmaplist
		PMAPPROC_DUMP(void)         = 4;

		call_result
		PMAPPROC_CALLIT(call_args)  = 5;
	} = 2;
} = 100000;

