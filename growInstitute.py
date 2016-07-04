# -*- coding: utf-8 -*-

#growInstitute.py

import random, time, os
from splinter import Browser


def getMeaning(b, wordchoice):
	defs = []
	wordchoice
	#
	b.visit('https://duckduckgo.com/?q=define%3A+'+wordchoice+'&ia=definition')
	time.sleep(2)
	definitions = b.find_by_css('.zci__def__definition') #..wd-dfn  #.lr_container.mod

	for d in definitions:
		defs.append(d.text)
	
	return defs

def getLastInstitute(filepath):
	for line in open(filepath):pass
	#print line
	return line

def Main():
	localdir = os.path.dirname(os.path.realpath(__file__))

	path = localdir + "/institutions.txt"
	#print path
	inst = getLastInstitute(path)
	i = inst.split(' ')
	lastword = i[len(i)-1]
	#print lastword
	b= Browser('chrome')
	meanings = getMeaning(b, lastword)
	print meanings


if __name__ == '__main__':
	Main()