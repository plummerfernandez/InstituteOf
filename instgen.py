# -*- coding: utf-8 -*-

### INSTALL NOTES / DEPENDENCIES
# sudo pip install pattern
# pip install nltk #(very large module)
# pip install RandomWords
# pip install twython
# download then brown corpus

from twython import Twython, TwythonError
import random, os, ConfigParser
from random_words import RandomWords
import pattern.en
import nltk
from nltk.corpus import brown
from random import randrange

### Save to clean once complete. 
def appendtoTxt(institute, localdir):
	fullpath= localdir+"/institutions.txt"
	#print fullpath
	with open(fullpath, "a") as myfile:
		myfile.write("\n")
		myfile.write(institute)

### Only twitter function here, simply tweets a txt message
def tweetStatus(twitter, msg):
	print ">>> tweeting now"
	print msg
	twitter.update_status(status=msg)
	print "[+] status updated"

# use nltk corpus to find good adj-noun combo given a list of nouns
def getbestadjnoun(wordlist):
	adjnouns =[]
	adjcounts =[]
	brown_learned_text = brown.tagged_words()
	for word in wordlist:
		noun = word
		if " " in word: #if there is a space present in my word, take the second word
			noun = word.split(" ")[1]
		precs = sorted(set(a for (a, b) in nltk.bigrams(brown_learned_text) if b[0] == noun))
		adjs =[]
		for prec in precs:
			if prec[1] == 'JJ':
				adjs.append(prec[0])
		if adjs:
			#print adjs
			adjnouns.append(adjs[randrange(0,len(adjs))]+" "+word)
			adjcounts.append(len(adjs))
	print adjnouns
	#print adjcounts
	#indx = adjcounts.index(max(adjcounts))
	#return adjnouns
	if len(adjs) > 0:
		return adjs
	else:
		return None 

#Provides a random search word
def randWord():
	rw = RandomWords()
	word = rw.random_word()
	return word

# make first letter in sentence uppercase
def upcase_first_letter(s):
	newstr = s[0].capitalize() + s[1:]
	#print s[0]
	return newstr

# Generate an institution
def genInstitute():
	
	adj = None
	
	while adj == None:
		typ = randWord()
		t = []
		t.append(typ)
		adj = getbestadjnoun(t)
	
	print adj
	random.shuffle(adj)

	typs = pattern.en.pluralize(typ)
	if typs[-2:] == 'ss':
		typs = typs[:-1]
	instituteTypes = ["Institute of ","Institute for ", "Institution of ", "Institution for "]
	random.shuffle(instituteTypes)
	institute = "The " +  upcase_first_letter(adj[0]) + " " + instituteTypes[0] + upcase_first_letter(typs)
	return institute


def Main():
	# You need to put your twitter api_key, secret, oauth token and oauth secret into settings.cfg
	config = ConfigParser.ConfigParser()
	try:
		localdir = os.path.dirname(os.path.realpath(__file__))
		print localdir
		print localdir
		config.read(localdir + '/settings.cfg')
		print "[+] Read settings"
	except:
		print "[-] Could not read settings"

	tw_key = config.get('twitter','API_KEY')
	tw_secret = config.get('twitter','API_SECRET')
	tw_token = config.get('twitter','OAUTH_TOKEN')
	tw_tsecret = config.get('twitter','OAUTH_TOKEN_SECRET')

	print '[+] Twitter client requested' 

	twitter = Twython(tw_key, #API_KEY
					tw_secret,  #APP_SECRET
					tw_token,   #OAUTH_TOKEN
					tw_tsecret) #OAUTH_TOKEN_SECRET

	institute = genInstitute()

	print institute
	appendtoTxt(institute, localdir)
	tweetStatus(twitter, institute)


if __name__ == '__main__':
	Main()

