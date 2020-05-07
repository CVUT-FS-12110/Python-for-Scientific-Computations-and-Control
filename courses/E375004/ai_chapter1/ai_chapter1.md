# Artificial Intelligence and Python - Part One

## Introduction

The phrase *artificial intelligence* is definitely one of the so-called *buzzwords*. Everyone has heard of *Industry 4.0*, but few can imagine what that means. Similarly, there is artificial intelligence, the foundations of which are much older than just the last 15 years of neural networks, which you have heard of on televsion.

That is why this lesson is not intended to replace the lecture of the history and theory of artificial intelligence, but rather to show you what is possible in python (often by useful libraries). If we were to program an example for each subarea of artificial intelligence, a whole semester would probably not be enough for us. For students who are passionate about AI, I highly recommend the sequence of lectures from MIT: [MIT open coursware - AI](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010/), although these lectures are from 2010, I think it's still one of the best you can find on the internet.

I decided to look at 3 examples of the three AI sub-areas. They will be relatively simple, but in my opinion illustrative.

## Genetic algorithms

Genetic algorithms (or sometimes evolutionary algorithms) are simply algorithms that try to mimic evolution. Do you still remember mitosis and meiosis? And what about mutations and crossing-over? Whatever comes to mind in this context and is inspired by nature can be considered a genetic algorithm.

- [example 1 - genetic algorithm](genetic.ipynb)

## Fuzzy system


Another example will be a fuzzy system based on the interesting mathematics of fuzzy sets (fuzzy means blury or not black/white). In the following example, you can see that the dynamics of the famous [Mackey-Glass equation](http://www.scholarpedia.org/article/Mackey-Glass_equation) can be approximated using a fuzzy system.

- [example 2 - fuzzy system Mackey-Glass](fuzzymackeyglass.ipynb)


If you would like to learn more about fuzzy systems and fuzzy control, I recommend the book *A Course in Fuzzy Systems and Control*. However, I am not sure if it is available in a PDF version for free download, if it is not and someone would really be interested, write me an email.

## Perceptron

The last example is *perceptron*, which I don't have to introduce:

- [example 3 - perceptron](perceptron.ipynb)