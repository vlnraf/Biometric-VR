import matplotlib.pyplot as plt
import sys
import csv



if len(sys.argv) <= 1:
    print("Parametri non corretti")
else:

    #fig = plt.figure()

    t = 1
    tempotot = 110.4

    with open("dati/"+str(sys.argv[1])+"/distanzaController.csv", "r") as csvfile:
        '''if csvfile.mode == "r":
            f = csvfile.readlines() #Estrarre gli elementi leggendo solo la linea
        '''

        #Rimozione header

        readCSV = csv.reader(csvfile)
        
        if csv.Sniffer().has_header:
            next(csvfile)

        
        #VELOCITA' DISTANZA TRA DUE CONTROLLER

        vel = []
        dis = []
        temp = []

        for row in readCSV:
            dis.append(float(row[0]))

        print(dis)

        distot = 0
        for i in dis:
            distot += i

        velocita = distot/tempotot
        print(velocita)

        #k = 1
        '''for i in range(0, len(dis)-1):
            temp.append(abs(dis[k] - dis[i]))        #abs probabilmente tronca i num negativi
            k += 1
            vel.append(round(temp[i] / t, 1))
		'''


    with open("dati/"+str(sys.argv[1])+"/distanzaSingoliController.csv", "r") as csvfile1:
        '''if csvfile.mode == "r":
            f = csvfile.readlines() #Estrarre gli elementi leggendo solo la linea
        '''

        #Rimozione header

        readCSVmani = csv.reader(csvfile1, delimiter=',')
        
        if csv.Sniffer().has_header:
            next(csvfile1)


        veldx = []
        disdx = []
        tempdx = []
        velsx = []
        dissx = []
        tempsx = []
        disdxtot = 0.0
        dissxtot = 0.0 

        #VELOCITA' CONTROLLER DESTRO
        
        for row in readCSVmani:
            disdx.append(float(row[0]))
            dissx.append(float(row[1]))

        
        for i in dissx:
        	dissxtot += i 

        velocitasx = dissxtot/tempotot

        for i in disdx:
        	disdxtot += i 

        velocitadx = disdxtot/tempotot


        print(velocitadx)
        print(velocitasx)
   
        '''
        k = 1
        for i in range(0, len(disdx)-1):
            tempdx.append(abs(disdx[k] - disdx[i]))        #abs probabilmente tronca i num negativi
            k += 1
            veldx.append(round(tempdx[i] / t, 1))

        print(veldx)

        #VELOCITA' CONTROLLER SINISTRO

        k = 1
        for i in range(0, len(dissx)-1):
            tempsx.append(abs(dissx[k] - dissx[i]))        #abs probabilmente tronca i num negativi
            k += 1
            velsx.append(round(tempsx[i] / t, 1))
            
    print(velsx)
	'''


'''print(vel)
plt.plot(vel)
plt.show()'''
