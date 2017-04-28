# TDD Functional Programming Workshop

## Goal

See through a series of simple examples, how property-base testing can be implemented.

## Environment Setup

The workshop environment is provided as a Docker image. Please execute the following command in the root folder of this workshop.

```shell
docker build -t tdd-fp-ws .
```

And now let's run the app and start sbt.

```shell
docker run -it --rm  -v $(pwd):/app tdd-fp-ws
```

## Step by Step

### What is ScalaCheck?

"ScalaCheck is a tool for testing Scala and Java programs, based on property specifications and automatic test data generation. The basic idea is that you define a property that specifies the behaviour of a method or some unit of code, and ScalaCheck checks that the property holds."[1]

#### Test Case Minimisation

One interesting feature is that if it finds an argument that falsifies a property, it tries to minimize that argument before it is reported.

#### Properties

A property is a testable unit.

The first example is about testing Lists behavior. Before running the test, first, take a look at the code and get familiarized with it. There you are going to see examples of how to condition, combine, group and label properties.

```shell
test-only basicPropertiesTest
```

#### Generators

Generators are responsible for generating test data. A generator can be seen simply as a function that takes some generation parameters, and returns a generated value.

In this second example, we are going to see how to generate arbitrary values of a Rectangle case class, define the size of its height and width with a simple condition and classify the data it generates.

```shell
test-only basicGeneratorsTest
```

#### Stateful Testing

Sometimes you want to not only specify how a method should behave on its own, but also how a collection of methods should behave together when used as an interface to a larger system. You want to specify how the methods affect the system's state throughout time.

In this third example, you can test if a state is correct after running an arbitrary sequence of events.

```shell
test-only basicStatefulTest
```

#### Symmetry Testing

The fourth and last example is a small recap of all the previous concepts seen before, using the symmetry pattern.

```shell
test-only basicSymmetryTest
```

## References

* [1] https://github.com/rickynils/scalacheck/blob/master/doc/UserGuide.md ScalaCheck User Guide
* [2] https://yow.eventer.com/yow-lambda-jam-2015-1305/practical-property-based-testing-by-charles-o-farrell-1884 Charles O’Farrell at YOW! Lambda Jam 2015
* [3] https://github.com/oscarrenalias/scalacheck-examples Examples used as a basis for the workshop
* [4] https://github.com/charleso/property-testing-preso Examples used as a basis for the workshop

