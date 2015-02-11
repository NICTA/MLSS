import numpy as np
from sklearn import svm
from sklearn.cross_validation import KFold

import util

X, Y = util.load_data()

Xd = X - np.mean(X,axis=0)
Xs = (Xd/np.std(Xd,axis=0))
Xw = np.dot(Xd, util.whitening_matrix(Xd))

# >>> kf = KFold(4, n_folds=2, shuffle=True)
# >>> for train, test in kf:

# fit the model
clf = svm.NuSVC()
clf.fit(Xw, Y)

query = util.plot_svm(Xw, Y, clf, 0, 1, (-3,-3), (3,3), (500,500))


