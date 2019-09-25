import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import math
import sys

if len(sys.argv) <= 1:
    print("Parametri non corretti")

else:
    fig = plt.figure()
    dx = open("dati/" + str(sys.argv[2]) + "/1_" + str(sys.argv[1]) + "destraX.txt", "r")
    dy = open("dati/" + str(sys.argv[2]) + "/1_" + str(sys.argv[1]) + "destraY.txt", "r")
    dz = open("dati/" + str(sys.argv[2]) + "/1_" + str(sys.argv[1]) + "destraZ.txt", "r")
    dx2 = open("dati/" + str(sys.argv[3]) + "/1_" + str(sys.argv[1]) + "destraX.txt", "r")
    dy2 = open("dati/" + str(sys.argv[3]) + "/1_" + str(sys.argv[1]) + "destraY.txt", "r")
    dz2 = open("dati/" + str(sys.argv[3]) + "/1_" + str(sys.argv[1]) + "destraZ.txt", "r")
    finale = open("dati/" + str(sys.argv[2]) + "/manoDx.txt", "w+")

    x1 = []
    y1 = []
    z1 = []

    x2 = []
    y2 = []
    z2 = []

    if dx.mode == "r":
        destraX = dx.readlines()
        destraY = dy.readlines()
        destraZ = dz.readlines()
        destraX2 = dx2.readlines()
        destraY2 = dy2.readlines()
        destraZ2 = dz2.readlines()

        for i in destraX:
            s = float(i)
            x1.append(s)

        for i in destraY:
            s = float(i)
            y1.append(s)

        for i in destraZ:
            s = float(i)
            z1.append(s)

        for i in destraX2:
            s = float(i)
            x2.append(s)

        for i in destraY2:
            s = float(i)
            y2.append(s)

        for i in destraZ2:
            s = float(i)
            z2.append(s)

    xx = []
    yy = []
    zz = []
    xyz = []
    sqxyz = []
    xx2 = []
    yy2 = []
    zz2 = []
    xyz2 = []
    sqxyz2 = []
    #dist = []
    #c = 0.0

    for i in range(1, len(x1)):
        x = x1[i] - x1[i - 1]
        x = x * x
        xp = x2[i] - x2[i - 1]
        xp = xp * xp
        xx.append(x)
        xx2.append(xp)

    for i in range(1, len(y1)):
        y = y1[i] - y1[i - 1]
        y = y * y
        yp = y2[i] - y2[i - 1]
        yp = yp * yp
        yy.append(y)
        yy2.append(yp)

    for i in range(1, len(z1)):
        z = z1[i] - z1[i - 1]
        z = z * z
        zp = z2[i] - z2[i - 1]
        zp = zp * zp
        zz.append(z)
        zz2.append(zp)

    for i in range(0, len(xx)):
        xyz.append(xx[i] + yy[i] + zz[i])
        xyz2.append(xx2[i] + yy2[i] + zz2[i])

    for i in range(0, len(xyz)):
        sqxyz.append(round(math.sqrt(xyz[i]), 2))
        sqxyz2.append(round(math.sqrt(xyz2[i]), 2))

    assex = []
    for i in range(0, len(sqxyz)):  # serve per ricavarmi l' asse x del grafico
        assex.append(i)

    # f = interp1d(assex, sqxyz)  #interpola il movimento di y con il numero di dati

    '''for i in range(0, len(xyz)-1):        #Distanza totale percorsa
        c = c + round(math.sqrt(xyz[i]),2)
        dist.append(c)'''

    for i in sqxyz:
        finale.write("%.1f \n" % i)

    finale.close()

    #print(dist)
    primo = mpatches.Patch(color='red', label=sys.argv[2])
    secondo = mpatches.Patch(color='blue', label=sys.argv[3])
    plt.legend(handles=[primo,secondo])
    plt.plot(assex, sqxyz, color='red')
    plt.plot(assex, sqxyz2, color = 'blue')
    #plt.plot(dist)      #Stampa distanza percorsa

    plt.show()
