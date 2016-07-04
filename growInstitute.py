# -*- coding: utf-8 -*-

#growInstitute.py

import random, time, os
from splinter import Browser



def docEntry(localdir, name, text, write):
	fullpath = localdir + "/institutions/"+name
	print fullpath
	with open(fullpath, write) as myfile:
		myfile.write(text)
	myfile.close()



def formatHeader(entry,s1): 
	### center title
	length = len(entry)
	spacerLen = int((70 - length)/2)
	spacer = ""
	for s in range(spacerLen):
		spacer = spacer + " "


	### Detail inspired by Thricedotted 'The Seeker':
	header = []
	for x in range(5):
		
		for y in range(70):
			symbols = [s1,s1,s1,s1,' ', '-']
			random.shuffle(symbols)
			header.append(symbols[0])

		header.append('\n')

	headString = ''
	for h in header:
		headString = headString + h

	# linebreak = "\n"
	# for x in range(35):
	# 	linebreak = linebreak + "- "

	# linebreak = linebreak + "\n \n"
	responseheader = headString +'\n'+ '\n'+ spacer+ entry +'\n'+'\n'+ '\n'+headString
	#formattedEntry = responseheader + linebreak
	return responseheader

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

# make first letter in sentence uppercase
def upcase_first_letter(s):
	newstr = s[0].capitalize() + s[1:]
	#print s[0]
	return newstr

def Main():
	localdir = os.path.dirname(os.path.realpath(__file__))

	path = localdir + "/institutions.txt"
	print path
	inst = getLastInstitute(path)
	instwords = inst.split(' ')
	lastword = instwords[len(instwords)-1]
	### make text doc name and doc
	docname = ""
	for i in instwords:
		docname = docname + upcase_first_letter(i)
	docname = docname + ".txt"
	docEntry(localdir,docname, '\n','w')
	### add title of institution
	nameInCaps = ""
	for l in inst:
		try:
			lc = l.capitalize()
			nameInCaps = nameInCaps + lc
		except:
			pass
	print nameInCaps
	symbols = ['#','$','§','º','∑','∫','≈','ß','˙','^']
	random.shuffle(symbols)
	header = formatHeader(nameInCaps, symbols[0])
	docEntry(localdir,docname, header,'a')

	#print lastword
	# b= Browser('chrome')
	# meanings = getMeaning(b, lastword)
	# print meanings


if __name__ == '__main__':
	Main()