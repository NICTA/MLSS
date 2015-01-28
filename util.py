import csv
import numpy as np
import scipy.linalg
import matplotlib.pyplot as pl

def load_data():
    with open("titanic.csv") as f:
        g = (",".join([i[1],i[2],i[4],i[5],i[6],i[7],i[9],i[11]]).encode(encoding='UTF-8') 
                for i in csv.reader(f,delimiter=",",quotechar='"'))
        data = np.genfromtxt(g, delimiter=",",names=True,
                dtype=(int,int,np.dtype('a6'),float,int,int,float,np.dtype('a1')))
    embark_dict = {b'S':0, b'C':1, b'Q':2, b'':3}
    survived = data['Survived']
    passenger_class = data['Pclass']
    is_female = (data['Sex'] == b'female').astype(int)
    age = data['Age']
    sibsp = data['SibSp']
    parch = data['Parch']
    fare = data['Fare']
    embarked = np.array([embark_dict[k] for k in data['Embarked']])
    # skip age for the moment because of the missing data
    X = np.vstack((passenger_class, is_female, sibsp, parch, fare, embarked)).T
    Y = survived 
    return X, Y


def whitening_matrix(X):
    """The matrix of Eigenvectors that whitens the input vector X"""
    assert (X.ndim == 2)
    sigma = np.dot(X.T, X)
    e, m = scipy.linalg.eigh(sigma)
    return np.dot(m, np.diag(1.0/np.sqrt(e)))*np.sqrt((X.shape[0]-1))


def plot_svm(X, Y, svm_instance, xdim1=0, xdim2=1, minbound=(-3,-3),
        maxbound=(-3,-3), resolution=(100,100)):
    """ Plot any two dimensions from an SVM"""
    # build the meshgrid for the two dims we care about
    d = svm_instance.shape_fit_[1]
    n = resolution[0] * resolution[1]
    xx, yy = np.meshgrid(np.linspace(minbound[0], maxbound[0], resolution[0]),
            np.linspace(minbound[1], maxbound[1], resolution[1]))
    query2d = np.c_[xx.ravel(), yy.ravel()]
    query = np.zeros((n,d))
    query[:,xdim1] = query2d[:, 0]
    query[:,xdim2] = query2d[:, 1]

    Z = svm_instance.decision_function(query)
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
 

def illustrate_preprocessing():
    x = np.random.multivariate_normal(np.array([5.0,5.0]),
            np.array([[5.0,3.0],[3.0,4.0]]),size=1000)
    x_demean = x - np.mean(x, axis=0)
    x_unitsd = x_demean/(np.std(x_demean,axis=0))
    x_whiten = np.dot(x_demean, whitening_matrix(x_demean))

    fig = pl.figure(figsize=(10,10))
    
    def mk_subplot(n, data, label):
        ax = fig.add_subplot(2,2,n)
        ax.scatter(data[:,0], data[:,1])
        ax.set_xlim((-10,10))
        ax.set_ylim((-10,10))
        ax.set_xlabel(label)

    mk_subplot(1, x, "Original")
    mk_subplot(2, x_demean, "De-meaned")
    mk_subplot(3, x_unitsd, "Unit SD")
    mk_subplot(4, x_whiten, "Whitened")
    pl.show()

