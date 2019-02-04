# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(u'Имя отправителя', max_length=25, blank=True, null=True)
    text = models.CharField(u'Текст отзыва', max_length=255, blank=True, null=True)
    show = models.BooleanField(u'показывать на сайте', default=True)
    image_present = models.ImageField(u'Фото для отзыва', upload_to="db_img", blank=True, null=True)