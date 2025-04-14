from machine import Pin, ADC # type: ignore
import time
# Pin zur Aktivierung der Pumpe durch TRansistor
transistor = Pin(5, Pin.OUT)
transistor.off()

# Pin für den digitalen EIngang des Feuchtigkeitssensors
feuchtigkeitDigital = Pin(4, Pin.IN) 
digital_value = feuchtigkeitDigital.value()

# Pin für den analogen Eingang des Feuchtigkeitssensors
feuchtigkeitAnalog = ADC(0)
analog_value = feuchtigkeitAnalog.read()

# Boot LED
led = Pin(2, Pin.OUT) 