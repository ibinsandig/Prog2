import machine # type: ignore
import time
import network
import socket

# WLAN-Station-Modus aktivieren
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Mit WLAN verbinden
ssid = "WLAN"
password = "penispenis"
wlan.connect(ssid, password)

# Warten, bis die Verbindung hergestellt ist
while not wlan.isconnected():
    pass
    print(".")

print("Verbunden! IP-Adresse:", wlan.ifconfig()[0])
