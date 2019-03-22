# -*- coding: utf-8 -*-
from django.db import models

class Comment(models.Model):
    email = models.CharField(u'Email', max_length=100, blank=False, null=False)
    fio = models.CharField(u'ФИО', max_length=100, blank=False, null=False)
    comment_text = models.TextField(u'Комментарий', blank=False, null=False)
    view = models.BooleanField(u'Показывать на сайте', default=False)
    image = models.ImageField(u'Фотография для отзыва', blank=True, null=True)

    def __unicode__(self):
        return "%s %s" % (self.email, self.credentials)

    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
