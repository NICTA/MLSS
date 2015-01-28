from pylab import *
import numpy as np
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
    # Plot the true clusters
    fig = figure(figsize=(10, 10))
    ax = gca()

    vor = Voronoi(centers)

    voronoi_plot_2d(vor, ax)
    axis('equal')

    colors = ['r', 'b', 'g', 'y', 'o']
    for k, col in zip(range(len(centers)), colors):
        my_members = labels == k
        scatter(X[my_members, 0], X[my_members, 1], c=col, marker='o', s=20)

    for k, col in zip(range(len(centers)), colors):
        cluster_center = centers[k]
        scatter(cluster_center[0], cluster_center[1], c=col, marker='o', s=200)

    title('Clusters')


def load_2d_simple():
    """
    Should be easily clustered with K-Means.
    """
    centres = [[1, 1], [-0.5, 0], [1, -1]]
    X, labels_true = make_blobs(n_samples=1000, centers=centres, cluster_std=[[0.3, 0.3]])
    return X


def load_2d_hard():
    """
    Returns non-isotropoic data to motivate the use of non-euclidean norms
    """

    centres = [[1, 0.75], [1, -0.75], [0, 0]]

    X0, labels0_true = make_blobs(n_samples=300, centers=centres[0], cluster_std=[[0.6, 0.1]])
    X1, labels1_true = make_blobs(n_samples=300, centers=centres[1], cluster_std=[[0.6, 0.1]])
    X2, labels2_true = make_blobs(n_samples=300, centers=centres[2], cluster_std=[[0.6, 0.1]])

    X = np.concatenate((X0, X1, X2))
    labels_true = np.concatenate((labels0_true, labels1_true+1, labels2_true+2))

    return X


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