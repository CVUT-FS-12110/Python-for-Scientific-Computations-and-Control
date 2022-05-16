
# Preparation

## Arduino IDE
* Download portable (or install) [Arduino IDE](https://www.arduino.cc/en/software)
* Connect ESP with USB to the PC
* Open Arduino IDE -> tools -> Serial monitor with correct port (you have to find it with Arduino IDE -> Tools -> Port and try with serial monitor)

## esptool
* Create venv with `python -m venv venv`
* Open venv (`venv\Scripts\activate` on Win) 
* Install esptool with `pip install esptool`
* erase board: `python -m esptool --chip esp32 --port <PORT_OF_YOUR_BOARD> erase_flash` (you need to close Serial monitor for that to free the com port)
    * after running the command push the button **BOOT** on the board
* Get firmware for your board from: https://micropython.org/download/ (we use the one from lecture repository on github)
* flash the board: `python -m esptool --chip esp32 --port <PORT_OF_YOUR_BOARD> --baud 460800 write_flash -z 0x1000 esp32-20220117-v1.18.bin`
    * instead of `esp32-20220117-v1.18.bin` use the path to the firmware bin you have downloaded


# Micropythoning
## first time connection
* Open Arduino IDE Serial monitor again
* Restart the board with **EN** button
* You should se logs in serial monitor
* First we will import module network from the monitor console `import network`
* `wlan = network.WLAN(network.STA_IF)` # create station interface
* `wlan.active(True)`       # activate the interface
* `wlan.scan()`             # scan for access points
* `wlan.connect('micropython_lecture', 'Abcde12345')` # connect to an AP
* `wlan.isconnected()`      # check if the station is connected to an AP

## webrepl
* Webrepl is tool for acessing the board, loading and unloading code and basic debugging
* Download [Webrepl](https://github.com/micropython/webrepl) or grab it from lecture files
* Open the folder with webrepl and launch it with `webrepl.html`
* Back to serial monitor setup webrepl on board: `import webrepl_setup` -> with options (E)nable, pass, pass, n
* Next `import webrepl` and start it: `webrepl.start()`
* In the log of serial monitor look for `WebREPL daemon started on ws://192.168.0.88:8266` and grab the address from there
* Use the address from serial monitor in Webrepl console to connect to device
* Fill in password after the webrepl asks you for it and you should be in

## Boot script
* After reboot of the board the `boot.py` script is loaded first
* There we should specify basic setup of the board (wifi connection, webrepl setup) so we don't have to do it each time
* Prepare your `boot.py` or use the one from [lecture files](https://github.com/CVUT-FS-12110/Python/blob/master/courses/E375004/micropython_smart_sensor/04_scripts_for_board/boot.py)
* Load the `boot.py` with Webrepl: Choose file -> Send to device
* Reboot the board, in the serial monitor you should se the connection and webrepl launch

## Main script
* After the `boot.py` is executed the `main.py` is then loaded
* In `main.py` our code for program should be placed (we can also include other scripts but main is starting point)
* For the lecture purposes we will make program for reading of temperature sensor on the board and providing the data to server API via local WIFI site
   * prepared `main.py` is in  [lecture files](https://github.com/CVUT-FS-12110/Python/blob/master/courses/E375004/micropython_smart_sensor/04_scripts_for_board/main.py) 
