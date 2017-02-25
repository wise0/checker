import requests
import time

urls = [ # this is a list of urls that you want to ping. Feel free to add more than one.
  "http://thecosmopolitan.herokuapp.com/",
]

while True:
  for url in urls:
    requests.get(url) # pinging the server
  time.sleep(300) # delay for 5 minutes  
