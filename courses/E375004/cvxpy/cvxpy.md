# Optimalization - cvxpy

## Before we start

I recommend to make empty virtual enviroment (I usualy name it ".venv")

```
python -m venv .venv
```

Activate:

```
/.venv/Scripts/activate
```

Install libraries:

```
pip install matplotlib
pip install numpy
pip install cvxpy
```

## Introduction

Optimization is a process of seeking the maximum or minimum of the *objective function*. In reality, those types of problems are all over the place. For example, if you have a company producing paper boxes, you will want as many boxes as possible made from as little paper as possible.

Typically, optimization has been used for a long time in any scheduling tasks(for example, when a coal-fired power plant block should or should not run, when and on what machine to produce some metal parts, to be as fast as possible). There are a lot of tasks, and as future engineers you will sooner or later need optimization in some form.

## Example 1 - Welded metal sheet boxes

The first task will be very simple. In fact, you would need nothing more than a pen and paper. We will program the solution as a very simple notebook though (also, a script is fine if you're working in command line). So far no special library will be needed (except numpy and matplotlib).

- [Example 1 - boxes](boxes.ipynb)


# Linear programming

Linear programming is a very simple tool for optimizing problems that can be formulated in LP language. I recommend the English Wikipedia and of course the official documentation:
- [wiki](https://en.wikipedia.org/wiki/Linear_programming)
- [cvxpy - docs](https://www.cvxpy.org/)

If you are interested in lecture, there is also very informative youtube video from MIT courseware, which I highly recommend.

[![15. Linear Programming: LP, reductions, Simplex](http://img.youtube.com/vi/WwMz2fJwUCg/0.jpg)](https://www.youtube.com/watch?v=WwMz2fJwUCg&t "15. Linear Programming: LP, reductions, Simplex")

## Example 2 - cvxpy (linear programming)

Our first example will be a notorious task in optimizing the composition of dog kibbles. The cvxpy library **can not** be used in our jupyter server. You have to install the library in your local virtual environment. If you want to use jupyter lab at home, just install it also in a virtual environment and run from your command line on local host.

-[Example 2 - dog kibbles](granule.ipynb)

## Example 3 - Gas plant block optimization

In the following example, our task will be to optimize the day-ahead (24 hours) of the performance of the gas power plant block so that we earn as much money as possible.

-[Example 3 - gas plant block](blok.ipynb)

## Example 4 - Maximizing flow through the network

In this example, our task is to maximize flow through the network. Network is represented as directed graph with one starting node (source) and one ending node (sink).

-[Example 4 - Maximizing flow through the network](flow.ipynb)
