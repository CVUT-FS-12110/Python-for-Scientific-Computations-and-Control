import time
import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('micropython_lecture', 'Abcde12345')
    atempts = 10
    while not wlan.isconnected() and atempts:
        atempts -= 1
        print(f"Retrying to connect. Atempts remaining: {atempts}")
        time.sleep(1)
print('network config:', wlan.ifconfig())

import webrepl
webrepl.start()