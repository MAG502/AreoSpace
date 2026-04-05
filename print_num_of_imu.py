from pymavlink import mavutil

# master = mavutil.mavlink_connection('tcp:127.0.0.1:5763')

# master.wait_heartbeat()
# print('Got Heartbeat.\n')

def imu_check(master):
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE,
        0,
        mavutil.mavlink.MAVLINK_MSG_ID_SCALED_IMU,
        1000000,
        0, 0, 0, 0, 0
    )

    imu_senesor_values = master.recv_match(type='SCALED_IMU', blocking=True, timeout=1)
    imu_senesor_values2 = master.recv_match(type='SCALED_IMU2', blocking=True, timeout=1)
    imu_senesor_values3 = master.recv_match(type='SCALED_IMU3', blocking=True, timeout=1)

    number_of_senesors = 0

    pr1, pr2, pr3 = "", "", ""
    if imu_senesor_values:
        pr1 = f'...Sensor {imu_senesor_values.msgname.replace("SCALED_", "")} dedecated'
        number_of_senesors += 1

    if imu_senesor_values2:
        pr2 = f'\n...Sensor {imu_senesor_values2.msgname.replace("SCALED_", "")} dedecated'
        number_of_senesors += 1

    if imu_senesor_values3:
        pr3 = f'\n...Sensor {imu_senesor_values3.msgname.replace("SCALED_", "")} dedecated'
        number_of_senesors += 1

    print(pr1 + pr2 + pr3)
    return(f'The Number Of IMU Senesors Dedecated: {number_of_senesors}')