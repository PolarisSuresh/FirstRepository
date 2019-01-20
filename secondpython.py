#!C:\Users\Suresh\AppData\Local\Programs\Python\Python37-32\python.exe

'''
For learning print function in Python 
By Suresh
Python ver 3.7
On date 24-Nov-2018
'''
import os
def funca():
     a=3
     print("In function funca")
     return a

def funcb():
    b=funca()
    print("In function funcb")
    return b

def abc():
    alpha = ["Apple","Banana","Cherry"]
    for x in alpha:
      print(x)
      if x== "Banana":
         print("Breaking now")
         print("Good bye...")
         break

i=input("Execute loop for -> ")
for t in range(int(i)):
     print("for LOOP->",i)
     i=funcb()
     abc()
     alpha = ["www.google.com","www.ndtv.com"]
     for x in alpha:
       url="start chrome " + x
       os.system(url)