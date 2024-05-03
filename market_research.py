import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate synthetic data: 1000 customers with features: annual spending, number of transactions
data, _ = make_blobs(n_samples=1000, centers=4, cluster_std=1.5, random_state=42, n_features=2)
data = pd.DataFrame(data, columns=['Annual Spending (1000$)', 'Number of Transactions'])

# Configure and fit the K-means model
kmeans = KMeans(n_clusters=4, random_state=42)
data['Cluster'] = kmeans.fit_predict(data[['Annual Spending (1000$)', 'Number of Transactions']])

# Plotting the clusters
plt.figure(figsize=(10, 6))
plt.scatter(data['Annual Spending (1000$)'], data['Number of Transactions'], c=data['Cluster'], cmap='viridis', marker='o', edgecolor='black')
plt.title('Customer Segmentation based on Purchasing Behavior')
plt.xlabel('Annual Spending (1000$)')
plt.ylabel('Number of Transactions')
plt.colorbar(label='Cluster')
plt.grid(True)
plt.show()
