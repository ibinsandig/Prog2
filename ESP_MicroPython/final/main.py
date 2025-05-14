from machine import Pin
import time
import umqtt.simple as mqtt_client

MQTT_BROKER = "10.78.162.167"  # Your Pi Zero's IP address
MQTT_PORT = 1883
MQTT_TOPIC_PUB = b'watering/status'
MQTT_TOPIC_SUB = b'watering/control'

led_green = Pin(12, Pin.OUT)

def connect_mqtt():
    client = mqtt_client.MQTTClient("ESP8266", MQTT_BROKER, MQTT_PORT)
    try:
        client.connect()
        print("Connected to MQTT Broker")
        return client
    except Exception as e:
        print(f"Failed to connect to MQTT Broker: {e}")
        return None

# Connect to MQTT
client = connect_mqtt()
data = 0

# Signal successful connection
led_green.on()
time.sleep(1)
led_green.off()

while True:
    try:
        if client is None:
            client = connect_mqtt()
            time.sleep(1)
            continue
            
        # Convert data to bytes before publishing
        message = str(data).encode()
        client.publish(MQTT_TOPIC_PUB, message)
        print(f"Published: {data}")
        
        data += 2
        time.sleep(1)  # Add delay to avoid flooding the broker
        
    except Exception as e:
        print(f"Error in loop: {e}")
        client = None
        time.sleep(1)
