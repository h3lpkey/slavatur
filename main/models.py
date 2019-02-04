# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class MainText(models.Model):
    text_on_video = models.CharField(u'надпись на видео', max_length=25, blank=True, null=True)
    video_present = models.URLField(u'ссылка на видео', blank=True, null=True)
    image_present = models.ImageField(u'картинка вместо видео для телефонов', upload_to="db_img", blank=True, null=True)

class Sortable(models.Model):
    order = models.PositiveIntegerField(u'порядок')

    class Meta:
        abstract = True

class Modules(models.Model, Sortable):
    publication = models.ForeignKey(MainText,
                                    verbose_name=u'модуль',
                                    related_name=u'item')
    text = RichTextField(u'текст')
    slug = models.SlugField(u'слаг', max_length=255)
    image_present = models.ImageField(u'картинка', upload_to="db_img", blank=True, null=True)
