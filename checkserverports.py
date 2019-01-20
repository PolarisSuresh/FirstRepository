#!C:\Users\Suresh\AppData\Local\Programs\Python\Python37-32\python.exe

'''
For learning print function in Python 
By Suresh
Python ver 3.7
On date 16-Dec-2018
'''

#This is to check data types
import os	
import time
#This is to check the python ports
for t in range(6000,6002):
           print("Checking Port# ",t)
           cmd1="start cmd /k python -m http.server " + str(t)		
           os.system(cmd1)
           print(cmd1)