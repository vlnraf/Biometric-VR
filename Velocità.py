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

        
        #VELOCITÀ DISTANZA TRA DUE CONTROLLER

        vel = []
        dis = []
        temp = []


        #VELOCITÀ SCALARE MEDIA
        for row in readCSV:
            dis.append(float(row[0]))

        distot = 0
        for i in dis:
            distot += i

        velocita = distot/tempotot

        #VELOCITÀ MEDIA AL SECONDO DA CAMBIARE FORSE
        #MOLTIPLICANDO TUTTO CON 0,3 OPPURE DIVIDENDO CON 3

        i=0
        while i < len(dis):
            #temp1 = dis[i] + dis[i-1] + dis[i-2]
            temp1 = dis[i]*0.3
            vel.append(round(temp1, 2))
            #i += 3
            i += 1

        #print(len(vel))

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
        
        file=open('dati/'
            +str(sys.argv[1])+'/1_3'
            +str(sys.argv[1])+'.csv',"r")

        #Rimozione header

        readCSVmani = csv.reader(csvfile1, delimiter=',')
        
        if csv.Sniffer().has_header:
            next(csvfile1)


        velDx = []
        disdx = []
        tempdx = []
        velSx = []
        dissx = []
        tempsx = []
        disdxtot = 0.0
        dissxtot = 0.0 

        #VELOCITA' MEDIA CONTROLLER SINGOLI SCALARE
        
        for row in readCSVmani:
            disdx.append(float(row[0]))
            dissx.append(float(row[1]))

        
        for i in dissx:
        	dissxtot += i

        velocitasx = dissxtot/tempotot

        for i in disdx:
        	disdxtot += i

        velocitadx = disdxtot/tempotot

        #VELOCITÀ MEDIA CONTROLLER SINGOLI AL SECONDO DA CAMBIARE FORSE
        #MOLTIPLICANDO TUTTO CON 0,3 OPPURE DIVIDENDO CON 3

        i=0
        while i < len(disdx):
            #temp2 = dissx[i] + dissx[i-1] + dissx[i-2]
            temp2 = disdx[i]*0.3 
            velDx.append(round(temp2, 2))
            #i += 3
            i += 1

        #print(len(velDx))
            

        i=0
        while i < len(dissx):
            #temp3 = disdx[i] + disdx[i-1] + disdx[i-2]
            temp3 = dissx[i]*0.3 
            velSx.append(round(temp3, 2))
            #i += 3
            i += 1 

        #print(len(velSx))

        with open('dati/'+str(sys.argv[1])+'/evelocity.csv','w',newline='') as file:
            fieldnames=['velocityDx','velocitySx','velocity']
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            writer.writeheader()
            for s in range(0,len(velDx)):
                writer.writerow({'velocityDx':"%f" %velDx[s],'velocitySx':"%f" %velSx[s],'velocity':"%f" %vel[s]})
    #print(velSx)


'''print(vel)
plt.plot(vel)
plt.show()'''
