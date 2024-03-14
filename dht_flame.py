import dht
import machine

dht_pin = 26
sensor = dht.DHT11(machine.Pin(dht_pin))  #assuming connected to GPIO 26

flame_sensor_pin = 14  #example GPIO pin, adjust based on your connection
flame_sensor = machine.Pin(flame_sensor_pin, machine.Pin.IN)

def read_dht():
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        return temperature, humidity # (temp, humid)
    except:
        return 0, 0
   
def read_flame():
    flame_detected = flame_sensor.value()
    return not flame_detected # so as to invert the sensor data since it is active low