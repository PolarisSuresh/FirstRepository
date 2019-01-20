#!C:\Users\Suresh\AppData\Local\Programs\Python\Python37-32\python.exe

'''
For learning print function in Python 
By Suresh
Python ver 3.7
On date 25-Nov-2018
'''
#while "true":
#    print("Hello in While loop")

import os	
import time
#This function is to start chrome with google and execute a command
def exec_chrome_cmd_func():	
       for t in range(1,10):
           print("Value of t is ",t)
           if t==2:
              os.system("start chrome www.google.com")
           elif t==3:
              cmd=input("Enter Command-")
              os.system(cmd)
           elif t==5:
              break

#This function is to start chrome with google and kill based on
#command prompt input to kill
def start_kill_chrom_func():
   for t in range(1,5):
      print("Value of t is ",t)
      if t==2:
         os.system("start chrome www.google.com")
      elif t==3:
         cmd=input("Enter Command-")
         if cmd=="kill":
           print(cmd)
           os.system("taskkill /f /im chrome.exe")
           break

#This function is to start chrome with google and kill after
#sleeping for the number of seconds requested
def openchrom_killaftersleep_func():
    os.system("start chrome www.google.com")
    sleeptime=input("How long should I sleep")
    time.sleep(int(sleeptime))
    os.system("taskkill /f /im chrome.exe")
    print("Sleep over")

#This function is to execute sleep command, if the input is 5
#prints a hello message
def sleep_for_few_seconds_func():
     sleeptime=input("How long should I sleep ")
     while sleeptime=="5":
        print("Hello in While loop")

#This function is to display the files in a OS directory
def list_files_func():
  for files in os.walk('C:/Users/Suresh'):
      print(files)

#This function is to test the range function usage
def range_func():
    for i in range(1,10):
       if i==3:
          continue
       print(i)

#This function is to check the usage of list variable
def mobile_brands_list_display_func():
      mobile_brands=["apple","samsung","lenovo","oneplus1"]
      i=0
      while i < len(mobile_brands):
            print(mobile_brands[i])
            if mobile_brands[i]=="lenovo":
               print("Hello, it islenovo")
            i=i+1

#This function is to check the usage of list integer variable
def numbers_list_display_func():
      numbers=[1,2,3,4,5]
      sum=0
      for number1 in numbers:
         print("sum ",sum)
         print("numbers ",number1)
         sum=sum+number1

#This is the function you want to execute
#mobile_brands_list_display_func()