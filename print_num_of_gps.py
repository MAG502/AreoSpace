#!/usr/bin/env python3

from pymavlink import mavutil

# master = mavutil.mavlink_connection('tcp:127.0.0.1:5763')

# master.wait_heartbeat()
# print('Got Heartbeat.\n')
def gps_check(master):
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL,
        0,
        mavutil.mavlink.MAVLINK_MSG_ID_GPS_RAW_INT,
        1000000,
        0, 0, 0, 0, 0
    )

    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL,
        0,
        mavutil.mavlink.MAVLINK_MSG_ID_GPS2_RAW,
        1000000,
        0, 0, 0, 0, 0
    )

    gps_values = master.recv_match(type='GPS_RAW_INT', blocking=True, timeout=2)
    gps_values2 = master.recv_match(type='GPS2_RAW', blocking=True, timeout=2)

    number_of_gps = 0

    pr1, pr2  = '', ''
    if gps_values:
        pr1 = f'...Found a {gps_values.msgname} Gps'
        number_of_gps += 1

    if gps_values2:
        pr2 = f'\n...Found a {gps_values2.msgname} Gps'
        number_of_gps += 1

    print(pr1 + pr2)
    return(f'Number Of GPS: {number_of_gps}')
