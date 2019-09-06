from django.urls import path
from . import views
urlpatterns = [
    path('main_news' , views.json_resp_Main_News),
]
