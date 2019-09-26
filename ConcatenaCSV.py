import pandas as pd
import glob
import sys
import matplotlib.pyplot as plt

path = 'dati/'+ str(sys.argv[1]) # use your path
all_files = glob.glob(path + "/*.csv")
li = []

for filename in all_files:
    if filename == 'dati/'+str(sys.argv[1])+'/1_3'+str(sys.argv[1])+'.csv':
        continue
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

result = pd.concat(li, axis = 1, sort = False)

combined_csv = pd.concat(li, axis=0, ignore_index=True, sort = False) #per combinare più files uno sotto l' altro

result.to_csv('dati/datiCompleti/'+str(sys.argv[1])+'.csv', index=False, encoding='utf-8-sig')

#combined_csv.to_csv("dati/Emilio/combined_csv.csv", index=False, encoding='utf-8-sig')

result.plot()
plt.show()
