import numpy as np
import scipy.linalg
import matplotlib.pyplot as pl
from sklearn import svm
# loads selected columns from the Titanic csv file into a numpy array.
# columns are [Survived,pClass,Sex,Age,SibSp,Parch,Fare,Embarked]

import csv
with open("titanic.csv") as f:
    g = (",".join([i[1],i[2],i[4],i[5],i[6],i[7],i[9],i[11]]) for i in csv.reader(f,delimiter=",",quotechar='"'))
    data = np.genfromtxt(g, delimiter=",",names=True,dtype=(int,int,np.dtype('a6'),float,int,int,float,np.dtype('a1')))

embark_dict = {'S':0, 'C':1, 'Q':2, '':3}

survived = data['Survived']
passenger_class = data['Pclass']
is_female = (data['Sex'] == 'female').astype(int)
age = data['Age']
sibsp = data['SibSp']
parch = data['Parch']
fare = data['Fare']
embarked = np.array([embark_dict[k] for k in data['Embarked']])

# skip age for the moment because of the missing data
X = np.vstack((passenger_class, is_female, sibsp, parch, fare, embarked)).T
Y = survived 

def whitening_matrix(X):
    """The matrix of Eigenvectors that whitens the input vector X"""
    assert (X.ndim == 2)
    sigma = np.dot(X.T, X)
    e, m = scipy.linalg.eigh(sigma)
    return np.dot(m, np.diag(1.0/np.sqrt(e)))*np.sqrt((X.shape[0]-1))

Xd = X - np.mean(X,axis=0)
Xs = (Xd/np.std(Xd,axis=0))
Xw = np.dot(Xd, whitening_matrix(Xd))



def plot_svm(X, Y, svm_instance, xdim1, xdim2, minbound, maxbound, resolution):
    # build the meshgrid for the two dims we care about
    d = svm_instance.shape_fit_[1]
    n = resolution[0] * resolution[1]
    xx, yy = np.meshgrid(np.linspace(minbound[0], maxbound[0], resolution[0]),
        np.linspace(minbound[1], maxbound[1], resolution[1]))
    query2d = np.c_[xx.ravel(), yy.ravel()]
    query = np.zeros((n,d))
    query[:,xdim1] = query2d[:, 0]
    query[:,xdim2] = query2d[:, 1]
    
    Z = clf.decision_function(query)
    Z = Z.reshape(xx.shape)

    pl.imshow(Z, interpolation='nearest',
               extent=(xx.min(), xx.max(), yy.min(), yy.max()), aspect='auto',
               origin='lower', cmap=pl.cm.PuOr_r)
    contours = pl.contour(xx, yy, Z, levels=[0], linewidths=2,
                           linetypes='--')
    pl.scatter(X[:, xdim1], X[:, xdim2], s=30, c=Y, cmap=pl.cm.Paired)
    pl.xticks(())
    pl.yticks(())
    pl.axis([minbound[0], maxbound[0], minbound[1], maxbound[1]])
    pl.show()



# fit the model
clf = svm.NuSVC()
clf.fit(Xw, Y)

query = plot_svm(Xw, Y, clf, 0, 1, (-3,-3), (3,3), (500,500))


