import time
import requests

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
    #stemperature = esp32.raw_temperature()
    data = {
        "name": "Martin",
        "temperature": 22,
    }
    post_data(data)
    
    time.sleep(4)