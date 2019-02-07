# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
from main.mixing import ImageMixin


class MainText(models.Model):
    text_on_video = models.CharField(u'надпись на видео', max_length=25, blank=True, null=True)
    video_present = models.URLField(u'ссылка на видео', blank=True, null=True)
    image_present = models.ImageField(u'картинка вместо видео для телефонов', upload_to="db_img", blank=True, null=True)


class Module(models.Model):
    text = models.CharField(u'Надпись на картинке', max_length=25, blank=True, null=True)
    slug = models.SlugField(u'слаг', max_length=255)
    image_present = models.ImageField(u'картинка', upload_to="db_img", blank=True, null=True)


class Comment(ImageMixin):
    email = models.CharField(u'Email', max_length=255, blank=False, null=False)
    credentials = models.CharField(u'ФИО', max_length=100, blank=False, null=False)
    comment_text = models.TextField(u'Комментарий', blank=False, null=False)

    def __unicode__(self):
        return "%s %s" % (self.email, self.credentials)

    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
