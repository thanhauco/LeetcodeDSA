import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Sample data: [feature1, feature2]
data = np.array([
    [1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80],
    [24, 80], [25, 81], [26, 81]
])

# Initialize DBSCAN
# epsilon is the radius within which points are considered neighbors
# min_samples is the number of points required to form a dense region
dbscan = DBSCAN(eps=3, min_samples=2)

# Fit DBSCAN to the data
dbscan.fit(data)

# Get cluster labels
labels = dbscan.labels_

# Identify unique labels (clusters and noise)
unique_labels = set(labels)

# Plot results
plt.figure(figsize=(8, 6))

# Define colors for clusters and noise
colors = plt.cm.get_cmap('Spectral', len(unique_labels))

for label in unique_labels:
    class_member_mask = (labels == label)
    xy = data[class_member_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=colors(label), markeredgecolor='k', markersize=6)

plt.title('DBSCAN Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

# Print the cluster labels
print('Cluster Labels:', labels)