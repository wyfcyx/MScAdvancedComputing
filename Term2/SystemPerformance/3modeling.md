aspects: machine/code/data, at least one of them is missed, thus substitute it with a model->system model and profile it

simplifications: input is from a uniform distribution without correlation, do not model system noise(scheduling overhead), assume single-threaded code

approaches: numerical/experimental model(a serial of data points, easy to be understood by human, limited prediction?), or analytical models(difficult to interpret, prediction depends on the flexibility of the model)

---

numerical models: gathering data through micro-benchmarking->interpret through interpolation

pros: easy to get, based on ground truth, easy to interpret,

cons: poor generalization, require a lot data points in a multi-dimensional parameter space, limited prediction accuracy, limited interpretability/insight(kind of black-box)

---

analytical models: scary formulas, more an art than a craft, requires detailed understanding/extension validation, very complicated since it considers all edge cases 

model fitting: empirical models->analytical ones, maybe through regression, similar to numerical models but more expressive(regression versus interpolation)

stateless systems

---

stateful systems: some effects have dynamic state which affects the model, we use stochastical models to model them

Discrete-Time Markov chains, finite state machine, useful for modeling low-level behaviors

example: modeling branch predictors



