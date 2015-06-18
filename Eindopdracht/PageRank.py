import urllib
import urllib.request
import re
from re import findall

domain = "uu.nl"
myurl = "http://" + domain
#input("@> ")
x = urllib.request.urlopen(myurl)
for i in re.findall('''href=["'](.[^"']+)["']''', str(x.read()), re.I):
#    print("hoofdpagina")
    if re.search("css$", i) == None and re.search("png$", i) == None and re.search("ico$", i) == None and re.search("/rss/", i) == None:
        if re.match("/", i):
            i = myurl + i
            print(i)
        
        elif re.search(domain, i):
            print(i)
        else:
            pass
  
    
    # try:
    #     for j in re.findall('''href=["'](.[^"']+)["']''', str(urllib.request.urlopen(str(i)).read()), re.I):
    #         print(j)
    # except:
    #     pass