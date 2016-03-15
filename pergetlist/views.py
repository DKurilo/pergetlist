from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Source

from pergetlist.services import loadBrodcasts

def index(request):
  sourcesList = Source.objects.all()
  viewSourcesList = [];
  for source in sourcesList:
    if source.isDepricated():
      broadcast = loadBrodcasts(source.username)
      now = timezone.now()
      if 'id' in broadcast:
        source.broadcast = broadcast['id']
        source.broadcast_end = broadcast['end']
      else:
        source.broadcast = '';
        source.broadcast_end = now;
      source.lastpoll = now
      source.save();
    broadcast_end = 'Live!';
    if source.broadcast_end != None:
      broadcast_end = source.broadcast_end.strftime('%d/%m/%Y %H:%M:%S');
    viewSourcesList.append({
      'username': source.username, 
      'broadcast': source.broadcast, 
      'broadcast_end': broadcast_end, 
      'lastpoll': source.lastpoll.strftime('%d/%m/%Y %H:%M:%S'),
    })
  

  context = {"sources": viewSourcesList}
  return render(request, 'pergetlist/index.html', context)
