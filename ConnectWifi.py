from time import sleep
import network
from credentials import WIFI_SSID, WIFI_PASSWORD 

def connect():    
    station = network.WLAN(network.STA_IF)
    
    if station.isconnected():
        print("already connected")
        return
    
    station.active(True)
    station.connect(WIFI_SSID, WIFI_PASSWORD)
    
    print("Connecting", end="")
    while not station.isconnected():
        print(".", end="")
        sleep(.2)
    else:
        print()
    
    print("Connection successful")
    print(station.ifconfig())