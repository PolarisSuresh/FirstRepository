#!C:\Users\Suresh\AppData\Local\Programs\Python\Python37-32\python.exe

'''
For learning list data type in Python 
By Suresh
Python ver 3.7
On date 23-Dec-2018
'''
import request
#a.append(6)
#a.extend([7,8])
#print(a.count(2))
#a.clear()
#b=a.copy()  # will copy complete list from a into b
#a.pop() #removes the last value in list
#a.remove(3) #removes specified value from the list
#a.reverse() #reverses the values in the list
#a.insert(1,3) #inserts argument 2 in the place mentioned in arg 1
#a.sort() # to sort the values in ascending order in list
#b=index(4) #will return 3
req=request.get("http://www.rediff.com")
print(req)
a=[1,2.5,1+3j,"abc",3]
print(a)
for i in a:
    print(i)
print(a)
