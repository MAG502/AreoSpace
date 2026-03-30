from pymavlink import mavutil
import time

master = mavutil.mavlink_connection('udp:127.0.0.1:14550')
# master = mavutil.mavlink_connection('/dev/tty.usbmodem01')

master.wait_heartbeat()

end_time = time.time() + 10
seen = {}
number_of_sensors = 0
while time.time() < end_time:
    msg = master.recv_match(blocking=True, timeout=1)
    
    if msg:
        msg_type = msg.get_type()
        
        if msg_type in ['SCALED_PRESSURE', 'SCALED_PRESSURE2', 'SCALED_PRESSURE3'] and msg_type not in seen:
            print(f'Sensor {msg_type.replace("SCALED_","")} dedicated')
            seen[msg_type] = True
            number_of_sensors += 1
print(number_of_sensors, 'Sensors Dedicated' if number_of_sensors > 1 else 'Sensor Dedicated')