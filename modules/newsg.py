#!/usr/bin/env python
import feedparser
import re
import web

def newsg(phenny,input):
	str = ("http://news.google.com/news?q=%s&output=rss") % (web.urllib.quote(input.group(2).encode('utf-8')))
	d = feedparser.parse(str)
	try:
	        phenny.say(d['entries'][0]['title'])
		phenny.say(re.split('url=',d.entries[0]['link'])[-1])	
	except:
		phenny.say("Master I cant find anything !")
newsg.commands = ['news']
newsg.priority = 'medium'

if __name__ == "__main__":
    print __doc__.strip()
