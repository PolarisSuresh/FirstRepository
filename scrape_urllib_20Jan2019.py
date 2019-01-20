#!C:/Users/Suresh/AppData/Local/Programs/Python/Python37-32/python.exe
'''
For learning print function in Python 
By Suresh
Python ver 3.7
On date 31-Dec-2018, revised on 20-Jan-2018
'''
import time
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

url= "http://toscrape.com/"
html=urlopen(url)
soup=BeautifulSoup(html.read(),"html.parser")
Text1=soup.h1
HeaderText=Text1.get_text()
body=soup.find('body')
body1=body.findChildren()
list=soup.prettify()
list=soup.find_all('td')
n=0
while (n < 3):
   string=list[n]
   newstring=string.strip()
   print('|',newstring,'|',len(newstring),'|')
   if 'of' in newstring:
     print('Yes')
   n=n+1
    