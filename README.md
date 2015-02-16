# MLSS 2015 NICTA Labs
A collection of labs for the 2015 Machine Learning Summer School from NICTA
authored by:

* Finn Lattimore
* Lachlan McCalman
* Simon O'Callaghan
* Alistair Reid
* Daniel Steinberg
* Brian Thorne
* John Vial

The labs are all self contained in [ipython
notebooks](http://ipython.org/notebook.html) which are python environments that
are locally hosted within a browser. Both the instructions and the code input
cells are in the notebook, and so all you need to do to complete a lab is to
open the corresponding notebook in the directory where you have downloaded the
tutorials, and then work through the exercises in your browser.

This repository contains the first four labs for MLSS 2015 Syndey:

1. [Introduction to Python and PCA](https://github.com/NICTA/MLSS/tree/master/Intro%20and%20PCA)
2. [Linear Regression](https://github.com/NICTA/MLSS/tree/master/Linear%20Regression)
3. [Classification](https://github.com/NICTA/MLSS/tree/master/classification)
4. [Clustering and Latent Variable Models](https://github.com/NICTA/MLSS/tree/master/clustering)

You can find the general lab instructions [here](http://tinyurl.com/m62udcy),
as well as how to set up your python environment.


## Preview and Solutions

You can preview all of the lab solutions here:

1. [Introduction to Python and PCA](http://nbviewer.ipython.org/github/NICTA/MLSS/blob/master/Intro%20and%20PCA/Intro%20to%20python%20Answers.ipynb)
2. [Linear Regression](http://nbviewer.ipython.org/github/NICTA/MLSS/blob/master/Linear%20Regression/linearRegressionAnswers.ipynb)
3. [Classification](http://nbviewer.ipython.org/github/NICTA/MLSS/blob/master/classification/Classification_solutions.ipynb)
4. [Clustering and Latent Variable Models](http://nbviewer.ipython.org/github/NICTA/MLSS/blob/master/clustering/Clustering%20and%20Latent%20Variable%20Models%20-%20SOLUTIONS.ipynb)


## Dependencies

General:
* scikit-learn
* numpy
* matplotlib
* scipy
* ipython[all]

The above can all be checked using the `Dependency checker.ipynb` script in this repo. Optionally for the clustering lab:
* lda (may require you to also pull down pbr)
* Pillow
