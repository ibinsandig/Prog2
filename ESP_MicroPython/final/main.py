from machine import Pin, ADC #typing: ignore
from umqtt.simple import MQTTClient #typing: ignore
import time
# Konfiguration
MQTT_BROKER = "10.87.223.167"
#zero:
#"10.78.162.167"
# neu: 10.87.223.167  

#RPi4:
#"192.168.178.21" 
#"10.78.162.224"
MQTT_PORT = 1883
MQTT_TOPIC_PUB = b'watering/status'
MQTT_TOPIC_PUB2 = b'watering/pump_status'
MQTT_TOPIC_PUB3 = b'watering/status2'
MQTT_TOPIC_SUB = b'watering/control'


# Hardware
led_green = Pin(12, Pin.OUT)
led_green.off()

sensor_analog = ADC(0)
sensor_digital = Pin(4, Pin.IN)

pump = Pin(5, Pin.OUT) 

# Globale Variablen

#data_analog = sensor_analog.read()
#data_digital = sensor_digital.value()

status_pump = 0

trigger = 300

pump_time = 3

pump_time_stop = 3


def senden(zu_verwendende_topic, data):
    global client
    
    if client:
        status = {
            "digital": data
            #"pump": status_pump
        }
    status_msg = str(status).encode()
        
    try:
        client.publish(zu_verwendende_topic, status_msg)
        print(f"Nachricht gesendet: {status_msg}")
    except Exception as e:
        print(f"Fehler beim Senden der Nachricht: {e}")

# Callback-Funktion für empfangene Nachrichten

def empfangen(topic, msg):
    global status_pump
    
    print(f"Nachricht empfangen:")
    topic = topic.decode()
    print(f"Topic: {topic}")
    message = msg.decode()
    print(f"Nachricht: {message}")

    if message == "on":
        status_pump = 1
        led_green.on()
        print("Pumpe eingeschaltet")
    elif message == "off":
        status_pump = 0
        led_green.off()
        print("Pumpe ausgeschaltet")


# MQTT-Verbindung
def connect_mqtt():
    try:
        client = MQTTClient("ESP8266", MQTT_BROKER, port=MQTT_PORT)
        client.set_callback (empfangen)
        client.connect()
        client.subscribe(MQTT_TOPIC_SUB)
        print("MQTT verbunden")
        return client
    except Exception as e:
        print(f"MQTT-Verbindung fehlgeschlagen: {e}")
        return None


client = connect_mqtt()



def run_watering():
    global client
    while True:
        try:
            if client:
                client.check_msg()  # Prüfe auf neue MQTT-Nachrichten
            else:
                # Versuche Neuverbindung
                try:
                    client = connect_mqtt()
                except:
                    pass
                    
            time.sleep(5) # Warte 5 Sekunden zwischen den Status-Updates
        


        except Exception as e:
            print('Fehler in Hauptschleife:', e)
            time.sleep(5)
            client = None
    
        if sensor_digital.value() == 1 or status_pump == 1:
            senden(MQTT_TOPIC_PUB2, 1)
            senden(MQTT_TOPIC_PUB, sensor_digital.value())
            print(f"Pumpe an für {pump_time} sek")
            led_green.on()
            data_digital = 1
            pump.on()
            time.sleep(pump_time)  # Sleep nach pump.on() eingefügt
            
        
        elif sensor_digital.value() == 0 and status_pump == 0:
            senden(MQTT_TOPIC_PUB2, 0)
            senden(MQTT_TOPIC_PUB, sensor_digital.value())
            pump.off()
            print(f"Pumpe aus für {pump_time_stop} sek")
            led_green.off()
            data_digital = 0
        time.sleep(pump_time_stop)

run_watering()