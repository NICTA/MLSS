from pylab import *
import matplotlib.cm as cm
import numpy as np
import scipy.linalg as la
from scipy.stats import chi2
from scipy.spatial import Voronoi, voronoi_plot_2d
from sklearn.datasets import make_blobs


def plot_2d_clusters(X, labels, centers):
    """
    Given an observation array, a label vector, and the location of the centers
    plot the clusters
    """

    clabels = set(labels)
    K = len(clabels)

    if len(centers) != K:
        raise ValueError("Expecting the number of unique labels and centres to"
                         " be the same!")

    # Plot the true clusters
    figure(figsize=(10, 10))
    ax = gca()

    vor = Voronoi(centers)

    voronoi_plot_2d(vor, ax)

    colors = cm.hsv(np.arange(K)/float(K))
    for k, col in enumerate(colors):
        my_members = labels == k
        scatter(X[my_members, 0], X[my_members, 1], c=col, marker='o', s=20)

    for k, col in enumerate(colors):
        cluster_center = centers[k]
        scatter(cluster_center[0], cluster_center[1], c=col, marker='o', s=200)

    axis('tight')
    axis('equal')
    title('Clusters')


def plot_2d_GMMs(X, labels, means, covs, percentcontour=0.66, npoints=30):
    """
    Given an observation array, a label vector (integer values), and GMM mean
    and covariance parameters, plot the clusters and parameters.
    """

    clabels = set(labels)
    K = len(clabels)

    if len(means) != len(covs) != K:
        raise ValueError("Expecting the number of unique labels, means and"
                         "covariances to be the same!")

    phi = np.linspace(-np.pi, np.pi, npoints)

    circle = np.array([np.sin(phi), np.cos(phi)]).T

    figure(figsize=(10, 10))
    gca()

    colors = cm.hsv(np.arange(K)/float(K))
    for k, col in zip(clabels, colors):

        # points
        my_members = labels == k
        scatter(X[my_members, 0], X[my_members, 1], c=col, marker='o', s=20)

        # means
        cluster_center = means[k, :]
        scatter(cluster_center[0], cluster_center[1], c=col, marker='o', s=200)

        # covariance
        L = la.cholesky(np.array(covs[k]) * chi2.ppf(percentcontour, [3])
                        + 1e-5 * np.eye(covs[k].shape[0]))
        covpoints = circle.dot(L) + means[k, :]
        plot(covpoints[:, 0], covpoints[:, 1], color=col, linewidth=3)

    axis('tight')
    axis('equal')
    title('Clusters')


def load_2d_simple():
    """
    Should be easily clustered with K-Means.
    """
    centres = [[1, 1], [-0.5, 0], [1, -1]]
    X, labels_true = make_blobs(n_samples=1000, centers=centres,
                                cluster_std=[[0.3, 0.3]])
    return X


def load_2d_hard():
    """
    Returns non-isotropoic data to motivate the use of non-euclidean norms (as
    well as the ground truth).
    """

    centres = np.array([[3., -1.], [-2., 1.], [2., 5.]])
    covs = []
    covs.append(np.array([[4., 2.], [2., 1.5]]))
    covs.append(np.array([[1, -1.5], [-1.5, 3.]]))
    covs.append(np.array([[1., 0.], [0., 1.]]))

    N = [1000, 500, 300]

    X = [np.random.randn(n, 2).dot(la.cholesky(c, lower=True)) + m
         for n, m, c in zip(N, centres, covs)]
    X = np.vstack(X)

    labels = np.concatenate((np.zeros(N[0]), np.ones(N[1]), 2*np.ones(N[2])))

    return X, labels
