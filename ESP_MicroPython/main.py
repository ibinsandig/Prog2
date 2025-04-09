def led_blink():
    for _ in range(3):
        bootled.on()    # type : ignore
        time.sleep(0.5) # type : ignore
        bootled.off() # type : ignore
        time.sleep(0.5) # type : ignore

led_blink()

for _ in range(3):
    transistor.on() # type : ignore
    time.sleep(10) # type : ignore
    transistor.off() # type : ignore
    time.sleep(3) # type : ignore

led_blink()