from pymavlink import mavutil
from static import baro_types, bustypes, compass_types, imu_types, airspeed_types

master = mavutil.mavlink_connection('tcp:127.0.0.1:5763')
master.wait_heartbeat()
print('Got Heartbeat.')



def baro_param(master):
    master.param_fetch_one('BARO1_DEVID')
    master.param_fetch_one('BARO2_DEVID')
    master.param_fetch_one('BARO3_DEVID')

    param1 = master.recv_match(type='PARAM_VALUE', blocking=True, timeout=1)
    param2 = master.recv_match(type='PARAM_VALUE', blocking=True, timeout=1)
    param3 = master.recv_match(type='PARAM_VALUE', blocking=True, timeout=1)
    
    param_name1, param_value1 = param1.param_id, param1.param_value
    param_name2, param_value2 = param2.param_id, param2.param_value
    param_name3, param_value3 = param3.param_id, param3.param_value

    prints(param_name1, param_value1)
    prints(param_name2, param_value2)
    prints(param_name3, param_value3)


def compass_param(master):
    master.param_fetch_one('COMPASS_DEV_ID')
    master.param_fetch_one('COMPASS_DEV_ID2')
    master.param_fetch_one('COMPASS_DEV_ID3')

    param1 = master.recv_match(type='PARAM_VALUE', blocking=True, timeout=1)
    param2 = master.recv_match(type='PARAM_VALUE', blocking=True, timeout=1)
    param3 = master.recv_match(type='PARAM_VALUE', blocking=True, timeout=1)
    
    param_name1, param_value1 = param1.param_id, param1.param_value
    param_name2, param_value2 = param2.param_id, param2.param_value
    param_name3, param_value3 = param3.param_id, param3.param_value
    
    prints(param_name1, param_value1)
    prints(param_name2, param_value2)
    prints(param_name3, param_value3)

def ins_acc_param(master):
    master.param_fetch_one('INS_ACC_ID')
    master.param_fetch_one('INS_ACC2_ID')
    master.param_fetch_one('INS_ACC3_ID')

    param1 = master.recv_match(type='PARAM_VALUE', blocking=True, timeout=1)
    param2 = master.recv_match(type='PARAM_VALUE', blocking=True, timeout=1)
    param3 = master.recv_match(type='PARAM_VALUE', blocking=True, timeout=1)

    param_name1, param_value1 = param1.param_id, param1.param_value
    param_name2, param_value2 = param2.param_id, param2.param_value
    param_name3, param_value3 = param3.param_id, param3.param_value

    prints(param_name1, param_value1)
    prints(param_name2, param_value2)
    prints(param_name3, param_value3)

def ins_gyr_param(master):
    master.param_fetch_one('INS_GYR_ID')
    master.param_fetch_one('INS_GYR2_ID')
    master.param_fetch_one('INS_GYR3_ID')

    param1 = master.recv_match(type='PARAM_VALUE', blocking=True, timeout=1)
    param2 = master.recv_match(type='PARAM_VALUE', blocking=True, timeout=1)
    param3 = master.recv_match(type='PARAM_VALUE', blocking=True, timeout=1)

    param_name1, param_value1 = param1.param_id, param1.param_value
    param_name2, param_value2 = param2.param_id, param2.param_value
    param_name3, param_value3 = param3.param_id, param3.param_value

    prints(param_name1, param_value1)
    prints(param_name2, param_value2)
    prints(param_name3, param_value3)

def arspd_param(master):
    master.param_fetch_one('ARSPD_DEVID')

    param = master.recv_match(type='PARAM_VALUE', blocking=True, timeout=1)

    param_name, param_value = param.param_id, param.param_value

    prints(param_name, param_value)

def prints(param_id, param_value):
    param_value = int(param_value)
    bus_type = int(param_value) & 0x07
    bus = int(param_value >> 3) & 0x1F
    address = int(param_value >> 8) & 0xFF
    sensor_model = int(param_value >> 16)
    
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
        baro_param(master)
        number_of_try = 0
    
    elif name.startswith(('COMPASS', 'compass')):
        compass_param(master)
        number_of_try = 0
    
    elif name.startswith(('INS_ACC', 'ins_acc')):
        ins_acc_param(master)
        number_of_try = 0

    elif name.startswith(('INS_GYR', 'ins_gyr')):
        ins_gyr_param(master)
        number_of_try = 0
        
    elif name.startswith(('ARSPD', 'arspd')):
        arspd_param(master)
        number_of_try = 0
    
    else:
        print('\nPleas Enter Valid Sensor Name.\nNames: BARO, COMPASS, INS_ACC, INS_GYR, ARSPD\n')
        number_of_try += 1
        if number_of_try > 3:
            print('Excited Max Number Of Tries.')
            break
