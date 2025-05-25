import machine # type: ignore
import time
import network # type: ignore
import socket

# Wlan aktivieren 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)


print("Verbinde mit WLAN...")
ssid = "Lochbox"
password = "280874b61133"

# Wlan verbinden
wlan.connect(ssid, password)

# versucht es x mal
max_wait = 10
while max_wait > 0:
    if wlan.isconnected():
        break
    max_wait -= 1
    print("Verbindungsversuch...")
    time.sleep(1)

if wlan.isconnected():
    print("Verbunden! IP-Adresse:", wlan.ifconfig()[0])
else:
    print("Verbindung fehlgeschlagen!")
    print("Status:", wlan.status())