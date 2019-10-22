#!/usr/bin/env python

import time
import pprint
import openvr
import triad_openvr
import sys
import math
import os
import csv


"""
Get the HTC Vive controllers keypresses and print them to screen.
You need to do:
export LD_LIBRARY_PATH=$HOME/.steam/steam/steamapps/common/SteamVR/bin/linux64:$HOME/.steam/steam/steamapps/common/tools/bin/linux64:$LD_LIBRARY_PATH
before executing it.
Expected output:
Left controller:
{   'grip_button': False,
    'menu_button': False,
    'trackpad_pressed': False,
    'trackpad_touched': True,
    'trackpad_x': 0.032959990203380585,
    'trackpad_y': -0.8471328020095825,
    'trigger': 0.0,
    'ulButtonPressed': 0L,
    'ulButtonTouched': 4294967296L,
    'unPacketNum': 2037L}
Right controller:
{   'grip_button': False,
    'menu_button': False,
    'trackpad_pressed': False,
    'trackpad_touched': False,
    'trackpad_x': 0.0,
    'trackpad_y': 0.0,
    'trigger': 0.0,
    'ulButtonPressed': 0L,
    'ulButtonTouched': 0L,
    'unPacketNum': 1146L}
Author: Sammy Pfeiffer <Sammy.Pfeiffer at student.uts.edu.au>
"""


def get_controller_ids(vrsys=None):
    if vrsys is None:
        vrsys = openvr.VRSystem()
    else:
        vrsys = vrsys
    left = None
    right = None
    for i in range(openvr.k_unMaxTrackedDeviceCount):
        device_class = vrsys.getTrackedDeviceClass(i)
        if device_class == openvr.TrackedDeviceClass_Controller:
            role = vrsys.getControllerRoleForTrackedDeviceIndex(i)
            if role == openvr.TrackedControllerRole_RightHand:
                right = i
            if role == openvr.TrackedControllerRole_LeftHand:
                left = i
    return left, right


def from_controller_state_to_dict(pControllerState):
    # docs: https://github.com/ValveSoftware/openvr/wiki/IVRSystem::GetControllerState
    d = {}
    d['unPacketNum'] = pControllerState.unPacketNum
    # on trigger .y is always 0.0 says the docs
    d['trigger'] = pControllerState.rAxis[1].x
    # 0.0 on trigger is fully released
    # -1.0 to 1.0 on joystick and trackpads
    d['trackpad_x'] = pControllerState.rAxis[0].x
    d['trackpad_y'] = pControllerState.rAxis[0].y
    # These are published and always 0.0
    # for i in range(2, 5):
    #     d['unknowns_' + str(i) + '_x'] = pControllerState.rAxis[i].x
    #     d['unknowns_' + str(i) + '_y'] = pControllerState.rAxis[i].y
    d['ulButtonPressed'] = pControllerState.ulButtonPressed
    d['ulButtonTouched'] = pControllerState.ulButtonTouched
    # To make easier to understand what is going on
    # Second bit marks menu button
    d['menu_button'] = bool(pControllerState.ulButtonPressed >> 1 & 1)
    # 32 bit marks trackpad
    d['trackpad_pressed'] = bool(pControllerState.ulButtonPressed >> 32 & 1)
    d['trackpad_touched'] = bool(pControllerState.ulButtonTouched >> 32 & 1)
    # third bit marks grip button
    d['grip_button'] = bool(pControllerState.ulButtonPressed >> 2 & 1)
    # System button can't be read, if you press it
    # the controllers stop reporting
    return d


#if __name__ == '__main__':
max_init_retries = 4
retries = 0
print("===========================")
print("Initializing OpenVR...")
while retries < max_init_retries:
    try:
        openvr.init(openvr.VRApplication_Background)
        poses = []
        break
    except openvr.OpenVRError as e:
        print("Error when initializing OpenVR (try {} / {})".format(
              retries + 1, max_init_retries))
        print(e)
        retries += 1
        time.sleep(2.0)
else:
    print("Could not initialize OpenVR, aborting.")
    print("Make sure the system is correctly plugged, you can also try")
    print("to do:")
    print("killall -9 vrcompositor vrmonitor vrdashboard")
    print("Before running this program again.")
    exit(0)

print("Success!")
print("===========================")
vrsystem = openvr.VRSystem()

left_id, right_id = None, None
print("===========================")
print("Waiting for controllers...")
try:
    while left_id is None or right_id is None:
        left_id, right_id = get_controller_ids(vrsystem)
        if left_id and right_id:
            break
        print("Waiting for controllers...")
        time.sleep(1.0)
except KeyboardInterrupt:
    print("Control+C pressed, shutting down...")
    openvr.shutdown()

print("Left controller ID: " + str(left_id))
print("Right controller ID: " + str(right_id))
print("===========================")

pp = pprint.PrettyPrinter(indent=4)

reading_rate_hz = 250
show_only_new_events = True
last_unPacketNum_left = 0
last_unPacketNum_right = 0

print("===========================")
print("Printing controller events!")
try:
    ttt = True

    while ttt:
        time.sleep(1.0 / reading_rate_hz)
        result, pControllerState = vrsystem.getControllerState(left_id)
        d = from_controller_state_to_dict(pControllerState)
        result2, pControllerState2 = vrsystem.getControllerState(right_id)
        d2 = from_controller_state_to_dict(pControllerState2)
        #if show_only_new_events and last_unPacketNum_left != d['unPacketNum']:
        last_unPacketNum_left = d['unPacketNum']
        if(float(d["trigger"]) > 0.3 or float(d2["trigger"]) > 0.3):
            #numb = input()
            #int_numb = int(numb)

            #if(int_numb == 1):
            v = triad_openvr.triad_openvr()
            #v.print_discovered_objects()        #Stampa oggetti connessi

            t_end = time.time() +60*1.84;         #Tempo che il programma è in esecuzione (in questo caso 1 minuto)

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
                with open('dati/'+str(sys.argv[2])+'/1_'+str(sys.argv[1])+str(sys.argv[2])+'.csv', mode='w', newline='') as csv_file:
                    fieldnames = ['x', 'y', 'z', 'x2', 'y2', 'z2','altezza']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    while(time.time() < t_end):
                        controller_1 = v.devices["controller_1"].get_pose_euler()
                        controller_2 = v.devices["controller_2"].get_pose_euler()
                        hmd = v.devices["hmd_1"].get_pose_euler()
                        start = time.time()
                        writer.writerow({'x': "%.2f" %controller_1[0], 'y': "%.2f" %controller_1[1], 'z': "%.2f" %controller_1[2], 'x2': "%.2f" %controller_2[0], 'y2': "%.2f" %controller_2[1], 'z2': "%.2f" %controller_2[2],'altezza' : "%.2f" %hmd[1]})
                        #writer.writerow({'x': '0.12', 'y': '0.13', 'z': '0.14'})
                        sleep_time = interval-(time.time()-start)           #Calcolo del tempo T, che serve per stampare ogni T
                        if sleep_time>0:
                            time.sleep(sleep_time)

            ttt = False

except KeyboardInterrupt:
    print("Control+C pressed, shutting down...")
    openvr.shutdown()
