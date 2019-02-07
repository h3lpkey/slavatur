# -*- coding: utf-8 -*-
from django.core.files.base import ContentFile
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail
from django.conf import settings
from django.db import models
import os


class ImageMixin(models.Model):
    image = models.ImageField(u'изображение', upload_to='db_img',
                              null=True, blank=True)

    def __unicode__(self):
        return self.image.name

    class Meta:
        abstract = True
        verbose_name = u'изображение'
        verbose_name_plural = u'изображения'
        

    @property
    def image_size(self):
        if self.image:
            size = (self.image.file.size/1024)/1024
            if size == 0:
                size = 0.5
        return u"%s Mb" % size

    def save(self, copied=False, *args, **kwargs):
        if not self.id and not copied:
            super(ImageMixin, self).save(*args, **kwargs)
            if self.image:
                resized = get_thumbnail(self.image, "800", upscale=False)
                os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))
                self.image.delete(False)
                self.image.save(resized.name, ContentFile(resized.read()), True)
        super(ImageMixin, self).save(*args, **kwargs)


class TitleMixin(models.Model):
    title = models.CharField(u'название', max_length=255)

    def __unicode__(self):
        return self.title

    def natural_key(self):
        return (self.title)

    class Meta:
        abstract = True
