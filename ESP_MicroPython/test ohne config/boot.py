import machine # type: ignore
import time

led_pin = machine.Pin(2, machine.Pin.OUT)

def blink_led():
    for i in range(3):
        led_pin.on()
        time.sleep(0.5)
        led_pin.off()
        time.sleep(0.5)
        
blink_led()