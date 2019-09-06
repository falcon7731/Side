from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Client(models.Model):
    token = models.CharField(default='', max_length=128)


    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

class Content_Main_News(models.Model):
    creator = models.ForeignKey(User , on_delete = models.CASCADE , null = True)
    title = models.CharField(default='', max_length=512)
    image = models.URLField()


    class Meta:
        verbose_name = 'Content_Main_News'
        verbose_name_plural = 'Content_Main_Newss'

class Content_Event(models.Model):
    creator = models.ForeignKey(User , on_delete = models.CASCADE , null = True)
    title = models.CharField(default='', max_length=1024)


    class Meta:
        verbose_name = 'Content_Event'
        verbose_name_plural = 'Content_Events'
