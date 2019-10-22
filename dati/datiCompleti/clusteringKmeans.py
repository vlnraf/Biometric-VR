# K-Means Clustering

# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from yellowbrick.cluster import KElbowVisualizer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import warnings
from sklearn.decomposition import PCA

warnings.simplefilter(action='ignore', category=FutureWarning)

# Importing the dataset
df = pd.read_csv('dataset1.csv')

dataset = df.values

X = dataset[:,0:4]
y = dataset[:,4]

x = StandardScaler().fit_transform(X)

pca = PCA(n_components=2)

principalComponents = pca.fit_transform(X)

principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1','principal component 2'])
finalDf = pd.concat([principalDf, df[['Sesso']]], axis = 1)

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1)
targets = ['Distanza','DistanzaDx']
colors = ['r','g','b']
for target, color in zip(targets, colors):
    indicesToKeep = finalDf['Sesso'] == target

ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'], finalDf.loc[indicesToKeep, 'principal component 2'], c = color, s = 50)

ax.legend(targets)
ax.grid()


plt.scatter(X[:,0], X[:,1])
plt.show()

'''
X = StandardScaler().fit_transform(X)
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(X)

principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])
finalDf = pd.concat([principalDf, df[['Sesso']]], axis = 1)
print(finalDf)

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
targets = ['0', '1'] #0M 1F
colors = ['r', 'g']

finaldata = finalDf.values

for target, color in zip(targets,colors):
    indicesToKeep = finalDf['Sesso'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'], finalDf.loc[indicesToKeep, 'principal component 2'], c = color, s = 50)

print(pca.explained_variance_ratio_)

ax.legend(targets)
ax.grid()
plt.show()
'''
'''
#Correlation Matrix
corrmat = dataframe.corr() 
f, ax = plt.subplots(figsize =(9, 8)) 
sns.heatmap(corrmat, ax = ax, cmap ="YlGnBu", linewidths = 0.1) 
print(corrmat)
plt.show()

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)
y_kmeans = kmeans.fit(X)
centers = kmeans.cluster_centers_
print(centers)
new_labels=kmeans.labels_
print(new_labels)

plt.scatter(X[:,0],X[:,1], c=new_labels, cmap='viridis', edgecolor='k', s=50)
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s = 300, c = 'red', label = 'Centroids')

#Silhouette
print(silhouette_score(X,kmeans.labels_, metric="euclidean"))

plt.legend()
plt.show()
#Elbow's number
visualizer = KElbowVisualizer(kmeans, k=(2,6), metric='silhouette', timings=False)

visualizer.fit(X)
visualizer.poof()
'''
