from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import RegexValidator

class textMessage(models.Model):
    addr = models.CharField(max_length=25)
    date = models.CharField(max_length=30)
    msgId = models.CharField(max_length=30)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user.username + " - " + self.msgId + " - " + self.addr