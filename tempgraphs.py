import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

from sklearn.datasets.samples_generator import make_blobs
X, y_true = make_blobs(n_samples=300, centers=15,
                       cluster_std=0.60, random_state=0)
# plt.scatter((X[:, 0]+10)/20, (X[:, 1]+10)/20, s=10)
# plt.show()

kmeans = KMeans(n_clusters=7)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

plt.scatter((X[:, 0]+10)/20, (X[:, 1]+10)/20, c=y_kmeans, s=5, cmap='viridis')

centers = kmeans.cluster_centers_
plt.scatter((centers[:, 0]+10)/20, (centers[:, 1]+10)/20, c='black', s=10, alpha=0.5);
plt.show()
