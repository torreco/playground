# Functional programming workshop

### Goal

Explore how the functional programming feels by comparing it with object oriented programming.

## Environment setup

The working environment is provided as a Docker image that can be built by executing the following command at the root folder of this workshop.
```shell
docker build -t ooo-fun-ws docker
```

The following alias will help us run the examples:
```shell
alias ooo-fun-ws="docker run --rm  -v $(pwd):/app ooo-fun-ws"
```

> Side note: Python was choose as programming language because it's capable of dealing with different programming models, namely: OOO and functional.

### Optional
This workshop has some examples written in Scala. They are packed as an SBT project, as such you need to install the SBT build tool. 

One way to do it is by installing [SDKMAN](http://sdkman.io/) and then running:
```shell
sdk install sbt
```

To run the examples move the folder `extras/type_safe` and execute:
```shell
sbt run
```

## Primes

The first example we're going to run is simple: Get the list of prime numbers from 0 to 10000.

* Checkout the files `primes/not_fun.py` and `primes/fun.py`, understand them and see why we say that functional programming it's declarative (_what to do but not how to do it_) instead of imperative (_what to do and how to do it_). 
* Run:

 ```shell
 ooo-fun-ws mprof run primes/not_fun.py
 ooo-fun-ws python -m profile primes/not_fun.py
 ooo-fun-ws mprof run primes/fun.py
 ooo-fun-ws python -m profile primes/fun.py

 ```
*  The above commands will profile the programs in **memory** and **CPU** usage. The memory report is located at the root of this workshop folder and named `mprofile_<timestamp>.dat`. The CPU data is in the standard output after each command has finished.
* Compare the results.
* **TODO:** Can you think of a way to improve the performance of the functional version?

## Evaluator

The second example is a bit more complex. It defines a common design pattern in Object Oriented Programming: [the decorator pattern](https://en.wikipedia.org/wiki/Decorator_pattern).

The model is used to evaluate applicants to a job under different constraints. Different positions apply different constraints. So there's a need to composed them in multiple ways.

* Checkout the file `evaluator/not_fun.py`. Understand the model.
* Run:

 ```shell
 ooo-fun-ws mprof run evaluator/not_fun.py
 ooo-fun-ws python -m profile evaluator/not_fun.py
 ```
* Checkout the file `evaluator_fun.py`. Review how the code has changed.
* **TODO:** Implement the `p_compose` function to combine predicates.
* After completing the above, run:

 ```shell
 ooo-fun-ws mprof run evaluator/fun.py
 ooo-fun-ws python -m profile evaluator/fun.py
 ```
* Compare the results.

## Editor

The third, and final, example shows [the command pattern](https://en.wikipedia.org/wiki/Command_pattern).

The model is pretty simple: an editor (which doesn't do anything) and a set of commands that can act upon it.

* Checkout the file `editor/not_fun.py`. Understand the model.
* Run:
 
 ```shell
 ooo-fun-ws python editor/not_fun.py
 ```
* Now, checkout the file `editor/fun.py`. Most of the code went away.
 > Side note: As noted by Richard Warburton in _Object-Oriented vs. Functional Programming._: "The command pattern is really just a poor man’s lambda expression to begin with."
 
* Run:
 ```shell
 ooo-fun-ws python editor/fun.py
 ```
* **TODO**: The command pattern is useful for implementing undo actions. Add the undo behavior to the programs.


## A subjective note on static vs dynamic typing 

You may have noticed that most of the functional programming languages such as Haskell and Elm, or hybrid languages such as Scala, Clojure and F# tend to be statically typed. It's no coincidence. They tend to choose this option as programs are easier to reason and with the help of the compiler, the number of errors that get into production is smaller. Not by much [3] and still refutable [4].

The usual argument used by people preferring dynamic typing is that writing types is too verbose and that by using dynamic typing the developer productivity is increased. 

The problem is that the developer still has to deal with types manually. It's the kind of the same idea when people say NoSQL databases are schema-less, the schema is still there but the developer is the one who needs to write code to check the model is what she expects it to be.

The improvement of type systems has helped static languages to become less verbose, so the afore mentioned argument is loosing some ground. One such example is the fact that languages like as Python, PHP (with Hack) and TypeScript are moving to a type safe(r) environment. The benefits of static typing are outweighing the benefits of dynamic typing.

As an example of the above checkout the file `evaluator_fun.scala` and detail how it differs from the Python version. It's roughly the same in terms of lines of code and the statements required for typing are not there without a purpose or redundant.

In the end, as usual, it's a matter of preference but several languages seem to be converging to static typing.

_PS: The above is @davidmr's personal opinion :)_.

## Real world examples

**TODO**: Have you ever used any kind of functional programming in your day to day work?. Do you have any examples?.

## References

* [1] https://youtu.be/wjF1WqGhoQI used as basis of the Primes and Evaluator examples
* [2] https://vimeo.com/111041651 used as basis of the Editor example
* [3] http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.658.7207&rep=rep1&type=pdf
* [4] http://danluu.com/empirical-pl/