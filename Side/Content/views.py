from django.shortcuts import render , HttpResponse 
from . import scrape , models
import random
from .tasks import save_in_db
import json



counter = 0
def index(request):
    news = save_in_db()
    return render(request ,'index.html' , {'news':news})



def ajax_test(request):
    return HttpResponse(scrape.scrape_events())

def ajax(request):
    return render(request , 'ajax/index.html')


def testshow(request):
    rand_model = models.news.objects.order_by("?").first()
    print(rand_model)
    to_show = {'title': rand_model.title , 'date':rand_model.date  , 'image_url':rand_model.image_url}
    return render(request , 'testshow.html' , to_show)


def json_resp_Main_News(request):
    if(request.method == 'GET'):
        to_send = {'Success':False ,'reach_end':False, 'News':[]}
        if models.Client.objects.filter(token = request.GET.get('token')).exists():
            #client = models.clients.objects.get(token = request.GET.get('token'))
            start_from = int(request.GET.get('start_from'))
            count = int(request.GET.get('count'))
            max_count = models.Content_Main_News.objects.all().count()
            if(count > max_count):
                count = max_count
            if(start_from > max_count):
                start_from = 0
            if(start_from + count >= max_count):
                to_send['reach_end'] = True

            to_get_from_db = []
            for i in range(start_from,start_from + count):
                if(i > max_count - 1):
                    index_to_get = i - max_count
                    
                else:
                    index_to_get = i
                print(index_to_get)
                to_get_from_db.append(models.Content_Main_News.objects.all()[index_to_get])
            for entries in to_get_from_db:
                a_news = {'title':'' , 'image':''}
                a_news['title'] = entries.title
                a_news['image'] = entries.image
                to_send.get('News').append(a_news)

            to_send['Success'] = True
            return HttpResponse(json.dumps(to_send , ensure_ascii=False))



def json_event_resp(request):
    if(request.method == 'GET'):
        to_send = {'Success':False , 'News':[]}
        if (models.clients.objects.filter(token = request.GET.get('token')).exists()):
            client = models.clients.objects.filter(token = request.GET.get('token'))[0]
            last_event_seen = client.last_event_seen

            if(last_event_seen < models.events.objects.count() - 1):
                last_event_seen += 1
            else:
                last_event_seen = 0

            the_event = models.events.objects.all()[last_event_seen]

            event_to_send = {'title':'' , 'image':''}
            event_to_send['title'] = the_event.title
            event_to_send['image'] = the_event.image_url

            
                
            client.last_event_seen = last_event_seen
            client.save()
            to_send['Success'] = True
            return HttpResponse(json.dumps(event_to_send , ensure_ascii=False))


    
# Create your views here.
