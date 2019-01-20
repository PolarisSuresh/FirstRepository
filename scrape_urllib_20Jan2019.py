#!C:/Users/Suresh/AppData/Local/Programs/Python/Python37-32/python.exe
'''
For learning print function in Python 
By Suresh
Python ver 3.7
On date 31-Dec-2018, revised on 20-Jan-2018
'''
import urllib.request

#Collect and parse first page
request_url = urllib.request.urlopen('https://www.besanttechnologies.com/')
print(request_url.read())

