import pandas as pd


# Importing the dataset
dataframe = pd.read_csv('dataset1.csv')

dataset = dataframe.values

X = dataset[:,0:4]
y = dataset[:,4]

sommadist = 0
mediadist = 0

for i in range(0,30):
	for j in range(0,330):
		sommadist = X[:,0] + sommadist
	mediadist = sommadist/330