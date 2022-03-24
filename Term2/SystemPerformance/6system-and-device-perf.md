data movement(when IPC) consume more energy

abstraction overhead, when it is based on hardware it is smaller, but not zero

for example, virtualization(instruction such as `rdtscp`, trap into the hypervisor, a huge overhead); page table(page table walking is hard to predict since there are too many HW involved), VM multiple this cost; memory tiering; CPU-memory bus overhead, for example: protocol, congestion;

polling devices leads to a huge PCIe overhead

cache-coherent MMIO: example: OpenCAPI

blocking I/O overhead: 2 privilege level switches due to a system call; data copy, data cannot be directly written to user space; 2 context switches due to resched;   

non-blocking I/O: async(notified by signals?) versus events;

Linux async I/O interface

`io_uring`

application-specific direct device assignment: device support multiple 'instances', call virtual functions which is originally designed for virtualization; example: DPDK(for network) and SPDK(for storage)



