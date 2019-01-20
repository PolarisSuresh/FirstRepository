#!C:\Users\Suresh\AppData\Local\Programs\Python\Python37-32\python.exe

'''
For learning list data type in Python 
By Suresh
Python ver 3.7
On date 23-Dec-2018
'''
import requests
a=requests.get("https://www.besanttechnologies.com/")
b=input("Enter what you want to search:")
print(a.text)
