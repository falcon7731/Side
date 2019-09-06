from django.db import models

# Create your models here.
class Client(models.Model):
    token = models.CharField(default='', max_length=128)


class Content_Main_News(models.Model):

    title = models.CharField(default='', max_length=512)
    image = models.URLField()


class Content_Event(models.Model):

    title = models.CharField(default='', max_length=1024)
