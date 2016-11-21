from prometheus_client import start_http_server, Gauge
from w1thermsensor import W1ThermSensor
import time


sensorgauge = Gauge('sensor_temperature_celsius', 'Sensor temperature value in celsius', ['sensor'])

#@sensorgauge.time()
def track_sensors(t):
    for sensor in W1ThermSensor.get_available_sensors():
        sensorgauge.labels("%s" % sensor.id).set("%.2f" % sensor.get_temperature())
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)

    while True:
        track_sensors(1)