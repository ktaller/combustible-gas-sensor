from time import sleep
import network
import credentials

def connect():
    ssid = credentials.WIFI_SSID
    password = credentials.WIFI_PASSWORD
    
    station = network.WLAN(network.STA_IF)
    
    if station.isconnected():
        print("already connected")
        return
    
    station.active(True)
    station.connect(ssid, password)
    
    print("Connecting", end="")
    while not station.isconnected():
        print(".", end="")
        sleep(.2)
    else:
        print()
    
    print("Connection successful")
    print(station.ifconfig())