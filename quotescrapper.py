import urllib.request ,urllib.parse , urllib.error
from bs4 import BeautifulSoup
import ssl
import random 
c1=random.randrange(0,10)
y1="page/"+str(c1)
#print(y1)
if str(y1)=="page/0":
    y1=" "
#print(y1)

ctx=ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode=ssl.CERT_NONE
x=y1
url="http://quotes.toscrape.com/"+x
fhand=urllib.request.urlopen(url,context=ctx).read()
#print("Connecting ",url)
soup=BeautifulSoup(fhand,'html.parser')
print(soup.title.string)
mydivs = soup.findAll("span", {"class": "text"})
a=list()
z=0
for div in mydivs:
    a.append(div.text)
    z=z+1
b=random.randrange(1,9)
   
cy=print(a[b])


    
    
     
   
    
