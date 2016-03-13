from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone

class Source(models.Model):
  username = models.CharField(max_length=1024)
  broadcast = models.CharField(max_length=1024, default='')
  broadcast_end = models.DateTimeField('end of broadcast', default=None)
  lastpoll = models.DateTimeField('date last pulled', default=None)
  def isDepricated(self):
    if self.lastpoll and timezone.now() > (self.lastpoll + timedelta(0, 300)):
      return True
    return False
