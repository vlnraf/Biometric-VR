import pandas
import math
import csv
import sys

df =  pandas.read_csv('dati/'
        +str(sys.argv[1])+'/1_3'
        +str(sys.argv[1])+'.csv', sep=',')


file=open('dati/'
        +str(sys.argv[1])+'/1_3'
        +str(sys.argv[1])+'.csv',"r")

x1=[]
y1=[]
z1=[]
x2=[]
y2=[]
z2=[]

'''for line in file:
    row_data = line.strip(',').split()
    for i, item in enumerate(row_data):
        try:
             row_data[i] = float(item)
        except ValueError:
             pass
    data.append(row_data)
'''

with open('dati/'
        +str(sys.argv[1])+'/1_3'
        +str(sys.argv[1])+'.csv',"r" )as csvFile:
    csvReader = csv.reader(csvFile)
    if csv.Sniffer().has_header:
        next(csvFile)
    for row in csvReader:
        x1.append(float(row[0]))
        y1.append(float(row[1]))
        z1.append(float(row[2]))
        x2.append(float(row[3]))
        y2.append(float(row[4]))
        z2.append(float(row[5]))
        #print(row)


xx=[]
yy=[]
zz=[]
xyz=[]
xyzDx=[]
xyzSx=[]
xxDx=[]
yyDx=[]
zzDx=[]
xxSx=[]
yySx=[]
zzSx=[]

sqxyz = []
sqxyzDx = []
sqxyzSx = []

for i in range(0,len(x1)):
    x = x1[i] - x2[i]
    x = x * x
    if i >= 1:
        xDx = x1[i] - x1[i-1]
        xSx = x2[i] - x2[i-1]
        tempDx = xDx * xDx
        tempSx = xSx * xSx
        xxDx.append(tempDx)
        xxSx.append(tempSx)
    xx.append(x)

for i in range(0,len(y1)):
    y = y1[i] - y2[i]
    y = y * y
    if i >= 1:
        yDx = y1[i] - y1[i-1]
        ySx = y2[i] - y2[i-1]
        tempDx = yDx * yDx
        tempSx = ySx * ySx
        yyDx.append(tempDx)
        yySx.append(tempSx)
    yy.append(y)

for i in range(0,len(z1)):
    z = z1[i] - z2[i]
    z = z * z
    if i >= 1:
        zDx = z1[i] - z1[i-1]
        zSx = z2[i] - z2[i-1]
        tempDx = zDx * zDx
        tempSx = zSx * zSx
        zzDx.append(tempDx)
        zzSx.append(tempSx)
    zz.append(z)

for i in range(0,len(xx)):
    xyz.append(xx[i]+yy[i]+zz[i])

for i in range(0, len(xxDx)):
    xyzDx.append(xxDx[i]+yyDx[i]+zzDx[i])
    xyzSx.append(xxSx[i]+yySx[i]+zzSx[i])

for i in range(0,len(xyz)):
    sqxyz.append(round(math.sqrt(xyz[i]),2))

for i in range(0, len(xyzDx)):
    sqxyzDx.append(round(math.sqrt(xyzDx[i]),2))
    sqxyzSx.append(round(math.sqrt(xyzSx[i]),2))

assex = []
for i in range (0, len(sqxyz)):     #serve per ricavarmi l' asse x del grafico
    assex.append(i)

# f = interp1d(assex, sqxyz)  #interpola il movimento di y con il numero di dati

with open('dati/'+str(sys.argv[1])+'/distanzaController.csv','w',newline='') as csv_file:
    fieldnames = ['distanza']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for numb in sqxyz:
        writer.writerow({'distanza':"%f" %numb})


with open('dati/'+str(sys.argv[1])+'/distanzaSingoliController.csv','w',newline='') as csv_file:
    fieldnames = ['distanzaDx','distanzaSx']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for numb2 in range(0,len(sqxyzDx)):
        writer.writerow({'distanzaDx':"%f" %sqxyzDx[numb2], 'distanzaSx':"%f" %sqxyzSx[numb2]})

#plt.show()
