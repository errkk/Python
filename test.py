#! /usr/bin/env python
import urllib, sgmllib, sys, getopt, time, re

class MyParser(sgmllib.SGMLParser):
	"My Class for Parsing"
	
	def parse(self, s):
		"Parse the given string 's'"
		self.feed(s)
		self.close()
		
	def __init__(self,verbose=0):
		"Init an object, passing verbose to the superclass"
		
		sgmllib.SGMLParser.__init__(self, verbose)
		self.hyperlinks = []
		self.img = []		
		
	def start_a(self, attributes):
		"Process a hyperlink and its attributes"
		
		for name, value in attributes:
			if name == "href":
				self.hyperlinks.append(value)

	def start_img(self, attributes):
		for name, value in attributes:
			if name == "src":
				self.img.append(value)

	def get_hyperlinks(self):
		return self.hyperlinks
		
		
class CheckLinks():
	def __init__(self):
		self.urls404 = []
		self.invalid = []
		self.start = time.time()
		
	def _getcode(self,url):
		f = urllib.urlopen(url)
		code = f.getcode()
		f.close()
		return code
	
		
	def check(self, url):
		p = re.compile('http://')
		match = p.findall(url)

		if match.count('http://'):
			test = url
		else:
			test = site + url
			
		print '> %s' % test

		try:
			code= self._getcode(test)			
			if code == 404:
				self.urls404.append(url)
			return code
		except:
			self.invalid.append(url)
		 	return 0

			
	def looplinks(self,links):
		count = 0
		print 'Checking:'
		for url in links:
			self.check(url)
			count += 1
		print '---------'
		timetaken = time.time() - self.start	
 		print 'Scanned %d urls in %.2f seconds' % ( count, timetaken )
		print '---------'
		
try:
	site = sys.argv[1]
except:
	site = 'http://google.com'
	print 'Plese give a url'

try:
	f = urllib.urlopen(site)
	s = f.read()
	f.close()
	myparser = MyParser()
	myparser.parse(s)
	links = myparser.get_hyperlinks()
	
except:
	print 'Cant find %s' % site		
		


check = CheckLinks()
check.looplinks(links)

countinvalid = 0
for i in check.invalid:
	countinvalid += 1
	
if countinvalid:	
	print 'There was %d invalid URLs' % countinvalid
	print check.invalid


count404 = 0
for i in check.urls404:
	count404 += 1	
	
if count404:	
	print 'There were %d not found pages' % count404
	print check.urls404




