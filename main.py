import mike
import ConnectWifi
from time import sleep
from dht_flame import read_dht, read_flame

# mike.blink(1)
print ("run : main.py")
ConnectWifi.connect()

while True:
    try:
        dht_data = read_dht()
        temperature = dht_data[0]
        humidity = dht_data[1]
        flame = read_flame()
        
        print("Temperature: {}°C, Humidity: {}%, Flame: {}".format(temperature, humidity, "DETECTED" if flame else "ABSENT"))
#         print("Temperature: ", temperature, Humidity: {}%, Flame: {}", , humidity, flame_detected ? "AB" : "PR")
    except Exception as e:
            print("Error reading DHT sensor:", e)

    sleep(.5)  # Read every 1/2 seconds
    


# while True:
#     flame_detected = flame_sensor.value()  # Read digital signal
#     if flame_detected:
#         print("Flame detected!")
#     else:
#         print("No flame detected")
# 
#     time.sleep(2)  # Adjust the delay as needed