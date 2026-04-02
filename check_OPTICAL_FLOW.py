from pymavlink import mavutil

# master = mavutil.mavlink_connection('tcp:127.0.0.1:5763')
master = mavutil.mavlink_connection('/dev/tty.usbmodem01')

master.wait_heartbeat()
print('Got Heartbeat.\n')

master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE,
    0,
    mavutil.mavlink.MAVLINK_MSG_ID_OPTICAL_FLOW,
    0, 0, 0, 0, 0, 0
)

optical_flow_values = master.recv_match(type='OPTICAL_FLOW', blocking=True, timeout=1)

if optical_flow_values:
    print(f'The {optical_flow_values.flow_x} is dedected')
else:
    print(f'No Optical Flow Found')
