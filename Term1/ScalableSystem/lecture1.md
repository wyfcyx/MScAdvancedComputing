database design depends on the disk

queries together should be stored together

optimize for the disk pages, cache line

CSS no pointers for compression to make use of the cache line

CSB, a trade-off between CSS(query) and B+(update)

ML accelerate the indexing? but how to fit the cache line?

radix join: (too many partitions -> cache misses)

adjacent is not a physical concept cuz the plate is rotating

DBMS is based on the files managed by the OS