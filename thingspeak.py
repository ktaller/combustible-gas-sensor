import urequests as requests
from credentials import api_key, channel_id


def send_to_thingspeak(field1, field2, field3,field4):
    try:
        url = "https://api.thingspeak.com/update?api_key={}&field1={}&field2={}&field3={},&field4={}".format(api_key, field1, field2, field3, field4)
        response = requests.post(url)
        print("ThingSpeak Response:", response.text)
    except:
        pass
