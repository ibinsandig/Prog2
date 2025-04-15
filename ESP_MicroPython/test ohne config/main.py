from machine import Pin, ADC  # type: ignore
import time
import socket

# Pins für Sensor und Pumpe
transistor = Pin(5, Pin.OUT) 
transistor.off()

feuchtigkeitDigital = Pin(4, Pin.IN)
feuchtigkeitAnalog = ADC(0)

led = Pin(2, Pin.OUT)
led_green = Pin(12, Pin.OUT)

# Blinkende LED-Funktion
def led_blink_green():
    for _ in range(6):
        led_green.on()
        time.sleep(0.2)
        led_green.off()
        time.sleep(0.2)

# Transistor-Test
def transistor_test(i):
    for _ in range(i):
        transistor.on()
        time.sleep(3)
        transistor.off()
        time.sleep(1)

# Feuchtigkeitssensor-Test
def test_feuchtigkeit():
    count = 0
    while count < 10:
        digital_value = feuchtigkeitDigital.value()
        if digital_value == 0:
            led.off()
            print("feucht")
        else:
            led.on()
            print("trocken")

        print("digital_value:", digital_value)
        count += 1
        time.sleep(1)

# Webserver starten
def webserver():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(5)
    print('Webserver läuft...')

    while True:
        conn, addr = s.accept()
        print('Verbindung von', addr)

        feuchtigkeit = feuchtigkeitAnalog.read()
        pumpe_status = "AN" if transistor.value() else "AUS"

        html = f"""<!DOCTYPE html>
        <html>
            <head>
                <title>Feuchtigkeitssensor</title>
                <meta charset="utf-8">
                <meta http-equiv="refresh" content="2">
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        margin: 20px;
                        background-color: #f0f0f0;
                    }}
                    h1 {{
                        color: #333;
                        margin-bottom: 15px;
                    }}
                </style>
            </head>
            <body>
                <h1>Feuchtigkeitswert: {feuchtigkeit}</h1>
                <h1>Pumpe Status: {pumpe_status}</h1>
            </body>
        </html>"""

        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n\n')
        conn.send(html)
        conn.close()

# Abläufe starten
led_blink_green()
transistor_test(3)
led_blink_green()
test_feuchtigkeit()
led_blink_green()

# Webserver starten
webserver()