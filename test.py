#! /usr/bin/env python
import urllib, sgmllib, sys, getopt, time

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
		
	def check(self, url):
		try:
			f = urllib.urlopen(url)
			code = f.getcode()
			f.close()
			if code == 404:
				self.urls404.append(url)
				return '404 %s' % url
			else:
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
			print '> %s' % url
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
	
print check.invalid
print check.urls404




