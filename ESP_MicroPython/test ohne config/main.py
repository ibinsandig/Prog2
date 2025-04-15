from machine import Pin, ADC # type: ignore
import time

# Pin zur Aktivierung der Pumpe durch Transistor
transistor = Pin(5, Pin.OUT)
transistor.off()

# Pin für den digitalen Eingang des Feuchtigkeitssensors
feuchtigkeitDigital = Pin(4, Pin.IN) 
digital_value = feuchtigkeitDigital.value()

# Pin für den analogen Eingang des Feuchtigkeitssensors
feuchtigkeitAnalog = ADC(0)
analog_value = feuchtigkeitAnalog.read()

# LED
led = Pin(2, Pin.OUT)
led_green = Pin(12, Pin.OUT)

def led_blink_green():
    for _ in range(6):
        led_green.on()    
        time.sleep(0.2) 
        led_green.off() 
        time.sleep(0.2) 
        
def transistor_test(i):
    for _ in range(i):
        transistor.on() 
        time.sleep(3) 
        transistor.off() 
        time.sleep(1) 

def test_feuchtigkeit():
    count = 0
    while count < 10:
        if digital_value == 0:
            led.off() 
            print("feucht")
            print("digital_value: ", digital_value)
        else:
            led.on()
            print("trocken")
            print("digital_value: ", digital_value)
        count += 1
        time.sleep(1)

led_blink_green()

transistor_test(3)

led_blink_green()	

test_feuchtigkeit()

led_blink_green()