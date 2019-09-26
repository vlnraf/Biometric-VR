import pandas as pd
import glob
import sys
import matplotlib.pyplot as plt

path = ('dati/datiCompleti') # use your path
all_files = glob.glob(path + "/*.csv")
li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

result = pd.concat(li, axis=0, ignore_index=True, sort = False) #per combinare più files uno sotto l' altro

result.to_csv('dati/datiCompleti/dataset.csv', index=False, encoding='utf-8-sig')

