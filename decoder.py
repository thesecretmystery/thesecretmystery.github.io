import urllib2

url = raw_input("Enter URL: ")
page = urllib2.urlopen(url)
data = page.readlines()
for piece in data:
    if len(piece)>1000:
        datum = piece
datum = datum.strip(' ')
datum = datum.strip('\n')
        
key_page = urllib2.urlopen(url+'//key.txt')
key_str = key_page.read()
key_list = key_str.split(',')
key = [int(point) for point in key_list]