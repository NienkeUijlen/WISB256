import urllib
import urllib.request
import re
from re import findall
from scipy.sparse import coo_matrix
import numpy as np


X=[]
row=[]
col=[]
Lijst=['http://www.madurodam.nl/']
domein = 'madurodam.nl'
def JoriEnNienkesSuperfunctieEnTinkaIsErNiet(myurl):
    try:
        x = urllib.request.urlopen(myurl)
        for i in re.findall('''href=["'](.[^"']+)["']''', str(x.read()), re.I):
            if re.search("css", i) == None and re.search("png$", i) == None and re.search("ico$", i) == None and re.search("/rss/", i) == None and re.search(".pdf$", i) == None and re.search("facebook", i)==None and re.search("twitter", i)==None and re.search("mailto", i)==None and re.search("google", i)==None and re.search(" ", i)==None:
                if (re.search(domein, i) == None) and (re.match('www', i)==None) and (re.match('http', i) == None):
                    if re.match("/", i) == None:
                        i = "/" + i
                    i = "http://www." + domein + i
                    if (i in Lijst) == False:
                        Lijst.append(i)
                    a = (Lijst.index(myurl),Lijst.index(i))
                    if (a in X) == False:
                        X.append(a)
                        row.append(Lijst.index(myurl))
                        col.append(Lijst.index(i))
                        
                elif re.search(domein, i):
                    
                    if (i in Lijst) == False:
                        Lijst.append(i)
                    a = (Lijst.index(myurl),Lijst.index(i))
                    if (a in X) == False:
                        X.append(a)
                        row.append(Lijst.index(myurl))
                        col.append(Lijst.index(i))
                        
    except:
        pass
    
JoriEnNienkesSuperfunctieEnTinkaIsErNiet('http://www.madurodam.nl/')

print(Lijst)
print(len(Lijst))

for i in Lijst:
    print(i)
    JoriEnNienkesSuperfunctieEnTinkaIsErNiet(i)
for j in Lijst:
    print(str(Lijst.index(j))+ " "+ str(j))
print(len(Lijst))
print(X[-1])
print(len(X))

data = len(row)*[1]
v = len(Lijst)*[1/len(Lijst)]

matrix = coo_matrix((data, (row, col)), shape=(len(Lijst), len(Lijst))).toarray()

print(matrix)

for i in range(10):
    v = matrix.dot(v)
    som = sum(v)
    v = (1/som)*v
    print(i,v)