#!/usr/bin/env python3

from pymavlink import mavutil

# master = mavutil.mavlink_connection('/dev/tty.usbmodem1101')
# master = mavutil.mavlink_connection('tcp:127.0.0.1:5763')

# master.wait_heartbeat()
# print('Got Heartbeat\n')
def gimbal_info(master):
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE,
        0,
        mavutil.mavlink.MAVLINK_MSG_ID_GIMBAL_MANAGER_INFORMATION,
        0, 0, 0, 0, 0, 0
    )

    gimbal_info_values = master.recv_match(type='GIMBAL_MANAGER_INFORMATION', blocking=True, timeout=1)

    gimbal_caps = {
        1: "has retract",
        2: "has neutral",
        4: "has roll axis",
        8: "has roll follow",
        16: "has roll lock",
        32: "has pitch axis",
        64: "has pitch follow",
        128: "has pitch lock",
        256: "has yaw axis",
        512: "has yaw follow",
        1024: "has yaw lock",
        2048: "supports infinite yaw",
        4096: "supports yaw in earth frame",
        8192: "has rc inputs",
        65536: "can point location local",
        131072: "can point location global"
    }

    if gimbal_info_values:
        return(
            f'Device Id: {gimbal_info_values.gimbal_device_id}\n'
            f'Roll Min and Max: {gimbal_info_values.roll_min}, {gimbal_info_values.roll_max}\n'
            f'Pitch Min and Max: {gimbal_info_values.pitch_min}, {gimbal_info_values.pitch_max}\n'
            f'Yaw Min and Max: {gimbal_info_values.yaw_min}, {gimbal_info_values.yaw_max}\n'
            f'Gimbal capabilities: {gimbal_info_values.cap_flags}'
        )

    else:
        return('No Gambil Found.')

# print(gimbal_info(master))