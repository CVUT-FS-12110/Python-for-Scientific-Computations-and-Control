# Artificial Intelligence and Python - Part Two

## Introduction

In the first chapter, we showed 3 different simple examples. Today's lesson will only focus on various *neural networks*. However, keep in mind, that artificial intelligence is not the same thing as neural networks. Neural networks are only a subfield of AI.


Because of python, the development and implementation of neural networks is very simple and user friendly. It is possible to implement structures that are relatively complex on a few lines of code, thanks to several useful frameworks uch as:
- [Keras](https://keras.io/)
- [Tensorflow](https://www.tensorflow.org/)
- [PyTorch](https://pytorch.org/)


We will use *Tensorflow* and partly also keras (whose API is used by Tensorflow). You will see that creating and testing new model is really easy.

## SOM - Self-organizing Maps

First neural netwrok we will program will be so-called *SOM* ([wikipedia](https://en.wikipedia.org/wiki/Self-organizing_map)).

- [example 1 - SOM](SOM.ipynb)

## MLP - Multilayer perceptron

The second example of a neural network will be the so-called *MLP* ([wikipedia](https://en.wikipedia.org/wiki/Multilayer_perceptron)). We wrote a script for perceptron last hour. This network is made up of many of these neural units arranged in individual layers.

In order to partially simplify the work and also to be able to nicely visualize the results, our task will be to classify handwritten numbers ([MNIST dataset](https://en.wikipedia.org/wiki/MNIST_database)). This dataset is used as a metric for many proposed models, is well researched and can be found in every second tutorial on youtube.

- [example 2 - MLP](mnist_MLP.ipynb)

## CNN - Convolutional Neural Network

The last example will be the so-called *CNN* ([wiki-link](https://en.wikipedia.org/wiki/Convolutional_neural_network)). This type of network is often used to classify images (not only, but mainly).

We will use the MNIST dataset again, compare the number of network parameters and how fast those models learn. Which of these two networks (MLP, CNN) achieves greater accuracy on the validation set?

- [example 3 - CNN](mnist_CNN.ipynb)