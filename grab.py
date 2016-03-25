#!/usr/bin/python

import pycurl
import cStringIO
import csv
import re

import datetime
date1 = '2016-03-11'
date2 = '2016-03-13'
start = datetime.datetime.strptime(date1, '%Y-%m-%d')
end = datetime.datetime.strptime(date2, '%Y-%m-%d')
step = datetime.timedelta(days=1)

while start <= end:
  days = start.strftime('%m-%d-%Y').split('-')
  print days

  buf = cStringIO.StringIO()
  text = "http://www.sports-reference.com/cbb/boxscores/index.cgi?month=%s&day=%s&year=%s" % (days[0],days[1],days[2])
  print text

  c = pycurl.Curl()
  c.setopt(c.URL, text)
  c.setopt(c.WRITEFUNCTION, buf.write)
  c.perform()

  f = "%s%s%s.raw" % (days[0],days[1],days[2])
  with open(f,'a') as file:
    file.write(buf.getvalue())

  buf.close()
  start += step

