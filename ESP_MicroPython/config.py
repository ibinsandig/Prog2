from machine import Pin, ADC # type: ignore

# Pin zur Aktivierung der Pumpe durch TRansistor
transistor = Pin(5, Pin.OUT) # type : ignore
transistor.off()

# Pin für den digitalen EIngang des Feuchtigkeitssensors
feuchtigkeitDigital = Pin(4, Pin.IN) # type : ignore
digital_value = feuchtigkeitDigital.value()

# Pin für den analogen Eingang des Feuchtigkeitssensors
feuchtigkeitAnalog = ADC(0)
analog_value = feuchtigkeitAnalog.read()

# Boot LED
led = Pin(2, Pin.OUT) # type : ignore
led.off()
