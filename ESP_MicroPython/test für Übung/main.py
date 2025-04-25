from machine import Pin
import time

led_green = Pin(12, Pin.OUT)

led_green.on()
time.sleep(10)
led_green.off()