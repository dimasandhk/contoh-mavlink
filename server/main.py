from dronekit import connect
import time

vehicle = connect("tcp:127.0.0.1:14550", wait_ready=True)
vehicle.wait_ready("autopilot_version")

def position_callback(self, attr_name, value):
  lat = value.lat
  lon = value.lon
  alt = value.alt
  
  print(f"Global Position (Relative to Home): ({lat}, {lon}, {alt})")

vehicle.add_message_listener("GPS_RAW_INT", position_callback)

time.sleep(20)
vehicle.close()