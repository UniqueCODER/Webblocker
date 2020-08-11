import time
from datetime import datetime as dat
host_path = "C:\Windows\System32\drivers\etc"
# location of the driver that disables the website
redirect = '127.0.0.1'
# IP that will redirect your request, landing p
website_block = ['www.facebook.com', 'facebook.com', 'www.twitter.com']

while True:
    #check the time that will condition the block
    year = dat.now().year
    month = dat.now().month
    day = dat.now().day
    if dat(year,month,day,8) < dat.now() < dat(year,month,day,16):
        print("Working Hours...")
    else:
        print(dat.now())
        time.sleep(5)
