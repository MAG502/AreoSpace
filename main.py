#!/usr/bin/env python3

from pymavlink import mavutil
from print_Autopilot_name import print_name, get_value
from print_Autopilot_pressure import pressure_check
from print_num_of_imu import imu_check
from print_num_of_gps import gps_check
from check_OPTICAL_FLOW import optical_check
from print_camera_info import camera_info
from gimbal_info import gimbal_info
from autopilot_version import autopilot_version
import tkinter


# master = mavutil.mavlink_connection('tcp:127.0.0.1:5762')
# master = mavutil.mavlink_connection('udpout:192.168.144.15:19856')
# master.mav.heartbeat_send(
    # mavutil.mavlink.MAV_TYPE_GCS,
    # mavutil.mavlink.MAV_AUTOPILOT_INVALID,
    # 0, 0, 0
# )
master = mavutil.mavlink_connection('/dev/tty.usbmodem1103')
master.wait_heartbeat()
print('Got Heartbeat.\n')

class All_Info:
    def __init__(self):
        self.master = master

    def values(self):
        value = get_value(self.master)
        return(f'Autopilot Value Name: {value}')

    def names(self):
        name = print_name(get_value(self.master))
        return(f'Autopilot Name: {name}')

    def Pressure_sensors(self):
        check = pressure_check(self.master)
        return check

    def imu_sensors(self):
        check = imu_check(self.master)
        return check
    
    def gps_num(self):
        check = gps_check(self.master)
        return check
    
    def optical_flow(self):
        check = optical_check(self.master)
        return check

    def cam_info(self):
        info = camera_info(self.master)
        return info
    
    def gimbal_info(self):
        info = gimbal_info(self.master)
        return info

    def autopilot_version(self):
        info = autopilot_version(self.master)
        return info


drone = All_Info()
print(drone.values())
print(drone.names())
print(drone.Pressure_sensors())
print(drone.imu_sensors())
print(drone.gps_num())
print(drone.optical_flow())
print(drone.cam_info())
print(drone.gimbal_info())
print(drone.autopilot_version())
