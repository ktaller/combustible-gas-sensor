import dht
import machine
import time

sensor = dht.DHT11(machine.Pin(26))  # Assuming connected to GPIO 26

flame_sensor_pin = 14  # Example GPIO pin, adjust based on your connection
flame_sensor = machine.Pin(flame_sensor_pin, machine.Pin.IN)

def read_dht():
    sensor.measure()
    temperature = sensor.temperature()
    humidity = sensor.humidity()
    return temperature, humidity # (temp, humid)
   
def read_flame():
    flame_detected = flame_sensor.value()
    return not flame_detected # invert the sensor data since it is active low