from bs4 import BeautifulSoup
import requests
import random


def scrape_news():
    all_news = []
    for  page in range(1,4):
        raw_html = requests.get("http://iauahvaz.ac.ir/fa/news?page=" + str(page)).text
        parsed = BeautifulSoup(raw_html , 'lxml')
        news_1 = parsed.find_all('article' , class_='news-item')
        for news_2 in news_1:
            this_news = news_class('','','')
            item_content = news_2.find('div' , class_ = 'item-content')
            title = item_content.h3.a.text
            link = item_content.h3.a.get('href')
            date = item_content.div.text
            img = news_2.find('img')
            if(img != None):
                image_page = requests.get(link).text
                parsed_image_page = BeautifulSoup(image_page , 'lxml')
                image_in_page = parsed_image_page.find_all('img' , alt = 'عکس')
                if(len(image_in_page) > 0):
                    image_url = image_in_page[0].get('src')
                else:
                    image_url = news_2.find('img').get('src')
                
                this_news.image_url = 'http://iauahvaz.ac.ir' + image_url
            this_news.title = title
            this_news.date = date
            all_news.append(this_news)
        
        
        
    return all_news


def scrape_events():
    to_return = []
    raw_html = requests.get("http://iauahvaz.ac.ir/fa/news/category/90/%D8%B1%D9%88%DB%8C%D8%AF%D8%A7%D8%AF-%D8%AC%D8%AF%DB%8C%D8%AF")
    parsed = BeautifulSoup(raw_html.text , 'lxml')
    events_1 = parsed.find_all('div' , class_='item-content')
    for events_2 in events_1:
        images_url = []
        evnets_3 = events_2.find('h3' , class_='title').a.get('href')
        title = events_2.find('h3' , class_='title').a.text
        img_page = requests.get(evnets_3)
        parsed_image_page = BeautifulSoup(img_page.text , 'lxml')
        image_1 = parsed_image_page.find_all('div' , class_='thumbnail')
        images_url = 'http://iauahvaz.ac.ir' + image_1[random.randint(0,len(image_1) - 1)].find('a' , class_='image-link').get('href')
        to_return.append({'title':title , 'images_url':images_url})

        
    return to_return
        










class news_class:
    title = ''
    date = ''
    image_url = ''
    def __init__(self , title , date , image_url):
        self.title = title
        self.date = date
        self.image_url = image_url
    def __str__(self):
        return str(self.title) + '||' +str(self.date) + '||' + str(self.image_url)
