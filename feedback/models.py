# -*- coding: utf-8 -*-
from django.db import models
from main.mixing import ImageMixin

class Comment(ImageMixin):
    email = models.CharField(u'Email', max_length=255, blank=False, null=False)
    credentials = models.CharField(u'ФИО', max_length=100, blank=False, null=False)
    comment_text = models.TextField(u'Комментарий', blank=False, null=False)

    def __unicode__(self):
        return "%s %s" % (self.email, self.credentials)

    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
