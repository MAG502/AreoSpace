from pymavlink import mavutil

master = mavutil.mavlink_connection('udp:127.0.0.1:14550')

master.wait_heartbeat()
print('Got Heartbeat.\n')

master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL,
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
    pr1 = f'Sensor {imu_senesor_values.msgname.replace("SCALED_", "")} dedecated'
    number_of_senesors += 1

if imu_senesor_values2:
    pr2 = f'\nSensor {imu_senesor_values2.msgname.replace("SCALED_", "")} dedecated'
    number_of_senesors += 1
    
if imu_senesor_values3:
    pr3 = f'\nSensor {imu_senesor_values3.msgname.replace("SCALED_", "")} dedecated'
    number_of_senesors += 1

print(pr1 + pr2 + pr3)
print(f'The Number Of Senesors Dedecated: {number_of_senesors}')