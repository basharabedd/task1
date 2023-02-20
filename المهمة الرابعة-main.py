# Imports go at the top
from microbit import *
from ultrasonic import ultrasonic

ultra = ultrasonic()

while True:
    distance = ultrasonic_sensor.measure_distance_cm()
    display.scroll(str(int(distance)))
    if distance <= 10:
        pin2.write_digital(1)
    else:
        pin2.write_digital(0)
        

