import urllib2

while True:
    try:
        url = raw_input("Enter URL: ")                      #web adress entry.
        if 'https://' in url:                               #checks for https.
            url = url.replace('https://','http://')         #removes https (NOTHING IS SECURE).
        if 'http://' not in url:                            #checks for abreviated address.
            url = 'http://'+url                             #adds http if missing.
        page = urllib2.urlopen(url)                         #load page from URL.
        data = page.readlines()                             #reads each line from .html file.
        for piece in data:                                  
            if len(piece)>100000:                           #checks for the longest line.
                datum = piece                               #assigns line content to variable.
        datum = datum.strip(' ')                            #removes leading white space.
        datum = datum.strip('\n')                           #removes trailing new line character.
                
        key_page = urllib2.urlopen(url+'//key.txt')         #loads key index from 
                                                            #www.thesecretmystery.com/key.txt
                                                            #future keys are not so readily availabe.
        key_str = key_page.read()                           #reads string data from key.txt.
        key_list = key_str.split(',')                       #turns string into list of strings.
        key = [int(point) for point in key_list]            #converts string elements to integers.

        offset = 0                                          #the offset from the beginning of the
                                                            #text on the page. You can't rely on this 
                                                            #to be zero. You can't rely on anything.
        output = [datum[point+offset] for point in key]     #grabs characters from the text on the
                                                            #page and assembles them sequentially in
                                                            #a list according to the key and offset.
        print ''.join(output)                               #prints a string of the assembled message.
    except ValueError:                                      #checks for misspleeings, etc.
        print 'That\'s not the right url.'
    except urllib2.HTTPError:                               #checks for https and http inconsistencies.
        print 'that\'s not the right url.'
    except urllib2.URLError:                                #checks for incompatible URLs.
        print 'that\'s not the right url.'