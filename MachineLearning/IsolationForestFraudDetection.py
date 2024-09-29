import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
n_samples = 100
n_outliers = 20
n_features = 2

# Normal data (clustered)
X_normal = np.concatenate([np.random.normal(loc, 0.5, size=(n_samples // 3, n_features)) 
                             for loc in [0, 5, 10]], axis=0)

# Outlier data
X_outliers = np.random.uniform(low=-10, high=15, size=(n_outliers, n_features))

# Combine normal data and outliers
X = np.vstack([X_normal, X_outliers])

# Apply Isolation Forest
iso_forest = IsolationForest(contamination=0.2, random_state=42)
y_pred = iso_forest.fit_predict(X)

# Visualize the results
plt.figure(figsize=(10, 7))
plt.scatter(X[:, 0], X[:, 1], c=np.where(y_pred == -1, 'red', 'blue'), label='Anomalies vs Normal')
plt.title('Isolation Forest Anomaly Detection')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend(['Anomalies', 'Normal'])
plt.grid(True)
plt.show()