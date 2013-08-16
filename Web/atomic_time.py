#!/usr/bin/env python2.7
import urllib2 as url
import bs4 as bs


clock_url = 'http://www.time.gov/timezone.cgi?UTC/s/0'
html = bs.BeautifulSoup(url.urlopen(clock_url).read())
time = str(html.b.contents[0])

print "Atomic Time is  " + time