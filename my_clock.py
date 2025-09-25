import time
from datetime import datetime

while True:
    now = datetime.now()
    print("Current time:", now.strftime("%I:%M:%S %p"), end='\r')
    time.sleep(1)