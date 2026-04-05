from pymavlink import mavutil

# master = mavutil.mavlink_connection('tcp:127.0.0.1:5763')
# master = mavutil.mavlink_connection('/dev/tty.usbmodem01')

# print("No Heartbeat yet!!")

# master.wait_heartbeat()

# print("Got Heartbeat!!\n")

def pressure_check(master):
    master.mav.request_data_stream_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_DATA_STREAM_ALL,
        4,
        1
    )

    number_of_sensors = 0
    msg_pressure1 = master.recv_match(type=['SCALED_PRESSURE'], blocking=True, timeout=1)
    msg_pressure2 = master.recv_match(type=['SCALED_PRESSURE2'], blocking=True, timeout=1)
    msg_pressure3 = master.recv_match(type=['SCALED_PRESSURE3'], blocking=True, timeout=1)


    msg1, msg2, msg3 = "", "", ""
    if msg_pressure1:    
        msg1 = f'...Sensor {msg_pressure1.msgname.replace("SCALED_","")} dedecated'
        number_of_sensors += 1

    if msg_pressure2:    
        msg2 = f'\n...Sensor {msg_pressure2.msgname.replace("SCALED_","")} dedecated'
        number_of_sensors += 1

    if msg_pressure3:    
        msg3 = f'\n...Sensor {msg_pressure3.msgname.replace("SCALED_","")} dedecated'
        number_of_sensors += 1

    print(msg1 + msg2 + msg3)

    if number_of_sensors > 1 or number_of_sensors == 0:
        result = f'{number_of_sensors} Pressure Sensors Dedecated'
    else:
        result = f'{number_of_sensors} Pressure Sensor Dedecated'

    return(result)