from machine import Pin, ADC #typing: ignore
import umqtt.simple as mqtt_client #typing: ignore
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

#data_analog = 0
#data_digital = 0

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

def run_watering():
    while True:
        if sensor_digital.value() == 1 or status_pump == 1:  # '|' durch 'or' ersetzt
            print(f"Pumpe an für {pump_time} sek")  # String-Formatierung korrigiert
            pump.on()
            time.sleep(pump_time)  # Sleep nach pump.on() eingefügt
        
        elif sensor_digital.value() == 0 and status_pump == 0:  # '&' durch 'and' ersetzt
            pump.off()
        
        time.sleep(pump_time_stop)  # Einrückung korrigiert, else: entfernt