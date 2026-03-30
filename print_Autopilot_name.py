from pymavlink import mavutil


master = mavutil.mavlink_connection('tcp:127.0.0.1:5763')

#print(master.wait_heartbeat())

autopilot_value = master.messages['HEARTBEAT'].autopilot

autopilots = {
    0: "GENERIC",
    1: "RESERVED",
    2: "SLUGS",
    3: "ARDUPILOTMEGA",
    4: "OPENPILOT",
    5: "GENERIC_WAYPOINTS_ONLY",
    6: "GENERIC_WAYPOINTS_AND_SIMPLE_NAVIGATION_ONLY",
    7: "GENERIC_MISSION_FULL",
    8: "INVALID",
    9: "PPZ",
    10: "UDB",
    11: "FP",
    12: "PX4",
    13: "SMACCMPILOT",
    14: "AUTOQUAD",
    15: "ARMAZILA",
    16: "AEROB",
    17: "ASLUAV",
    18: "SMARTAP",
    19: "AIRRAILS",
    20: "REFLEX"
}

print("Autopilot Name:", autopilots[autopilot_value])