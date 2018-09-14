# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext

# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=130, default='Tetra')
#    members = models.CharField(max_length=13, blank=True)

    class Meta:
         ordering = ('name',)
    def __str__(self):
        return self.name

class Members(models.Model):
    name = models.CharField(max_length=130, default='Bob')
    GamesJoined = models.ManyToManyField(Games, related_name='joiners', null=True)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
         ordering = ('name',)
    def __str__(self):
        return self.name
