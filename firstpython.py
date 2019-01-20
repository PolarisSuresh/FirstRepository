#!C:\Users\Suresh\AppData\Local\Programs\Python\Python37-32\python.exe

'''
For learning print function in Python 
By Suresh
Python ver 3.7
On date 04-Nov-2018
'''

#print ("My first print in python")

#print ("Print", 1+2) 

'''
LoopCount=input("Enter number of times to print")
for i in range(int(LoopCount)):
        print("LoopCount ",i==2)
        if i==2:
          print("if condition executed")
        elif i==3:
          print("You are in second if condition")
        print("Outside if", LoopCount)
'''
def func1():
    A=1*2
    return A	

for i in range(7):
    if i==0:
       B=0
    B=B+func1()
    print("Value of B: ", B)
     
