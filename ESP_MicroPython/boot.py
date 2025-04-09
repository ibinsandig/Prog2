from machine import Pin # type: ignore
import time

transistor = Pin(5, Pin.OUT)
transistor.off()

led = Pin(2, Pin.OUT)
led.off()

# Blinksignal zur Anzeige des Bootens
for _ in range(10):
    led.on()
    time.sleep(0.2)
    led.off()
    time.sleep(0.2)
