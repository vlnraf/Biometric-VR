import pandas as pd
import csv


# Importing the dataset
dataframe = pd.read_csv('dataset1.csv')

dataset = dataframe.values

X = dataset[:,0:4]
y = dataset[:,4]

arrmediadist = []
arrmediadistdx = []
arrmediadistsx = []

k = 0
z = 0
with open('datasetCompatto.csv', mode='w', newline='') as csv_file:
	fieldnames = ['distMedia', 'altezza', 'distDxMedia', 'distSxMedia', 'Sesso']
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	writer.writeheader()
	for i in range(0,30):
		sommadist = 0
		sommadistdx = 0
		sommadistsx = 0
		mediadist = 0
		mediadistdx = 0
		mediadistsx = 0
		for j in range(0,330):
			sommadist += dataframe.loc[k,'distanza']
			sommadistdx += dataframe.loc[k,'distanzaDx']
			sommadistsx += dataframe.loc[k,'distanzaSx']
			k+=1

		mediadist = sommadist/10
		arrmediadist.append(mediadist)
		mediadistdx = sommadistdx/330
		arrmediadistdx.append(mediadistdx)
		mediadistsx = sommadistsx/330
		arrmediadistsx.append(mediadistsx)
	
	for i in range(0,len(arrmediadist)):
		writer.writerow({'distMedia': "%.2f" %arrmediadist[i], 'altezza': "%.2f" %dataframe.loc[z,'altezza'], 'distDxMedia': "%.2f" %arrmediadistdx[i], 'distSxMedia': "%.2f" %arrmediadistsx[i], 'Sesso': "%.2f" %dataframe.loc[z,'Sesso']})
		z+=330