import matplotlib.pyplot as plt
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
    finale = open("dati/" + str(sys.argv[2]) + "/manoDx.txt", "w+")

    x1 = []
    y1 = []
    z1 = []

    if dx.mode == "r":
        destraX = dx.readlines()
        destraY = dy.readlines()
        destraZ = dz.readlines()

        for i in destraX:
            s = float(i)
            x1.append(s)

        for i in destraY:
            s = float(i)
            y1.append(s)

        for i in destraZ:
            s = float(i)
            z1.append(s)

    xx = []
    yy = []
    zz = []
    xyz = []
    sqxyz = []
    #dist = []
    #c = 0.0

    for i in range(1, len(x1)):
        x = x1[i] - x1[i - 1]
        x = x * x
        xx.append(x)

    for i in range(1, len(y1)):
        y = y1[i] - y1[i - 1]
        y = y * y
        yy.append(y)

    for i in range(1, len(z1)):
        z = z1[i] - z1[i - 1]
        z = z * z
        zz.append(z)

    for i in range(0, len(xx)):
        xyz.append(xx[i] + yy[i] + zz[i])

    for i in range(0, len(xyz)):
        sqxyz.append(round(math.sqrt(xyz[i]), 2))

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
    plt.plot(assex, sqxyz)
    #plt.plot(dist)      #Stampa distanza percorsa

    plt.show()
