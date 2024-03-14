    
# Create an ADC object

def read_mq5(adc):
    mq5_value = adc.read_u16()

    print("MQ-5 Sensor Value:", mq5_value)
    
    return mq5_value

