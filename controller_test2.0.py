import triad_openvr
import time
import sys
import math
import os

v = triad_openvr.triad_openvr()
#v.print_discovered_objects()        #Stampa oggetti connessi

t_end = time.time() +60*2;         #Tempo che il programma è in esecuzione (in questo caso 1 minuto)

#if len(sys.argv) == 1:
#    interval = 1/100            #Intervallo di tempo per cui stampare i dati (in questo caso 1 secondi)
if len(sys.argv) >= 1:
    interval = 1/float(sys.argv[1])

path = os.getcwd()
try:
	os.mkdir(path + "/dati/" + str(sys.argv[2]))
    #os.mkdir(path + "/dati/1_"+str(sys.argv[1]))
except OSError:
	print("Direcotry gia esistente o creazione fallita")
else:
	print("Direcotry creata")

if interval:
    dx = open(path + "/dati/"+str(sys.argv[2])+"/1_"+str(sys.argv[1])+"destraX.txt","w+")
    dy = open(path + "/dati/"+str(sys.argv[2])+"/1_"+str(sys.argv[1])+"destraY.txt","w+")
    dz = open(path + "/dati/"+str(sys.argv[2])+"/1_"+str(sys.argv[1])+"destraZ.txt","w+")
    sx = open(path + "/dati/"+str(sys.argv[2])+"/1_"+str(sys.argv[1])+"sinistraX.txt","w+")
    sy = open(path + "/dati/"+str(sys.argv[2])+"/1_"+str(sys.argv[1])+"sinistraY.txt","w+")
    sz = open(path + "/dati/"+str(sys.argv[2])+"/1_"+str(sys.argv[1])+"sinistraZ.txt","w+")
    while(time.time() < t_end):
        start = time.time()
        txt = ""
        controller_1 = v.devices["controller_1"].get_pose_euler()
        controller_2 = v.devices["controller_2"].get_pose_euler()
        dx.write("%.2f \n" %controller_1[0])
        dy.write("%.2f \n" %controller_1[1])
        dz.write("%.2f \n" %controller_1[2])
        sx.write("%.2f \n" %controller_2[0])
        sy.write("%.2f \n" %controller_2[1])
        sz.write("%.2f \n" %controller_2[2])
        sleep_time = interval-(time.time()-start)           #Calcolo del tempo T, che serve per stampare ogni T
        if sleep_time>0:
            time.sleep(sleep_time)

    dx.close()
    dy.close()
    dz.close()
    sx.close()
    sy.close()
    sz.close()


