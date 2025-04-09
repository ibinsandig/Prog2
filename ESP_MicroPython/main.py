def led_blink():
    for _ in range(3):
        bootled.on()    # type : ignore
        time.sleep(0.5) # type : ignore
        bootled.off() # type : ignore
        time.sleep(0.5) # type : ignore
        
def transistor_test():
    for _ in range(3):
        transistor.on() # type : ignore
        time.sleep(10) # type : ignore
        transistor.off() # type : ignore
        time.sleep(3) # type : ignore

def test_feuchtigkeit(anzahl):
    while anzahl > 10:
        Serial.print("Digital: ", digital_value) # type : ignore
        Serial.print("Analog: ", analog_value) # type : ignore
        time.sleep(1)
        anzahl += 1



test_feuchtigkeit(10)

