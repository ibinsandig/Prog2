import config
import time
def led_blink():
    for _ in range(3):
        config.led.on()    
        time.sleep(0.5) 
        config.led.off() 
        time.sleep(0.5) 
        
def transistor_test(i):
    for _ in range(i):
        config.transistor.on() 
        time.sleep(10) 
        config.transistor.off() 
        time.sleep(3) 

def test_feuchtigkeit():
    while count:
        if config.digital_value == 0:
            config.led_test.off() 
            print("feucht")
        else:
            config.led_test.on()
            print("trocken")
        count += 1
        


# transistor_test(3)


test_feuchtigkeit()