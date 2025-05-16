import machine # type: ignore
import time
import network # type: ignore
import socket

# WLAN-Station-Modus aktivieren
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Mit WLAN verbinden
print("Verbinde mit WLAN...")
ssid = "WehLan"
password = "1234wlan5678"

# ssid = "Lochbox"
# password = ""

# Warten, bis die Verbindung hergestellt ist
while not wlan.isconnected():
    pass
    print(".")
    time.sleep(0.5)

print("Verbunden! IP-Adresse:", wlan.ifconfig()[0])

