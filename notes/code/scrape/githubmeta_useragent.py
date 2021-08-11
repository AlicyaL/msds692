import requests
import time
import random
from bs4 import BeautifulSoup

def fetch(url,delay=(1,2)):
    """
    Simulate human random clicking x..y seconds then fetch URL.
    Returns the actual page source fetched and the HTML object.
    """
    time.sleep(random.randint(delay[0],delay[1])) # wait random seconds
    try:
        response = requests.get(url, headers={"User-Agent":"Resistance is futile"})
    except ValueError as e:
        print(str(e))
        return '', BeautifulSoup('', "html.parser")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    return (html,soup)

print(requests.utils.default_headers())

data,soup = fetch("https://api.github.com/meta")
print(data)
