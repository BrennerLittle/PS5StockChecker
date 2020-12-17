urls = ["https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149",
        "https://www.target.com/p/playstation-5-console/-/A-81114595",
        "https://www.walmart.com/ip/PlayStation-5-Console/363472942"]
import time
import requests
from bs4 import BeautifulSoup
import winsound

y = 0
while (True):
    while (y < len(urls)):
        link = urls[y]

        agent = {"User-Agent": "Mozilla/5.0"}
        source = requests.get(link, headers=agent).text
        html = requests.get(link).text

        soup = BeautifulSoup(source, "lxml")
        res = soup.findAll(text="This item is out of stock.")

        if ("Add to Cart" in html):
            print("found it " + link)
            frequency = 2500  # Set Frequency To 2500 Hertz
            duration = 1000  # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)

        else:

            print("not found " + link)
        y += 1

    print("sleep")
    time.sleep(600)
    print("sleep")
    y = 0
