import matplotlib.pyplot as plt
import numpy as np
import math
import sys

if len(sys.argv) <= 1:
    print("Parametri non corretti")
    
else:
    fig = plt.figure()
    dx = open("dati/"+str(sys.argv[2])+"/1_"+str(sys.argv[1])+"destraX.txt","r")
    dy = open("dati/"+str(sys.argv[2])+"/1_"+str(sys.argv[1])+"destraY.txt","r")
    dz = open("dati/"+str(sys.argv[2])+"/1_"+str(sys.argv[1])+"destraZ.txt","r")
    sx = open("dati/"+str(sys.argv[2])+"/1_"+str(sys.argv[1])+"sinistraX.txt","r")
    sy = open("dati/"+str(sys.argv[2])+"/1_"+str(sys.argv[1])+"sinistraY.txt","r")
    sz = open("dati/"+str(sys.argv[2])+"/1_"+str(sys.argv[1])+"sinistraZ.txt","r")
    finale = open("dati/"+str(sys.argv[2])+"/finale.txt","w+")

    x1 = []
    y1 = []
    z1 = []
    x2 = []
    y2 = []
    z2 = []
    s = 0
    c = ""

    if dx.mode == "r":
        destraX = dx.readlines()
        destraY = dy.readlines()
        destraZ = dz.readlines()
        sinistraX = sx.readlines()
        sinistraY = sy.readlines()
        sinistraZ = sz.readlines()
        
        for i in destraX:
            s = float(i)
            x1.append(s)

        for i in destraY:
            s = float(i)
            y1.append(s)

        for i in destraZ:
            s = float(i)
            z1.append(s)

        for i in sinistraX:
            s = float(i)
            x2.append(s)

        for i in sinistraY:
            s = float(i)
            y2.append(s)

        for i in sinistraZ:
            s = float(i)
            z2.append(s)

    xx =[]
    yy = []
    zz = []
    xyz = []
    sqxyz = []

    for i in range(0,len(x1)):
        x = x1[i] - x2[i]
        x = x * x
        xx.append(x)

    for i in range(0,len(y1)):
        y = y1[i] - y2[i]
        y = y * y
        yy.append(y)

    for i in range(0,len(z1)):
        z = z1[i] - z2[i]
        z = z * z
        zz.append(z)

    for i in range(0,len(xx)):
        xyz.append(xx[i]+yy[i]+zz[i])

    for i in range(0,len(xyz)):
        sqxyz.append(round(math.sqrt(xyz[i]),1))

    assex = []
    for i in range (0, len(sqxyz)):     #serve per ricavarmi l' asse x del grafico
        assex.append(i)

   # f = interp1d(assex, sqxyz)  #interpola il movimento di y con il numero di dati

    for i in sqxyz:
        finale.write("%.1f \n" %i)

    finale.close()

    plt.plot(assex,sqxyz)

    plt.show()
