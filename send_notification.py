import requests
from auth import *

message = "TONES RECEIVED. Stand by for text message dispatch."
data = {"verification":verification,"dispatch":message}
r = requests.post(url = url, data = data)

print message;
