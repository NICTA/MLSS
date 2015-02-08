# Getting Started

## Download Python 3.4

Install the Anaconda Python distribution from [continuum.io](http://continuum.io/downloads#py34).
Be sure to click **I WANT PYTHON 3.4**. Direct download links are:

- [Anaconda Python 3.4 - Windows 64](http://repo.continuum.io/anaconda3/Anaconda3-2.1.0-Windows-x86_64.exe)
- [Anaconda Python 3.4 - OSX](http://repo.continuum.io/anaconda3/Anaconda3-2.1.0-MacOSX-x86_64.pkg)


## Start IPython Notebook


    ipython notebook


If you run into trouble, ask one of the friendly tutors. Or start reading the notebook in 
readonly mode at [nbviewer.ipython.org](http://nbviewer.ipython.org/github/hardbyte/python-ml-tut/blob/master/Intro%20to%20python.ipynb)

## Begin the tutorial

Open the `Intro to python.ipynb` Notebook and start working through the exercises.


## Already have Python 3.4?
 
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

```python
# numbers and variables
age = 26
pi = 3.14159

# strings and methods
s = 'Hugh F Durrant-Whyte'
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

# list (mutable ordered sequence)
beatles = ['John', 'Paul', 'George']
beatles.append('Ringo')
print(beatles)

# 'for' loop - indentation matters
for b in beatles:
    print('Hello ' + b)

# tuple (immutable ordered sequence)
ages = (18, 21, 28, 21, 22, 18, 19, 34, 9)

# set (mutable, unordered, no duplicates)
uniqueAges = set(ages)
uniqueAges.add(18) # already in set, no effect
uniqueAges.remove(21)

# no guaranteed order when iterating over a set
for thisAge in uniqueAges:
    print(thisAge)

# testing set membership
if 18 in uniqueAges:
    print('There is an 18-year-old present!')

# sorting
beatles.sort() # in-place
orderedUniqueAges = sorted(uniqueAges) # new list

# dict - mapping unique keys to values
netWorth = {}
netWorth['Donald Trump'] = 3000000000
netWorth['Bill Gates'] = 58000000000
netWorth['Tom Cruise'] = 40000000
netWorth['Joe Postdoc'] = 20000

# iterating over a dict gives keys
for personName in netWorth:
    print("{} is worth {}".format(personName, netWorth[personName]))

# You can also iterate over key-value pairs:
for (person, worth) in netWorth.items():
    if worth < 1000000:
        print('haha ' + person + ' is not a millionaire')

# testing dict membership is the same as with a set
if 'Tom Cruise' in netWorth:
    print('show me the money!')
```