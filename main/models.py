# -*- coding: utf-8 -*-
from django.db import models

class Order(models.Model):
    name = models.CharField(u'Имя', max_length=100, blank=False, null=False)
    tel = models.CharField(u'Телефон', max_length=100, blank=False, null=False)
    email = models.CharField(u'Email', max_length=100, blank=False, null=False)
    message = models.TextField(u'Сообщение', blank=False, null=False)

    def __unicode__(self):
        return "%s %s" % (self.email, self.credentials)

    class Meta:
        verbose_name = u'Заявка'
        verbose_name_plural = u'Заявки'


class OrderSMS(models.Model):
    name = models.CharField(u'Имя', max_length=100, blank=False, null=False)
    tel = models.CharField(u'Телефон', max_length=100, blank=False, null=False)

    def __unicode__(self):
        return "%s %s" % (self.email, self.credentials)

    class Meta:
        verbose_name = u'SMS заявка'
        verbose_name_plural = u'SMS заявки'
