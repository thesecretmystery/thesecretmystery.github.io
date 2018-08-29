import urllib2

while True:
    try:
        url = raw_input("Enter URL: ")
        if 'https://' in url:
            url = url.replace('https://','http://')
        if 'http://' not in url:
            url = 'http://'+url
        page = urllib2.urlopen(url)
        data = page.readlines()
        for piece in data:
            if len(piece)>100000:
                datum = piece
        datum = datum.strip(' ')
        datum = datum.strip('\n')
                
        key_page = urllib2.urlopen(url+'//key.txt')
        key_str = key_page.read()
        key_list = key_str.split(',')
        key = [int(point) for point in key_list]

        output = [datum[point] for point in key]
        print ''.join(output)
    except ValueError:
        print 'That\'s not the right url.'
    except urllib2.HTTPError:
        print 'that\'s not the right url.'
    except urllib2.URLError:
        print 'that\'s not the right url.'