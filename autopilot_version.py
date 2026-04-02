from pymavlink import mavutil

master = mavutil.mavlink_connection('tcp:127.0.0.1:5763')

master.wait_heartbeat()
print('Got Heartbeat.\n')

master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE,
    0,
    mavutil.mavlink.MAVLINK_MSG_ID_AUTOPILOT_VERSION,
    0, 0, 0, 0, 0, 0,
)

autopilot_version_values = master.recv_match(type='AUTOPILOT_VERSION', blocking=True, timeout=1)

firmware_types = {
    0: "dev",
    64: "alpha",
    128: "beta",
    192: "rc",
    255: "official"
}

if autopilot_version_values:
    autopilot_vresion = autopilot_version_values.flight_sw_version
    major = (autopilot_vresion >> 24) & 0xFF
    minor = (autopilot_vresion >> 16) & 0xFF
    patch = (autopilot_vresion >> 8) & 0xFF
    version_type = autopilot_vresion & 0xFF

    print(
        f'Major: {major}\n'
        f'Minor: {minor}\n'
        f'Patch: {patch}\n'
        f'Vesion Type: {firmware_types[version_type]}'
    )
