#!/usr/bin/env python3

from pymavlink import mavutil
from static import baro_types, bustypes, compass_types, imu_types, airspeed_types

master = mavutil.mavlink_connection('tcp:127.0.0.1:5763')
# master = mavutil.mavlink_connection('/dev/tty.usbmodem101')

master.wait_heartbeat()
print('Got Heartbeat.')

def fetch(master, param_list):
    for baro in param_list:
        master.param_fetch_one(baro)
        param = master.recv_match(type='PARAM_VALUE', blocking=True, timeout=1)
        prints(param.param_id, param.param_value)

def prints(param_id, param_value):
    
    param_value = int(param_value)
    bus_type = (param_value) & 0b111 #0x07
    bus = (param_value >> 3) & 0b11111 #0x1F
    address = (param_value >> 8) & 0b11111111 #0xFF
    sensor_model = (param_value >> 16)
    types = {}

    if param_id.startswith('BARO'):
        types = baro_types
    
    elif param_id.startswith('COMPASS'):
        types = compass_types
    
    elif param_id.startswith(('INS_ACC', 'INS_GYR')):
        types = imu_types
    
    elif param_id.startswith('ARSPD'):
        types = airspeed_types
    
    print(
        f'\nSensor Name: {param_id}\n'
        f'Bus Type: {bustypes.get(bus_type, "Unknown")}\n'
        f'Bus: {bus}\n'
        f'Address: {address}\n'
        f'Sensor Model: {types.get(sensor_model, "Unknown")}'
    )

number_of_try = 0
while True:
    name = input('Pleas Enter Sensor Name: ')
    
    if name.startswith(('BARO', 'baro')):
        baro_param = ['BARO1_DEVID', 'BARO2_DEVID', 'BARO3_DEVID']
        fetch(master, baro_param)
        number_of_try = 0
    
    elif name.startswith(('COMPASS', 'compass')):
        compass_param = ['COMPASS_DEV_ID', 'COMPASS_DEV_ID2', 'COMPASS_DEV_ID3']
        fetch(master, compass_param)
        number_of_try = 0
    
    elif name.startswith(('INS_ACC', 'ins_acc')):
        ins_acc_param = ['INS_ACC_ID', 'INS_ACC2_ID', 'INS_ACC3_ID']
        fetch(master, ins_acc_param)
        number_of_try = 0

    elif name.startswith(('INS_GYR', 'ins_gyr')):
        ins_gyr_param = ['INS_GYR_ID', 'INS_GYR2_ID', 'INS_GYR3_ID']
        fetch(master, ins_gyr_param)
        number_of_try = 0
        
    elif name.startswith(('ARSPD', 'arspd')):
        arspd_param = ['ARSPD_DEVID']
        fetch(master, arspd_param)
        number_of_try = 0
    
    else:
        print('\nPleas Enter Valid Sensor Name.\nNames: BARO, COMPASS, INS_ACC, INS_GYR, ARSPD\n')
        number_of_try += 1
        if number_of_try > 2:
            print('Exciting Max Number Of Tries.')
            break
