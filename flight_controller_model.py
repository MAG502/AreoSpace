#!/usr/bin/env python3

from pymavlink import mavutil
import time
import serial

board_types = {
    5: "FMU_V1",
    6: "FLOW_V1",
    9: "FMU_V2",
    10: "PIO_V1",
    11: "FMU_V4",
    13: "FMU_V4_PRO",
    50: "FMU_V5",
    51: "FMU_V5X",
    52: "FMU_V6",
    53: "FMU_V6X",
    56: "FMU_V6C",
    98: "AEROCORE_V1",
    99: "DISCOVERY_V1",
}
port = '/dev/cu.usbmodem101'
master = mavutil.mavlink_connection(port)

master.wait_heartbeat()
print('Got Heartbeat.\n')

master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_PREFLIGHT_REBOOT_SHUTDOWN,
    0,
    3,
    0, 0, 0, 0, 0, 0
)
master.close()
time.sleep(2)
ser = serial.Serial(port, 115200, timeout=1)

BOARD_ID = b'\x22\x02\x20'

ser.reset_input_buffer()
ser.write(BOARD_ID)
ser.flush()
board_id = ser.read(4)
board_id2 = list(board_id)

board_types = board_types.get(board_id2[0], 'Unknown')

print(f"Board ID Name: {board_types}")
