#create dictinoary and update using list
a={"key1":1,"key2":2.2}
list1=[]
for j in range (1,2):
    index = "key"+str(j)
    list1.append(a[index])
    print(list1)
    j=j+1
    	