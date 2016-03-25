#!/usr/bin/python

import pycurl
import cStringIO
import csv
import re

import datetime
date1 = '2015-11-13'
date2 = '2016-03-13'
start = datetime.datetime.strptime(date1, '%Y-%m-%d')
end = datetime.datetime.strptime(date2, '%Y-%m-%d')
step = datetime.timedelta(days=1)

while start <= end:
  days = start.strftime('%m-%d-%Y').split('-')
  schools=[]
  games={}
  file="score_files/%s%s%s.raw" % (days[0],days[1],days[2])
  count=0

  with open(file) as f:
   content = f.readlines()
   team_indicator=0
   game_indicator=0

   for a in content:
	pass_line=0
	####  find the start of a game ####
	if "valign_top" in a:
	  games[count]=[]
	  game_indicator=1
	### detect score ###
	if team_indicator==1 and a.startswith("<td") and a.rstrip().endswith("</td>") and 'Final' not in a and pass_line==0:
	  pass_line=1
	  score = re.sub('^.*>','',re.sub('</td>.*$','',a.rstrip()))
	  games[count].append(score)
	  team_indicator=0
	  if len(games[count])==4: 
		#print games[count]
		count+=1
		game_indicator=0
	### detect team ###
	if a.startswith("<td") and a.rstrip().endswith("</td>") and game_indicator==1 and 'Final' not in a and pass_line==0:
	  team = re.sub('^.*>','',re.sub('<\/a>.*$','',re.sub('<\/td>.*$','',a.rstrip())))
	  pass_line=1
	  games[count].append(team)
	  team_indicator=1

  #print len(games)
  for a in games:
    if games[a][1]!='' and games[a][3]!='': 
      print "%s|%s|%s|%s" % (games[a][0],games[a][1],games[a][2],games[a][3])

  start += step

