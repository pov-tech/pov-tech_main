from BeautifulSoup import BeautifulSoup
import urllib2
from random import randint

xyList=[]

def getProxy():
	html = urllib2.urlopen('http://www.cybersyndrome.net/pld.html')
	soup= BeautifulSoup(html)
	for i in soup.body.ol.findAll('li'):
		xyList.append(i.text)
	return xyList

def main(xyLocation):
	proxies = {'http':xyLocation}
	try:
		proxyHandler = urllib2.ProxyHandler(proxies)
		opener = urllib2.build_opener(proxyHandler)
		opener.addheaders = [('User-agent','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)')]
		urllib2.install_opener(opener)
		f = urllib2.urlopen('http://search.yahoo.co.jp/search?p=%E5%81%BD2ch%E9%A8%92%E5%8B%95&ei=UTF-8')
		data = f.read()
		sleep (randint(15,45))
	except:
		print 'Some Error Happened'

if __name__ == "__main__":
	for i in getProxy():
		print i
		main(i)
