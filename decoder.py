import urllib2

url = raw_input("Enter URL: ")
page = urllib2.urlopen(url)
data = page.readlines()
for piece in data:
    if len(piece)>1000:
        datum = piece
        
print len(datum)