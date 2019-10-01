# K-Means Clustering

# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from yellowbrick.cluster import KElbowVisualizer

# Importing the dataset
dataframe = pd.read_csv('dataset.csv')

dataset = dataframe.values

X = dataset[:,0:6]
y = dataset[:,6]

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)
y_kmeans = kmeans.fit(X)
centers = kmeans.cluster_centers_
print(centers)
new_labels=kmeans.labels_
print(new_labels)

fig, axes = plt.subplots(1, 2, figsize=(16,8))
axes[0].scatter(X[:,0],X[:,1], c='green',edgecolor='k', s=50)
axes[0].scatter(X[:,3],X[:,4], c='blue',edgecolor='k', s=50)
axes[1].scatter(X[:,0],X[:,1], c='green',edgecolor='k', s=50)
axes[1].scatter(X[:,3],X[:,4], c='blue',edgecolor='k', s=50)
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],s = 300, c = 'yellow', label = 'Centroids velocity')
plt.scatter(kmeans.cluster_centers_[:,3], kmeans.cluster_centers_[:,4],s = 300, c = 'red', label = 'Centroids distance')

'''
axes[0].set_xlabel('Destra',fontsize=18)
axes[0].set_ylabel('Sinistra',fontsize=18)
axes[1].set_xlabel('Destra',fontsize=18)
axes[1].set_ylabel('Sinistra',fontsize=18)
'''
axes[0].set_title('Effettivo',fontsize=18)
axes[1].set_title('Previsto',fontsize=18)

print(silhouette_score(X,kmeans.labels_, metric="euclidean"))

visualizer = KElbowVisualizer(kmeans, k=(2,6), metric='silhouette', timings=False)
plt.legend()
plt.show()

visualizer.fit(X)
visualizer.poof()