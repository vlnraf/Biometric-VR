# K-Means Clustering

# Importing the libraries
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import seaborn as sns 
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from yellowbrick.cluster import KElbowVisualizer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

# Importing the dataset
df = pd.read_csv('datasetCompatto.csv')

#plt.hist(df[['distMedia']].values, bins=np.linspace(1.3, 2, 30), fc='#AAAAFF', normed=True)


dataset = df.values

X = dataset[:,0:4]
x = dataset[:,0:4]
y = dataset[:,4]

x = StandardScaler().fit_transform(x)

#PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)

principalDf = pd.DataFrame(data = principalComponents,
	 columns = ['principal component 1', 'principal component 2'])
finalDf = pd.concat([principalDf, df[['Sesso']]], axis = 1)
print(finalDf)

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
targets = [0,1] #0M 1F
colors = ['blue', 'red']

finaldata = finalDf.values

for target, color in zip(targets,colors):
    indicesToKeep = finalDf['Sesso'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'], finalDf.loc[indicesToKeep, 'principal component 2'], c = color, s = 50)

print(pca.explained_variance_ratio_)

ax.legend(targets)
ax.grid()
plt.show()

#Correlation Matrix
corrmat = df.corr() 
f, ax = plt.subplots(figsize =(9, 8)) 
sns.heatmap(corrmat, ax = ax, cmap ="YlGnBu", linewidths = 0.1) 
print(corrmat)
plt.show()

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)
y_kmeans = kmeans.fit(X)
centers = kmeans.cluster_centers_
print(centers)
new_labels=kmeans.labels_
print(new_labels)

for target, color in zip(targets,colors):
    indicesToKeep = df['Sesso'] == target
    plt.scatter(df.loc[indicesToKeep,'distMedia'], df.loc[indicesToKeep,'altezza'], c = color, edgecolor='k', s=50)


plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s = 250, c = 'black', marker='*')

#Silhouette
print(silhouette_score(X,kmeans.labels_, metric="euclidean"))


blue_patch = mpatches.Patch(color='blue', label='Maschio')
red_patch = mpatches.Patch(color='red', label='Femmina')
black_patch = mpatches.Patch(color='black', label='Centroids')
plt.legend(handles=[red_patch,blue_patch,black_patch])

plt.show()
#Elbow's number
visualizer = KElbowVisualizer(kmeans, k=(2,6), metric='silhouette', timings=False)

visualizer.fit(X)
visualizer.poof()
