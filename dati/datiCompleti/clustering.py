import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans


dataframe = pd.read_csv('dataset.csv')

dataset = dataframe.values

X = dataset[:,0:5]

kmeans = KMeans(n_clusters=2, init='k-means++', max_iter=100, n_init=10, random_state=0)
pred_y = kmeans.fit_predict(X)
plt.scatter(X[:,3], X[:,4])
plt.scatter(kmeans.cluster_centers_[:, 3], kmeans.cluster_centers_[:, 4], s=300, c='red')
plt.show()
