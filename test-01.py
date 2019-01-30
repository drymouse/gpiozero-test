from gpiozero import LED, Button
from time import sleep
from signal import pause

led = LED(23)

while True:
    led.on()
    sleep(0.35)
    led.off()
    sleep(0.15)
