from gpiozero import LED, Button
from time import sleep
from signal import pause

led = LED(23)
"""
while True:
    led.on()
    sleep(0.35)
    led.off()
    sleep(0.15)
"""
def say_hello():
    print("Hello!")

button = Button(24, pull_up=False)

button.when_pressed = say_hello

pause()
