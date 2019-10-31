# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Info(models.Model):

   text = models.CharField(max_length=50)
   create_date = models.DateTimeField('date published')


# Create your models here.
