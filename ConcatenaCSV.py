import pandas as pd
import glob

path = 'dati/Emilio' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    if filename == 'dati/Emilio/1_3Emilio.csv':
        continue
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

result = pd.concat(li, axis = 1, sort = False)


#combined_csv = pd.concat(li, axis=0, ignore_index=True, sort = False)

result.to_csv("dati/Emiliocombined_csv.csv", index=False, encoding='utf-8-sig')

#combined_csv.to_csv("dati/Emilio/combined_csv.csv", index=False, encoding='utf-8-sig')

