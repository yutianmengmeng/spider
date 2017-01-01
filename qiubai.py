# -*- coding:  UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import pymongo
import time

client = pymongo.MongoClient("localhost", 27017)
qiubai = client['qiubai']
jokes_tab = qiubai['jokes_tab']
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
urls = ['http://www.qiushibaike.com/8hr/page/{}'.format(str(i)) for i in range(1, 36)]


def get_jokes_from(urls):
    time.sleep(2)
    wb_data = requests.get(urls, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select("div.author ")
    jokes = soup.select("a > div.content ")
    for title, joke in zip(titles, jokes):
        data = {
            'title': title.get_text(),
            'joke': joke.get_text(),
        }
        jokes_tab.insert_one(data)

for single_url in urls:
    get_jokes_from(single_url)



