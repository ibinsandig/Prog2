def led_blink():
    for _ in range(3):
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)

led_blink()

for _ in range(3):
    transistor.on()
    time.sleep(10)
    transistor.off()
    time.sleep(3)

led_blink()
