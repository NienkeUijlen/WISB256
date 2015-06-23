import urllib
import urllib.request
import re
from re import findall

Lijst=[]
domein = 'boswell-beta.nl'
def JoriEnNienkesSuperfunctieEnTinkaIsErNiet(myurl):
    try:
        x = urllib.request.urlopen(myurl)
        for i in re.findall('''href=["'](.[^"']+)["']''', str(x.read()), re.I):
            if re.search("css$", i) == None and re.search("png$", i) == None and re.search("ico$", i) == None and re.search("/rss/", i) == None:
                if (re.search(domein, i) == None) and (re.match('www', i)==None) and (re.match('http', i) == None):
                    if re.match("/", i) == None:
                        i = "/" + i
                    i = myurl + i
                    if (i in Lijst) == False:
                        Lijst.append(i)
                    
                elif re.search(domein, i):
                    if (i in Lijst) == False:
                        Lijst.append(i)
                    
    except:
        pass
            
JoriEnNienkesSuperfunctieEnTinkaIsErNiet('http://www.boswell-beta.nl')

print(Lijst)

for i in Lijst:
    JoriEnNienkesSuperfunctieEnTinkaIsErNiet(i)
  
print(Lijst)
    
    # try:
    #     for j in re.findall('''href=["'](.[^"']+)["']''', str(urllib.request.urlopen(str(i)).read()), re.I):
    #         print(j)
    # except:
    #     pass