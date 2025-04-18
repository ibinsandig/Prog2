import machine # type: ignore
import time


class WaterPump:
    def __init__(self, pin):
        self.pump = machine.Pin(pin, machine.Pin.Out)

    def start(self):
        self.pump.on()

    def stop(self):
        self.pump.off()

    def startstop(self, time):
        self.start()
        time.delay(time)
        self.stop()


pump = WaterPump(5)

pump.startstop(6)

class feuchtigkeitsensor:
    def __init__(self, pin):
        self.sensor = machine.Pin(pin, machine.Pin.In)
    
    def messung(self):
        analogValue = machine.Pin(pin,) 