# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(u'Заголовок', max_length=25, blank=True, null=True)
    text = models.TextField(u'Текст', blank=False, null=True)
    pub_date = models.DateField(u'дата публикации', blank=True, null=True)
    image = models.ImageField(u'Фотография для новости', blank=True, null=True)