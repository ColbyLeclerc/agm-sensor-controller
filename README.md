# Setting up the sensor controller
## Overview
The sensor controller uses the DHT 22 temperature-humidity sensor attached to a Raspberry Pi B+. When referring to the sensor controller, this will be with regards to the Raspberry Pi B+ board. The sensor controller has an HDMI port, and USB ports for use with a display, and mouse/keyboard devices respectively. The USB port with a green PCB sticking out is the WiFi module to allow for remote connection. 

The sensor controller requires a micro-USB connection to power the device. Note using a standard wall adapter with the USB cord will produce a startup message saying `undervoltage detected`. Typically, the CPU will be throttled in an undervoltage state. This is okay for our purposes. When the device is plugged in, its setup such that readings will begin being read, and requests will be attempted to be sent to `198.199.89.150`. Due to the device not being configured with the local WiFi network, the requests will not reach the server. You can either connect an ethernet cord to the sensor controller, or use an HDMI cable with a display, mouse, and keyboard, to configure the WiFi connection.

Most wire connections were soldered together, however the connection between the sensor and the sensor controller uses pins that may fall out during transit. In the event this occurs, see the 'Pin Placement' 

## Setting up the WiFi connection

First, you'll be brought to a desktop that looks like the image below. Marked in a red box is the WiFi icon used to configure a connection.

![WiFi Setup Step 1](/images/wifi-step1.jpeg "WiFi Setup Step 1")

Next, select the connection you'd like to connect to, then enter the password (if applicable)

![WiFi Setup Step 2](/images/wifi-step2.jpeg "WiFi Setup Step 2")

## Pin placement

Below is a schematic detailing the pin placement (from https://rototron.info/dht22-tutorial-for-raspberry-pi )
(Note: the DHT-22 sensor model I have does not contain the `No Connection` pin as shown in the image below)

![DHT22 Sensor Schematic](/images/DHT22-schematic.jpg "DHT22 Sensor Schematic")

Marked on each wire is a piece of tape that matches the wire to the schematic. Below is an image with the wires connected
(NOTE: The DHT22 shcematic shows the ground (`GND`) pin below the data pin, while the image below shows the ground pin on the left-most pin. Either way works, as there exists multiple ground pins on the board. I chose the leftmost pin because it was easier to show, and less 'congested' with the non-soldered pin contacts)

![Sensor Controller Pin Setup](/images/sensor-controller-pin.jpeg "Sensor Controller Pin Setup")

## Authorization

When creating a new instance, a new authentication token must be generated, then added to the sensor controller script. The file to modify is on the desktop, and is seen when starting the controller, named `autoRunCollection.py`. Open the file and modify the `sensor_id` variable, and the `auth` variable. See 'Example `auth` Generation' section on how to generate the auth token. See `Example 'sensor_id' Generation' section on how to generate a sensor id. 

### Example `auth` Generation

Here's an example on how to generate a new auth token for use with the sensor controller (and all other requests associated with the account). Note the server seen in the example will be left running, thus you can use this server for setup.

Note, the following headers are required when making a request:

```
Authorization: TEST
Content-Type: application/json
```

![Auth Example](/images/auth-example.png "Auth Example")


After the request is made, use the value present in the `token` field to update the `auth` variable in the `autoRunCollection.py` file

### Example `sensor_id` Generation

Here's an example on how to create a sensor to recieve a `sensor-id` from the API server for use as the `sensor_id` variable in the `autoRunCollection.py` file

Note, the following headers are required when making a request. (If you decide to generate a new auth token, replace the auth token below with the newly generated one, under the `Authorization` header):

```
Authorization: 3680061c-79e4-4161-a4cb-773c7a2b1001
Content-Type: application/json
```

![Sensor ID Example](/images/sensor-id-example.png "Sensor ID Example")

## Auto Run
In the `crontab` file found in this repo, you'll find the crontab entry I made to have the script start during reboot. Thus, once configured, a display will not be needed, and no action on the user is required. To verify the readings are being `POSTED`, check the `temperature-humidity` endpoint for recent readings, using the same authentication token used for the sensor controller.