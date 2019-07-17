import pycurl
from io import StringIO
from io import BytesIO
import sys
import time
import socket
import json
import os

STATUS_OK = 0
STATUS_WARNING = 1
STATUS_ERROR = 2

MY_URL = os.environ["MY_URL"]
DATADOG_API_KEY = os.environ["DATADOG_API_KEY"]
DATADOG_APP_KEY = os.environ["DATADOG_APP_KEY"]

c = pycurl.Curl()
c.setopt(c.URL, MY_URL)
c.setopt(c.FOLLOWLOCATION, True)

def monitor(success, url, api_key, app_key):
    if success:
        status = 0
    else:
        status = 2
    print("status: ", status)
    c2 = pycurl.Curl()
    c2.setopt(c2.URL, "https://app.datadoghq.com/api/v1/check_run?api_key={0}&application_key={1}".format(api_key, app_key))
    data = {
       "check": "check_http",
       "host": socket.gethostname(),
       "host_name": socket.gethostname(),
       "timestamp": int(time.time()),
       "status": status,
       "message": "Testing {0}".format(url),
       "tags": ["url:{0}".format(url)]
    }
    c2.setopt(c2.POSTFIELDS, json.dumps(data))
    c2.setopt(c2.HTTPHEADER, ["Content-type: application/json"])
    try:
        c2.perform()
        print("Response from Datadog API:")
        print(c2.getinfo(c2.RESPONSE_CODE))
    finally:
        c2.close()
    
try:
    s = BytesIO()
    c.setopt(pycurl.WRITEFUNCTION, s.write)
    c.perform()
    print("Response from ", MY_URL, ":")
    print(c.getinfo(c.RESPONSE_CODE))
    success = c.getinfo(c.RESPONSE_CODE) == 200
    monitor(success, MY_URL, DATADOG_API_KEY, DATADOG_APP_KEY)
except pycurl.error:
    print("Response from ", MY_URL, ":")
    print(c.getinfo(c.RESPONSE_CODE))
    success = False
    monitor(success, MY_URL, DATADOG_API_KEY, DATADOG_APP_KEY)
finally:
    c.close()
