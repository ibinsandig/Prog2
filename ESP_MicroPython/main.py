import config.py

def led_blink():
    for _ in range(3):
        led.on()    # type: ignore
        time.sleep(0.5) # type: ignore
        led.off() # type: ignore
        time.sleep(0.5) # type: ignore
        
def transistor_test():
    for _ in range(3):
        transistor.on() # type: ignore
        time.sleep(10) # type: ignore
        transistor.off() # type: ignore
        time.sleep(3) # type: ignore

def test_feuchtigkeit():
    while True:
        if digital_value ==0
            led.off() # type: ignore
        else:
            led.on()

test_feuchtigkeit()