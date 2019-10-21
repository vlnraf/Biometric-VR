from clusteringKmedoids import KMedoids
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def example_distance_func(data1, data2):
    '''example distance function'''
    return np.sqrt(np.sum((data1 - data2)**2))

if __name__ == '__main__':
    #X = np.random.normal(0,3,(500,2))
    dataframe = pd.read_csv('datasetCompatto.csv')
    dataset = dataframe.values

    X = dataset[:,0:4]

    model = KMedoids(n_clusters=2, dist_func=example_distance_func)
    model.fit(X, plotit=True, verbose=True)
    plt.show()
