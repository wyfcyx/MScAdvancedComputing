HPC: a single problem, of high value, relatively simple, supported by special hardware

Performance Engineering: focus on *systems*, complex, flexible

definition of system: be flexible at runtime, handle all kinds of workloads, domain-agnostic, developed over years(thus should be maintainable), 

trade-off triangle of systems: maintainable - flexible - fast

Step1: define a target metric

interesting metrics: energy consumption, TCO, elasticity(how fast a high throughput system transfers to another system)

Step2: setting an optimization budget(easier) or setting an optimization target/threshold(harder, for example, soft/hard RT requirements)

Quality-of-Service objectives: required metrics depending on some pre-conditions, tricky, from users, sometimes **in conflict** with functional requirements

Service-Level-Agreements(SLA), legal contract specifying QoS objectives, penalties for violations,

When defining requirements: SMART(Specific, Measurable, Acceptable[achievable in reality], Realizable, Thorough)

this course focuses on "measurable"

Measuring:

* Monitoring: measuring in production, maybe required to enforce SLA, incur runtime cost, not continuous

* Benchmarking: measuring in the lab, operations(smaller than production workload) when the system is in a predefined state

  benchmark workload: can be a batch(with all release time equaling to 0), measure throughput, do not care generator's performance; can be interactive, from generator to system, measure latency, generator should be faster than the system otherwise it will become the bottleneck of the evaluation; also can be hybrid

Interpreting the measurement: aggregate multiple run and report some measure of variance

Optimization & tuning:

parameters: system params,  do not change during runtime; workload params, may change during runtime(number of users, available memory)

numerical versus nominal parameters(target device classes such as phones, laptops, ...)

utilization; bottleneck: **the resource with the highest utilization**, for example: CPU-bound, memory-bound, disk-bound applications, also latency-bound means that the system is always waiting

But, hard to identify bottlenecks in a complex system! Instead we focus on performance-dominating code path including critical path(longest sequential path) and hot path(takes the most time)

Improving performance: for example, tuning system parameters so that resource consumption is minimized and performance metric is maximized(using analytical models instead of searching)

simulation: a single observed run of a stateful model

 



 