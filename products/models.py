# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

class Powder(models.Model):
    name = models.CharField(
        max_length=70)
    powder_type = models.CharField(
        max_length=70, choices=((u'Для Цветного Белья', "Color"),(u'Для Белого Белья', "White")))
    packing = models.CharField(
        max_length=70, choices=(('3kg', '3'),('15kg', '15')))
    auto = models.CharField(
        max_length=70, choices=((u'Автомат', "yes"),(u'Ручная стирка', "no")), default='no')
    price_wholesale = models.FloatField(
        verbose_name=u"Цена опт.")
    price_retail = models.FloatField(
        verbose_name=u"Цена розница")
    description = models.TextField()
    photo = models.ImageField(
        upload_to='products', default = "/images/pexels-photo-45718.jpeg")
    availability = models.BooleanField(default=True)
    
    def __unicode__(self):
		return self.name

class AboutPowder(models.Model):
    name = models.CharField(
        max_length=70)
    description = models.TextField()
    propose = models.TextField(default="Malve")

    def __unicode__(self):
		return self.name

class NavButton(models.Model):
    name = models.CharField(
        max_length=70)
    number = models.PositiveIntegerField()

    def __unicode__(self):
		return self.name

class Contact(models.Model):
    phone_1 = models.IntegerField(
        max_length=15)
    phone_2 = models.IntegerField(
        max_length=15)
    phone_3 = models.IntegerField(
        max_length=15)
    email = models.EmailField()
    photo = models.ImageField(
        upload_to='products_img', null=True)
    
    def __unicode__(self):
		return self.email
