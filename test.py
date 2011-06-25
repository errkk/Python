#! /usr/bin/env python
import urllib, sgmllib, sys

f = urllib.urlopen('http://wottonpool.co.uk')
s = f.read()
f.close()

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
		
	def start_a(self, attributes):
		"Process a hyperlink and its attributes"
		
		for name, value in attributes:
			if name == "href":
				self.hyperlinks.append(value)
	
	def get_hyperlinks(self):
		return self.hyperlinks
		
		
class CheckLinks():
	def __init__(self):
		self.urls404 = []
		self.invalid = []
	
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
		for url in links:
			self.check(url)
			print url
		
		
		
myparser = MyParser()
myparser.parse(s)
links = myparser.get_hyperlinks()

check = CheckLinks()
check.looplinks(links)
	
print check.invalid
print check.urls404


