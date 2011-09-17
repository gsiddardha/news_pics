import urllib
import xml.dom.minidom
from xml.dom.minidom import Node

u = urllib.urlopen('http://rss.news.yahoo.com/rss/mostviewed')
print "Got the feed ..."
f = open('feed.xml', 'w')
f.write(u.read())
u.close()
f.close()
print "Wrote the data into feed.xml ..."

doc = xml.dom.minidom.parse("feed.xml")
print "XML data now in variable called doc ..."

feed = {}
for node in doc.getElementsByTagName("item"):
    title = str((node.getElementsByTagName("title")[0]).childNodes[0].data)
    link = str((node.getElementsByTagName("link")[0]).childNodes[0].data)
    feed[link] = title
print "Stored all the titles and links in hashmap called feed ..."

