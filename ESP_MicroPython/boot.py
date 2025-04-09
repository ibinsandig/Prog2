import machine as mech
import time

# Pin zur Aktivierung der Pumpe durch TRansistor
transistor = mech.Pin(5, mech.Pin.OUT) # type : ignore
transistor.off()

# Pin für den digitalen EIngang des Feuchtigkeitssensors
feuchtigkeitDigital = mech.Pin(4, mech.Pin.IN) # type : ignore
digital_value = feuchtigkeitDigital.value()

# Pin für den analogen Eingang des Feuchtigkeitssensors
feuchtigkeitAnalog = mech.ADC(0)
analog_value = feuchtigkeitAnalog.read()

# Boot LED
bootled = mech.Pin(2, mech.Pin.OUT) # type : ignore
bootled.off()

# Blinksignal beendigung des Bootvorgangs
for _ in range(10):
    bootled.on()
    time.sleep(0.2)
    bootled.off()
    time.sleep(0.2)

bootled.on()
