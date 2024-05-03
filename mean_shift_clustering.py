import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import MeanShift, estimate_bandwidth

# Generate a synthetic dataset
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Estimate the bandwidth (the radius of the area to search for data points)
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)

# Initialize Mean Shift with the estimated bandwidth
mean_shift = MeanShift(bandwidth=bandwidth, bin_seeding=True)

# Fit Mean Shift to the data
clusters = mean_shift.fit_predict(X)

# Plot the clusters
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis', marker='o', edgecolor='k')
plt.title('Mean Shift Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar(label='Cluster Label')
plt.show()
