import pyflate
import board
import time
import socketpool
import ssl
import wifi
import adafruit_requests

try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

print("Connecting to wifi")
wifi.radio.connect(ssid=secrets["ssid"], password=secrets["password"])
socket_pool = socketpool.SocketPool(wifi.radio)
print("Connected with IP ", wifi.radio.ipv4_address)

requests = adafruit_requests.Session(socket_pool, ssl.create_default_context())

URL = "https://analytics.usa.gov/data/live/realtime.json"
response = requests.get(URL, headers=headers)
data = response.content

"""
data = b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03EPAN\xc3@\x0c\xbc\xe7\x15\xd6\x9e\x9b*\x1b\n%\xb9\xf1\x81\x1e*\xb8\x80PeRSVl\x92\xd6\xeb\x14\xaa(\x7f\xc7\xd9\xa4tO\x9e\xb1g\xec\xd9>\x010\r\xd6dJ0L\xe8\xc5i\xbd\x18\xd9\x80\xf5\xd1\xbb\xe6\xa0\x9d~\x88\xcc\xa9#\xbe\x8cP\x81\xc2\x9a\x84]\x15\x94x\x8b\x84R,%V\xe2\xce\xf4\x12\x88\x83\x89\xf4\xfbb\x1e\xc7\xdf\x94)t^F\x89\xcd\xf4icrV+\xbc\x19_\xefy\x8aV\x10\xbd`\xeb\x0e_\x02\x9b\xf6\xc7\xcc~{\n\x15\xbb\xa3\xb8\xb6\x19\x877]\xfdA\x0c\xed\'tq\xbe\xea\x98\xa9\x11\x7f\x81\xb3\x0bN4\x08\xa0\xf7\xa0%\x85\xa5\xf9\xdf\xbc\xc7\xb8yJ\xd0_sL!vQ\xd9\xf2x\xaf\xc9\x8b\xb5\xbd\x7f\x9c"\r\xc9\x1c\xcbH+\xe8\xc3\xed\x8b\x04\xbf\xa9\xd9\xa1DE\x96\xe7i\x96\xa76\x7f\xb6\xeb\xd2>\x94w\xabe\xb1*^M2\xfc\x01]\xf7\nbw\x01\x00\x00'
"""

out = pyflate.decode(data)
print(out)
