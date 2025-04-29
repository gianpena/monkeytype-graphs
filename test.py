import json
from datetime import datetime

timestamp = 1682617200000
timestamp /= 1000
dt = datetime.fromtimestamp(timestamp)
print(dt.strftime('%b %d, %Y at %H:%M:%S'))