import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Parameters
n_samples = 50
n_features = 2
centers = 3
cluster_std = [1.0, 1.0, 1.0]
noise_samples = 10  # Number of noise points
outlier_samples = 5  # Number of outlier points

# Generate synthetic data with clusters
data, _ = make_blobs(n_samples=n_samples, n_features=n_features, centers=centers, cluster_std=cluster_std, random_state=42)

# Add noise
np.random.seed(42)
noise = np.random.uniform(low=-10, high=10, size=(noise_samples, n_features))
data_with_noise = np.vstack([data, noise])

# Add outliers
outliers = np.random.uniform(low=-15, high=15, size=(outlier_samples, n_features))
data_with_outliers = np.vstack([data_with_noise, outliers])

# Apply DBSCAN
dbscan = DBSCAN(eps=1.5, min_samples=5)
labels = dbscan.fit_predict(data_with_outliers)

# Visualize the results
plt.figure(figsize=(12, 8))
unique_labels = np.unique(labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))

for k, col in zip(unique_labels, colors):
    class_member_mask = (labels == k)
    xy = data_with_outliers[class_member_mask]
    plt.scatter(xy[:, 0], xy[:, 1], s=50, c=[col], label=f'Cluster {k}')

# Highlight noise points (label = -1)
noise_mask = (labels == -1)
plt.scatter(data_with_outliers[noise_mask, 0], data_with_outliers[noise_mask, 1], s=50, c='black', marker='x', label='Noise')

plt.title('DBSCAN Clustering with Noise and Outliers')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid(True)
plt.show()