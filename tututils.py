from pylab import *
import matplotlib.cm as cm
import numpy as np
import scipy.linalg as la
from scipy.stats import chi2
from scipy.spatial import Voronoi, voronoi_plot_2d

from sklearn.cluster import KMeans
from sklearn.datasets import load_digits, make_moons, make_blobs
from sklearn.metrics import euclidean_distances

def kmeans_centers(X, k=3):
    """
    Helper function to calculate the cluster centers using sklearn's KMeans algorithm.

    Returns the cluster centers.
    """
    # Compute clustering with sklearn's K-Means
    k_means = KMeans(init='k-means++', n_clusters=k, n_init=10)
    k_means.fit(X)
    k_means_labels = k_means.labels_
    k_means_cluster_centers = k_means.cluster_centers_
    k_means_labels_unique = np.unique(k_means_labels)

    return k_means_cluster_centers


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
        L = la.cholesky(np.array(covs[k]) * chi2.ppf(percentcontour, [3]))
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

    centres = [[3, -1], [-2, 0], [0, 3]]
    covs = []
    covs.append([[3, 2], [2, 1]])
    covs.append([[1, -2], [-2, 3]])
    covs.append([[1, 0], [0, 1]])

    X0 = np.random.multivariate_normal(centres[0], covs[0], 1000)
    X1 = np.random.multivariate_normal(centres[1], covs[1], 500)
    X2 = np.random.multivariate_normal(centres[2], covs[2], 300)

    X = np.concatenate((X0, X1, X2))
    labels = np.concatenate((np.zeros(1000), np.ones(500), 2*np.ones(300)))

    return X, labels


def ex1():

    # Load X from a dataset generation function from tututils
    X = load_2d_simple()

    # Calculate M from X
    k_means_cluster_centers = kmeans_centers(X, 3)

    # Now calculate Z from X and M, probably using numpy's argmin()
    # CHANGE ME
    k_means_labels = np.ones(len(X))

    # Check your answer by plotting the clusters:
    plot_2d_clusters(X, k_means_labels, k_means_cluster_centers)
