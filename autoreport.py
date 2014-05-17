from BeautifulSoup import BeautifulSoup
import urllib2

xyList=[]

def getProxy():
	html = urllib2.urlopen('http://www.cybersyndrome.net/pla.html')
	soup= BeautifulSoup(html)
	for i in soup.body.ol.findAll('li'):
		xyList.append(i.text)
	return xyList

def main(xyLocation):
	proxies = {'http':xyLocation}
	try:
		proxyHandler = urllib2.ProxyHandler(proxies)
		opener = urllib2.build_opener(proxyHandler)
		urllib2.install_opener(opener)
		f = urllib2.urlopen('http://search.yahoo.co.jp/search?p=%E5%81%BD2ch%E9%A8%92%E5%8B%95&ei=UTF-8')
		data = f.read()
	except:
		print 'Some Error Happened'

if __name__ == "__main__":
	for i in getProxy():
		print i
		main(i)
