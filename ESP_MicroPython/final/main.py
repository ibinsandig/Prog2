from machine import Pin, ADC
import uasyncio as asyncio
import umqtt.simple as mqtt_client
import time
# Konfiguration
MQTT_BROKER = "10.78.162.167"
MQTT_PORT = 1883
MQTT_TOPIC_PUB = b'watering/status'
MQTT_TOPIC_SUB = b'watering/control'

# Hardware
led_green = Pin(12, Pin.OUT)
led_green.off()

sensor_analog = ADC(0)
sensor_digital = Pin(4, Pin.IN)

pump = Pin(5, Pin.OUT) 

# Globale Variablen

data_analog = 0
data_digital = 0

status_pump = 0

trigger = 300

pump_time = 3

pump_time_stop = 3

# MQTT-Verbindung
def connect_mqtt():
    try:
        client = mqtt_client.MQTTClient("ESP8266", MQTT_BROKER, MQTT_PORT)
        client.connect()
        print("MQTT verbunden")
        return client
    except Exception as e:
        print(f"MQTT-Verbindung fehlgeschlagen: {e}")
        return None

client = connect_mqtt()

# blink LED
async def blink_led(time):
    while time > 0:
        led_green.on()
        await asyncio.sleep(0.3)
        led_green.off()
        await asyncio.sleep(0.3)
        time -= 1

#read sensor
async def read_sensor():
    global data_analog
    global data_digital
    while True:
        data_analog = sensor_analog.read()
        data_digital = sensor_digital.value()
        print(f"Sensorwert analog: {data_analog}, Sensorwert digital: {data_digital}")
        await asyncio.sleep(0.9)
        
# pump steuern
async def control_pump(state, pump_time):
    global pump
    while True:
        if state == 1:
            pump.on()
            print("Starte Pumpzyklus")
            await blink_led(pump_time)
            await asyncio.sleep(pump_time)
            pump.off()
            print("Stoppe Pumpzyklus")
        else:
            await asyncio.sleep(pump_time_stop)

# check sensor_digital
async def check_sensor_digital():
    global status_pump  
    while True:
        if data_digital == 1:
            print("Sensorwert digital: 1")
            status_pump = 1
        else:
            print("Sensorwert digital: 0")
            status_pump = 0  
        await asyncio.sleep(1)

# check sensor_analog
async def check_sensor_analog():
    global status_pump
    while True:
        if data_analog < trigger:
            print("Sensorwert analog: {trigger}")
            status_pump = 1
        else:
            print("Sensorwert analog: {trigger}")
            status_pump = 0
        
        await asyncio.sleep(1)
        
# Aufgabe: MQTT-Publish alle 5 Sek
async def publish_data():
    global client
    while True:
        try:
            if client is None:
                client = connect_mqtt()
            if client:
                message = str(data_analog).encode()
                client.publish(MQTT_TOPIC_PUB, message)
                print(f"MQTT gesendet: {data_analog}")
        except Exception as e:
            print(f"MQTT-Fehler: {e}")
            client = None
        await asyncio.sleep(5)

# Hauptfunktion
async def main():
    asyncio.create_task(read_sensor())
    asyncio.create_task(check_sensor_digital())
    pump_control = asyncio.create_task(control_pump(status_pump, pump_time))
    while True:
        # Aktualisiere pump_control mit aktuellem status_pump
        if pump_control.done():
            pump_control = asyncio.create_task(control_pump(status_pump, pump_time))
        await asyncio.sleep(1)

# Starte die Event-Loop
asyncio.run(main())  # Hier startet der Event-Loop