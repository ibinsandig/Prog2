import time
from machine import Pin

# Reuse the transistor pin configured in boot.py
transistor = Pin(5, Pin.OUT)

# Function to control the transistor
def control_transistor(state):
    if state:
        transistor.on()  # Turn the transistor on
    else:
        transistor.off()  # Turn the transistor off

def led_blink():
    count = 0
    while count < 10:  # Blink 10 times
        led.on()  # Turn the LED on
        time.sleep(1)  # Wait 1 second
        led.off()  # Turn the LED off
        time.sleep(1)  # Wait 1 second
        count += 1

# Example usage: Blink the transistor
while True:
    control_transistor(True)  # Turn on
    time.sleep(3)             # Wait 3 second
    control_transistor(False) # Turn off
    time.sleep(3)             # Wait 3 second


# BLink after transistor
led_blink()