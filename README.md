# Getting Started

## Download Python 3.4

Install the Anaconda Python distribution from [continuum.io](http://continuum.io/downloads#py34).
Be sure to click **I WANT PYTHON 3.4**. Direct download links are:

- [Anaconda Python 3.4 - Windows 64](http://repo.continuum.io/anaconda3/Anaconda3-2.1.0-Windows-x86_64.exe)
- [Anaconda Python 3.4 - OSX](http://repo.continuum.io/anaconda3/Anaconda3-2.1.0-MacOSX-x86_64.pkg)


## Start IPython Notebook


    ipython notebook


## Begin the tutorial

Open the `Intro to python.ipynb` Notebook and start working through the exercises.


## Already have Python 3.4?
 
Just make sure you have all the requirements installed for this tutorial by running:

    pip install -r requirements.txt

# Python Quickstart

<iframe width="1600" height="900" frameborder="0" 
      src="http://pythontutor.com/iframe-embed.html#code=%23+Python+Tutor's+10-minute+intro+to+Python%0A%0A%23+numbers!%0Aage+%3D+26%0Api+%3D+3.14159%0A%0A%23+strings!%0As+%3D+'Rutherford+Birchard+Hayes'%0Atokens+%3D+s.split()%0AfirstName+%3D+tokens%5B0%5D%0AmiddleName+%3D+tokens%5B1%5D%0AlastName+%3D+tokens%5B2%5D%0As2+%3D+firstName+%2B+'+'+%2B+middleName+%2B+'+'+%2B+lastName%0A%0A%23+'if'+statement+-+indentation+matters!%0Aif+(s+%3D%3D+s2)%3A%0A++++print('yes!!!')%0Aelse%3A%0A++++print('nooooooo')%0A%0A%23+list+(mutable+sequence)%0Abeatles+%3D+%5B'John',+'Paul',+'George'%5D%0Abeatles.append('Ringo')%0A%0A%23+'for'+loop+-+indentation+matters!%0Afor+b+in+beatles%3A%0A++++print('Hello+'+%2B+b)%0A%0A%23+tuple+(immutable+sequence)%0Aages+%3D+(18,+21,+28,+21,+22,+18,+19,+34,+9)%0A%0A%23+set+(no+order,+no+duplicates)%0AuniqueAges+%3D+set(ages)%0AuniqueAges.add(18)+%23+already+in+set,+no+effect%0AuniqueAges.remove(21)%0A%0A%23+no+guaranteed+order+when+iterating+over+a+set%0Afor+thisAge+in+uniqueAges%3A%0A++++print(thisAge)%0A%0A%23+testing+set+membership%0Aif+18+in+uniqueAges%3A%0A++++print('There+is+an+18-year-old+present!')%0A%0A%23+sorting%0Abeatles.sort()+%23+in-place%0AorderedUniqueAges+%3D+sorted(uniqueAges)+%23+new+list%0A%0A%23+dict+-+mapping+unique+keys+to+values%0AnetWorth+%3D+%7B%7D%0AnetWorth%5B'Donald+Trump'%5D+%3D+3000000000%0AnetWorth%5B'Bill+Gates'%5D+%3D+58000000000%0AnetWorth%5B'Tom+Cruise'%5D+%3D+40000000%0AnetWorth%5B'Joe+Postdoc'%5D+%3D+20000%0A%0A%23+iterating+over+key-value+pairs%3A%0Afor+(person,+worth)+in+netWorth.items()%3A%0A++++if+worth+%3C+1000000%3A%0A++++++++print('haha+'+%2B+person+%2B+'+is+not+a+millionaire')%0A%0A%23+testing+dict+membership%0Aif+'Tom+Cruise'+in+netWorth%3A%0A++++print('show+me+the+money!')&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&curInstr=0&codeDivWidth=550&codeDivHeight=400"> </iframe>
      