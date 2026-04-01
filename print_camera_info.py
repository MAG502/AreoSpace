from pymavlink import mavutil

# master = mavutil.mavlink_connection('tcp:127.0.0.1:5763')
master = mavutil.mavlink_connection('/dev/tty.usbmodem01')
master.wait_heartbeat()
print('Got Heartbeat.\n')

master.mav.command_long_send(
    master.target_system,
    0,
    mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE,
    0,
    mavutil.mavlink.MAVLINK_MSG_ID_CAMERA_INFORMATION,
    0, 0, 0, 0, 0, 0
)

camera_values = master.recv_match(type='CAMERA_INFORMATION', blocking=True, timeout=1)

camera_caps = {
    1: "capture video",
    2: "capture image",
    4: "has modes",
    8: "can capture image in video mode",
    16: "can capture video in image mode",
    32: "has image survey mode",
    64: "has basic zoom",
    128: "has basic focus",
    256: "has video stream",
    512: "has tracking point",
    1024: "has tracking rectangle",
    2048: "has tracking geo status",
    4096: "has thermal range",
    8192: "has mti"
}

if camera_values:
    print(
        f'Name: {camera_values.vendor_name}\n'
        f'Model: {camera_values.model_name}\n'
        f'Resolution: {camera_values.resolution_h}x{camera_values.resolution_v}\n'
        f'Capabilities: {camera_caps[camera_values.flags]}\n'
        f'Camera definition URI: {camera_values.cam_definition_uri}'
    )

