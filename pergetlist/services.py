import urllib.request
import json, re
from html.parser import HTMLParser
from datetime import datetime
from .models import Source

class MyHTMLParser(HTMLParser):
  broadcastData = ''
  #def __init__(self):
  #  self.broadcastData = ''
  def get_broadcast(self):
    return json.loads(self.unescape(self.broadcastData))
  def handle_starttag(self, tag, attrs):
    if tag == 'meta' and attrs[0][0] == 'id' and attrs[0][1] == 'broadcast-data':
      self.broadcastData = attrs[1][1];

def loadBrodcasts(user):
  broadcast = {};
  url = 'https://www.periscope.tv/' + user
  request = urllib.request.Request(url)
  response = urllib.request.urlopen(request)
  html = response.read().decode('utf-8')
  
  parser = MyHTMLParser()
  parser.feed(html);
  
  broadcastData = parser.get_broadcast();
  
  if 'id' in broadcastData['broadcast']:
    broadcast['id'] = broadcastData['broadcast']['id']
    
    iso_ts = re.sub(r'(.*)\.\d{9}(.*):(.+)', '\g<1>\g<2>\g<3>', broadcastData['broadcast']['end']);
    broadcast['end'] = datetime.strptime(iso_ts, '%Y-%m-%dT%H:%M:%S%z')

  return broadcast;
