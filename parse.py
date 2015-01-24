# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2

class Vote:
	name = ""
	result = ""

def get_first(iterable, default=None):
    if iterable:
        for item in iterable:
            return item
    return default

votes =[]
vote = Vote()
#f = open('test_vote.html', 'r')
document = urllib2.urlopen("http://www.eduskunta.fi/triphome/bin/thw.cgi/trip/?${APPL}=aanestysu&${BASE}=aanestysu&${THWIDS}=0.28/1422136048_22128&${oohtml}=aax/hex5000&${html}=aax/aax5000&${snhtml}=aax/aaxnosyn&${savehtml}=/thwfakta/aanestys/aax/aax.htm").read()
soup = BeautifulSoup(document)
for vote_part in soup.find(class_="statistics").find_all("td"):
	if (vote == None):
		vote = Vote()
	contents = get_first(vote_part.contents)
	if (contents != None and len(contents) > 1) : # check that the node has some data in it
		if (contents == "Jaa" or contents == "Ei" or contents == "Poissa" or contents == u"Tyhjää"):
			vote.result = contents
		else:
			vote.name = contents;
			
	if (vote.name and vote.result):
		votes.append(vote)
		vote = None

# Small data-analysis
jaa = 0
ei = 0
poissa = 0
tyhjaa = 0
for v in votes:
	if v.result == "Jaa":
		jaa += 1
	if v.result == "Ei":
		ei += 1
	if v.result == "Poissa":
		poissa += 1
	if v.result == u"Tyhjää":
		tyhjaa += 1
print "Jaa " + str(jaa)
print "Ei " + str(ei)
print "Poissa " + str(poissa)
print "Tyhjää " + str(tyhjaa)
print "Puolesta: "
for n in [ x for x in votes if x.result == "Jaa"]:
	print "  " + n.name
print "Vastaan: "
for n in [ x for x in votes if x.result == "Eis"]:
	print "  " + n.name



