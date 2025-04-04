import machine
import time

led = machine.Pin(2, machine.Pin.OUT)  # GPIO2 ist oft mit der eingebauten LED verbunden

while True:
    led.value(1)  # LED einschalten
    time.sleep(1)  # 1 Sekunde warten
    led.value(0)  # LED ausschalten
    time.sleep(1)  # 1 Sekunde warten