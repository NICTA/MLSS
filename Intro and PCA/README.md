# Getting Started

## Download Python (2.7 or 3.4)

Install the Anaconda Python distribution from [continuum.io](http://continuum.io/downloads).
If you want Python 3.4 be sure to click **I WANT PYTHON 3.4**. 

## Start IPython Notebook

Find the Anaconda **Launcher** and launch:

    ipython notebook

Your browser should open up to http://localhost:8888 and show your home directory.
Find your way to the directory where you downloaded and unzipped the MLSS tutorials.

If you run into trouble, ask one of the friendly tutors. Or start reading the notebook in 
readonly mode at [nbviewer.ipython.org](http://nbviewer.ipython.org/github/NICTA/MLSS/blob/master/Intro%20and%20PCA/Intro%20to%20python.ipynb)

## Begin the tutorial

Open the `Intro to python.ipynb` Notebook and start working through the exercises.


## Already have Python?
 
Just make sure you have all the requirements installed for this tutorial by running:

    pip install -r requirements.txt

# Python Quickstart

# New to Python?

## Resources

- [Learn Python The Hardway](http://learnpythonthehardway.org/book/)
- [Online Python Interactive Debugger](http://people.csail.mit.edu/pgbovine/python/)
- [Dive into Python 3](http://getpython3.com/diveintopython3/)
- [Interactive Python](http://interactivepython.org/courselib/static/thinkcspy/index.html)

## Intro to Python Cheatsheet

Launch the IPython QT console and try run (and understand) these commands:

```python
# This is a comment line
# numbers and variables
age = 26
pi = 3.14159

# strings and methods
s = 'Hugh F Durrant-Whyte'

# Strings have a method `split` which returns a list of strings split by whitespace
tokens = s.split()
firstName = tokens[0]
middleName = tokens[1]
lastName = tokens[2]
s2 = firstName + ' ' + middleName + ' ' + lastName

# 'if' statement - indentation matters
if s == s2:
    print('yes the strings are equal')
else:
    print('no')

# if statements can also be inline
answer = 'yes' if s == s2 else 'no' 

# list (mutable ordered sequence)
beatles = ['John', 'Paul', 'George']
beatles.append('Ringo')
print(beatles)
print('Ringo' in beatles)


# 'for' loop - indentation matters
# Note that name is defined inside the for loop
for name in beatles:
    print('Hello ' + name)

# Iterating over a range of numbers is easy
# range has the following arguments (start, stop, step) where stop isn't included
for number in range(2, 10, 2):
    print(number)

# tuple (immutable ordered sequence)
ages = (18, 21, 28, 21, 22, 18, 19, 34, 9)

# Note you can't change the contents of a tuple

# set (mutable, unordered, no duplicates)
uniqueAges = set(ages)
uniqueAges.add(18) # already in set, no effect
uniqueAges.remove(21)


# testing set membership (very fast)
if 18 in uniqueAges:
    print('There is an 18-year-old present!')

# sorting a list
sorted(beatles) # returns a new sorted list
beatles.sort() # in-place - changes beatles list

# Sorting a set returns a list
orderedUniqueAges = sorted(uniqueAges)

# There is no guaranteed order when iterating over a set
for thisAge in uniqueAges:
    print(thisAge)

# Instead iterate over the sorted set:
for age in sorted(uniqueAges):
    print(age)

# dict - mapping unique keys to values
netWorth = {}
netWorth['Donald Trump'] = 3000000000
netWorth['Bill Gates'] = 58000000000
netWorth['Tom Cruise'] = 40000000
netWorth['Joe Postdoc'] = 20000

# Access the value associated with a key
print(netWorth['Donald Trump'])

# iterating over a dict gives keys
for personName in netWorth:
    print(personName + " is worth: ", end='')
    print(netWorth[personName])

# You can also iterate over key-value pairs:
for (person, worth) in netWorth.items():
    if worth < 1000000:
        print('haha ' + person + ' is not a millionaire')

# testing dict membership is the same as with a set
if 'Tom Cruise' in netWorth:
    print('show me the money!')
```
