import machine
import time
from dht_flame import read_dht, read_flame
from mq5_sensor import read_mq5
from thingspeak import send_to_thingspeak
from buzzer import toggle_buzz
import ConnectWifi

ConnectWifi.connect()
print("run: main.py")

mq5_pin = 33  # Example pin number, adjust based on your connection
adc = machine.ADC(machine.Pin(mq5_pin))

buzzer = machine.Pin(13, machine.Pin.OUT)
buzz_time = 0
upload_time = 0

while True:
    dht_temperature, dht_humidity = read_dht()
    flame_detected = read_flame()
    mq5_value = read_mq5(adc)

    print("Sensor Data - DHT: Temperature = {}°C, Humidity = {}%, Flame Detected = {}, MQ-5 Sensor Value: {}".format(
        dht_temperature, dht_humidity, flame_detected, mq5_value
    ))
    
    if dht_temperature == 0 and dht_humidity == 0:
        continue
    if mq5_value >= 50000 and time.time() - buzz_time >= 1:
#         toggle_buzz(buzzer)
        buzz_time = time.time()
        print("buzzer: ", buzzer.value(), buzz_time)
    else:
        buzzer.off()
    
    if time.time() - upload_time >= 2:
        send_to_thingspeak(mq5_value, dht_temperature, dht_humidity, flame_detected)
