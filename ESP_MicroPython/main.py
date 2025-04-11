import config
import time
# def led_blink():
#     for _ in range(3):
#         led.on()    # type: ignore
#         time.sleep(0.5) # type: ignore
#         led.off() # type: ignore
#         time.sleep(0.5) # type: ignore
        
# def transistor_test(i):
#     for _ in range(i):
#         config.transistor.on() # type: ignore
#         time.sleep(10) # type: ignore
#         config.transistor.off() # type: ignore
#         time.sleep(3) # type: ignore

def test_feuchtigkeit():
    while True:
        if config.digital_value == 0:
            config.led.off() 
        else:
            config.led.on()


# transistor_test(3)


test_feuchtigkeit()