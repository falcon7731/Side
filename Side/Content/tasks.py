from . import scrape , models
from celery.decorators import task , periodic_task
from celery.task.schedules import crontab
from webdocs.celery import app



def queue_maker():
        for client in models.clients.objects.all():
                #news queue
                old_queue = client.queue
                new_queue = models.queue()
                new_queue.save()
                for a_news in models.news.objects.all():
                        new_queue.entries.add(a_news)
                client.queue = new_queue
                client.last_seen = 0
                client.save()
                old_queue.delete()
                print('queue')




def save_events():
        scraped_events = scrape.scrape_events()
        models.events.objects.all().delete()
        print(len(scraped_events))
        for a_event in scraped_events:
                if(a_event.get('images_url') != None):
                        new_event = models.events()
                        new_event.title = a_event.get('title')
                        new_event.image_url = a_event.get('images_url')
                        new_event.save()
                        print('event')
                        






def save_news():
        news = []
        scraped = scrape.scrape_news()
        models.news.objects.all().delete()
        for a_news in scraped:
                if(a_news.image_url != ''):
                        new_news = models.news()
                        new_news.title = a_news.title
                        new_news.date = a_news.date
                        new_news.image_url = a_news.image_url
                        new_news.save()
                        print('news')
                        news_dict = {'title':a_news.title , 'date':a_news.date , 'image_url':a_news.image_url}
                        news.append(news_dict)
                        
        
        




@periodic_task(run_every = crontab())
def save_in_db():
    save_news() 
    save_events()
    queue_maker()
    #return news


    