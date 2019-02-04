# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class News(models.Model):
    text_on_video = models.CharField(u'надпись на видео', max_length=25, blank=True, null=True)
    video_present = models.URLField(u'ссылка на видео', blank=True, null=True)
    image_present = models.ImageField(u'картинка вместо видео для телефонов', upload_to="db_img", blank=True, null=True)