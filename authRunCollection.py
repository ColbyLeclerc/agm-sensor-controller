import sched
import time

import Adafruit_DHT
import json
import requests

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT22
sensor_id = 21
auth = '3680061c-79e4-4161-a4cb-773c7a2b1001'
# Example using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
#pin = 'P8_11'

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
pin = 4

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
#humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!


def sendReqForSensorData(sc):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        data = {"sensor-id": sensor_id, "temp-level": round(
            temperature, 2), "humidity-units": "percent", "humidity": round(humidity, 2), "temp-scale": "c"}
        data_json = json.dumps(data)
        headers = {'Content-type': 'application/json',
                   'Authorization': auth}
        print(data_json)
        response = requests.post(
            'http://198.199.89.150:8080/agm/v1/readings/temperature-humidity', data=data_json, headers=headers)
        print(response.text)
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')
    s.enter(15, 1, sendReqForSensorData, (sc,))


s = sched.scheduler(time.time, time.sleep)
# def do_something(sc):
#    print("creating script")
#    s.enter(2, 1, sendReqForSensorData)

s.enter(2, 1, sendReqForSensorData, (s,))
s.run()
