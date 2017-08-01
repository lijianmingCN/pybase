# -*- coding: UTF-8 -*-
import urllib2
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import re,socket

def getHtml(url):
    response=urllib2.urlopen(url)
    html=response.read()
    return html
def getHref(html):
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()
    return parser.links

def getIpByURL(url):
    try:
        ip = socket.gethostbyname(url)
    except socket.error, err_msg:
        print "%s: %s" %(url, err_msg)
    return ip

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            if len(attrs) == 0: pass
            else:
                for (variable, value)  in attrs:
                    if variable == "href":
                        self.links.append(value)



def findHTML(startURL):
    html = getHtml(startURL)
    hrefs = getHref(html)
    regex_complate = re.compile('http://[A-Za-z/.]*')
    regex_host = re.compile('http://[A-Za-z/.]*.com')
    for href in hrefs:
        match = re.search(regex_complate,href)
        if match:
            url = match.group()
            if 'action' not in url:
                if url[-1] == '/':
                    print url[:-1]
                    findHTML(url[:-1])
                    
                match = re.search(regex_host,href)
                if match:
                    url = match.group()[7:]
                    print getIpByURL(url)
if __name__ == '__main__':
   findHTML('http://www.jd.com')


