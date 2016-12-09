# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User
import datetime


class Feedback(models.Model):
    name = models.CharField( max_length=225, verbose_name=u'Ваше имя')
    subject = models.CharField(max_length=255, verbose_name=u'тема')
    message = models.TextField(verbose_name=u'сообщение')
    from_email = models.EmailField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
		return self.subject

class CallOrder(models.Model):
    name = models.CharField( max_length=100, verbose_name=u'Ваше имя')
    subject = models.CharField(max_length=100, verbose_name=u'тема')
    phone = models.IntegerField(max_length=100, verbose_name=u'Ваш телефон')
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
		return self.subject

