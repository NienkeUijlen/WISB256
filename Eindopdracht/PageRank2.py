import urllib
import urllib.request
import re
from re import findall


X=[]
Lijst=['http://www.verseoogst.nl/']
domein = 'verseoogst.nl'
def JoriEnNienkesSuperfunctieEnTinkaIsErNiet(myurl):
    try:
        x = urllib.request.urlopen(myurl)
        for i in re.findall('''href=["'](.[^"']+)["']''', str(x.read()), re.I):
            if re.search("css$", i) == None and re.search("png$", i) == None and re.search("ico$", i) == None and re.search("/rss/", i) == None and re.search(".pdf$", i) == None:
                if (re.search(domein, i) == None) and (re.match('www', i)==None) and (re.match('http', i) == None):
                    if re.match("/", i) == None:
                        i = "/" + i
                    i = "http://www." + domein + i
                    if (i in Lijst) == False:
                        Lijst.append(i)
                    a = (Lijst.index(myurl),Lijst.index(i))
                    if (a in X) == False:
                        X.append(a)
                        
                        
                elif re.search(domein, i):
                    
                    if (i in Lijst) == False:
                        Lijst.append(i)
                    a = (Lijst.index(myurl),Lijst.index(i))
                    if (a in X) == False:
                        X.append(a)
                        
                        
    except:
        pass
    
JoriEnNienkesSuperfunctieEnTinkaIsErNiet('http://www.verseoogst.nl/')

print(Lijst)
print(len(Lijst))

for i in Lijst:
    print(i)
    JoriEnNienkesSuperfunctieEnTinkaIsErNiet(i)
  
for j in Lijst:
    print(str(Lijst.index(j))+ " "+ str(j))
print(len(Lijst))
print(X)
print(len(X))
