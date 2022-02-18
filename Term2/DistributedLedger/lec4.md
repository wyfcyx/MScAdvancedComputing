classical consensus

timing models: async/sync/eventually sync(mixed, upper bound varies)

fault models: f out of N can fail; honest nodes, always available; availability/byzantine failure

broadcast models: consistent models; reliable models(termination, reliability, consistency)??

algorithms: leader election; safety(consistent output); liveness

timing assumption is required; randomness is crucial

for any protocol: several questions...

relationship to bitcoin: do not need to know participants upfront

---

bitcoin bootstrapping

find peers: DNS bootstrap/static IPs/chats of forums

---

DoS protection

wrong signature->blacklist for 24h(penalty 100)

shared node can be banned by others(like TOR)

---

network gossip protocol

propagation methods

---

LIVE: N-confirmation, for a transaction, include it in the blockchain after N blocks, which means that it is more likely to be accepted by more nodes



