# Course work 1

Yifan Wu

## Problem a

Question I): Phase-change memory. It has a lower access latency compared to SSD.

Question II): FTL is a complicated software driver or firmware. Its main purpose is balancing the distribution of the data on the flash to extend the lifetime of the flash.

Question III): SSD has a lower random read access time compared to magnetic disks, but their sequential access time are the same. This is because the random access time of SSD does not depend on the location of the block to be accessed. However, for magnetic disks, if the locations of two adjacent accesses are far away from each other, then it will take a large amount of time to wait the disk to rotate. The reason why SSD's random write accesses is slower than its random read accesses is that every write access requires a block copy and deletion, and SSD cannot write multiple blocks at a time like read. Because we need apply a high voltage to the SSD to erase a block, if erase block size is equal to the read block size then it will waste energy.

## Problem b

Question I):

track capacity=1KB\*50=51,200bytes, surface capacity=51,200bytes\*400=20,480,000bytes, 

disk capacity=20,480,000bytes\*5\*2=204,800,000bytes.

This disk has 50\*400\*5\*2=200,000 block since block size and sector size are equal.

Question II):

Each block can only store 10 records, so 1,000 blocks are required to store this file.

Wasted space: 24bytes\*1,000=24,000bytes.

No, there is not. This is because all the positions on the main memory can be used to store records.

1/3 memory bandwidth is wasted since 2 cache lines with 150 bytes are fetched in order to access a record but only 100 bytes of them are actually used.



## problem c

Question I):

access time: if a storage media has a long access time, it will become the bottleneck of the system.

capacity: if a storage media does not have enough capacity, it will also limit the total throughput.

Question II):

PCM has a good access time, so transactions of VoltDB can be fast on PCM.

However, PCM's density is low, which limits PCM's capacity and size of the data involved in the VoltDB's transactions.

## problem d



Question I): XML is based on tagged trees, but JSON/BSON are based on key-value pairs. XML does not allow cycles since it is a tree.

Question II):

Model-mapping is preferable when the XML does not rely on DTD information. Conversely, structure-mapping is preferable when XML relies on DTD information. MongoDB is based on collections and it does not have a fixed scheme, but structure-mapping's scheme is based on DTD thus it is fixed.