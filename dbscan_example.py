import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN

# Generate a synthetic dataset
X, _ = make_moons(n_samples=300, noise=0.1, random_state=42)

# Initialize DBSCAN with specified parameters
dbscan = DBSCAN(eps=0.2, min_samples=5)

# Fit DBSCAN to the data
clusters = dbscan.fit_predict(X)

# Plot the clusters
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis', marker='o', edgecolor='k')
plt.title('DBSCAN Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar(label='Cluster Label')
plt.show()
