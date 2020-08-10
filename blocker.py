import time

host_path = "C:\Windows\System32\drivers\etc"
# location of the driver that disables the website
redirect = '127.0.0.1'
# IP that will redirect your request, landing p
website_block = ['www.facebook.com', 'facebook.com', 'www.twitter.com']

while True:
    #check the time that will condition the block

    print(1)
    time.sleep(5)