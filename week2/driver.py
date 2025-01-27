import random
import yoursearch
import yoursort
list=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    list.append(random.randint(1,100))
print(list)
print("Enter 1 for linear search")
print("Enter 2 for binary search")
print("Enter 3 for bubble sort")
print("Enter 4 for selection sort")
print("Enter 5 for insertion sort")
number=int(input("Enter a number:"))
while(True):
    if(number==1):
        key=int(input("Enter the key you want to search for: "))
        yoursearch.linear(list,key)
    elif(number==2):
        key=int(input("Enter the key you want to search for: "))
        yoursearch.binary(list,key)
    elif(number==3):
        print("Original list")
        print(list)
        yoursort.bubble(list)
        print("Sorted list")
        print(list)
    elif(number==4):
        print("Original list")
        print(list)
        yoursort.insertion(list)
        print("Sorted list")
        print(list)
    elif(number==5):
        print("Original list")
        print(list)
        yoursort.selection(list)
        print("Sorted list")
        print(list)
    else:
        break
