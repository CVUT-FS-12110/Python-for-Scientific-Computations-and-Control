import time
import esp32
import urequests as requests

adress = '192.168.0.200'
port = '10070'
host = f"http://{adress}:{port}"


def post_data(data):
    path = "/sensor/data"
    r = requests.post(url=host+path, json=data)
    print(f"{r.status_code} -> Message: {r.json()['message']}")

r = requests.get(url=host)
print(f"{r.status_code} -> Message: {r.json()['message']}")

while True:
    temperature = esp32.raw_temperature()
    data = {
        "name": "ESP1",
        "temperature": (temperature - 32)/1.8,
    }
    post_data(data)
    
    time.sleep(4)