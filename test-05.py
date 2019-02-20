from gpiozero import Servo
from time import sleep

servo1 = Servo(17, min_pulse_width=0.55/1000, max_pulse_width=2.60/1000, frame_width=25/1000)
while True:
    seovo1.min()
    sleep(1)
    seovo1.mid()
    sleep(1)
    seovo1.max()
    sleep(1)
