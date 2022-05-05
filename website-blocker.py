import time
from datetime import datetime as dt

hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]

while True: #to keep the script running all the time.
    if dt(dt.now().year,dt.now().month,dt.now().day,23) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day+1,1):
        print("Working hours")
    else:
        print("Fun hours")
    time.sleep(5)