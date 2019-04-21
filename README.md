# Setting up the sensor controller
## Overview
The sensor controller uses the DHT 22 temperature-humidity sensor attached to a Raspberry Pi B+. When referring to the sensor controller, this will be with regards to the Raspberry Pi B+ board. The sensor controller has an HDMI port, and USB ports for use with a display, and mouse/keyboard devices respectively. The USB port with a green PCB sticking out is the WiFi module to allow for remote connection. 

The sensor controller requires a micro-USB connection to power the device. Note using a standard wall adapter with the USB cord will produce a startup message saying `undervoltage detected`. Typically, the CPU will be throttled in an undervoltage state. This is okay for our purposes. When the device is plugged in, its setup such that readings will begin being read, and requests will be attempted to be sent to `198.199.89.150`. Due to the device not being configured with the local WiFi network, the requests will not reach the server. You can either connect an ethernet cord to the sensor controller, or use an HDMI cable with a display, mouse, and keyboard, to configure the WiFi connection.

Most wire connections were soldered together, however the connection between the sensor and the sensor controller uses pins that may fall out during transit. In the event this occurs, see the 'Pin Placement' 

## Setting up the WiFi connectin

## Pin placement
