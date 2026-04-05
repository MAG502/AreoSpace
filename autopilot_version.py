from pymavlink import mavutil

# master = mavutil.mavlink_connection('tcp:127.0.0.1:5763')

# master.wait_heartbeat()
# print('Got Heartbeat.\n')
def autopilot_version(master):
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE,
        0,
        mavutil.mavlink.MAVLINK_MSG_ID_AUTOPILOT_VERSION,
        0, 0, 0, 0, 0, 0,
    )

    autopilot_version_message = master.recv_match(type='AUTOPILOT_VERSION', blocking=True, timeout=1)

    firmware_types = {
        0: "dev",
        64: "alpha",
        128: "beta",
        192: "rc",
        255: "official"
    }

    if autopilot_version_message:
        software_vresion = autopilot_version_message.flight_sw_version
        major = (software_vresion >> 24) & 0xFF
        minor = (software_vresion >> 16) & 0xFF
        patch = (software_vresion >> 8) & 0xFF
        version_type = software_vresion & 0xFF

        return f'Autopilot Vresion: {major}.{minor}.{patch}-{firmware_types[version_type]}'
