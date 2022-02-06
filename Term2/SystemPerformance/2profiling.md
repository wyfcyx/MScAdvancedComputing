how identify opt opportunities, hot path/bottleneck, that are system behaviors

how to define system behaviors

events(tracing and profiling): change of system state, restrained to a certain granularity, simple/complex, with payload/accuracy

do with events: where they come from(event sources)/where they go(tracing/profiling)

tracing: log of ordered events, describing the changes of the system, high collecting overhead

> example: call stack tracing, quite expensive overhead

perturbation: the degree to which the perf of the system changes when its analyzed, may negative affects the accuracy

reduce perturbation: by reducing fidelity(correctness of a copy/reproduction), not recording every event

for example: sampling, sample in regular/random intervals

sampling intervals: time-based(computer clock rates vary, not sync among CPUs, so use CPU reference cycles, easy to interpret)/event-based(generalization of time-based, powerful, deterministic and lower noise, tricky to interpret, need to be mapped back to the time domain)

Quantization errors: interval resolution is limited, introducing quantization errors/biases since time is continuous

interesting example: indirect tracing, trace events(such as control-flow, if/else/switch...) that dominate others,reducing overhead

tracing: extremely tedious, too much to consider(like reading a huge log file)

profiling: aggregate events over a specific metric, globally, or broken down by other events, information is lost!

reason: easy to interpret, it is lightweight and it can reduce perturbation

example: flame graphs,

more events, event sources: requirements: detailed/little perturbation/accurate

what do events come from: SW(lib,compiler,OS)/HW/Emulator(minimal perturbation but not scalable)

instrumentation: automatically/manually inserting logging code, no need HW support, flexible, however overhead/perturbation is high

manual/automatic source-level/automatic binary instrumentation(static/dynamic)

xray instrumentation/profiling framework, missed some function calls, ignore functions that run for less than 5 microseconds

HW support: performance counting, low-level events, some of them are buggy/unmaintained/poorly documented/of poor accuracy, it would be better to do some sanity checks

frontend bound(no ops entering the pipeline): too many function calls? backend bounds(no enough resources, cache miss/ALU stalls); issued and retired-retiring

