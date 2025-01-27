number1 = int(input("Enter a number: "))
cnt = 0
for i in range(1,int(number1/2)):
    if(number1%i==0):
        cnt=cnt+1
if(cnt > 2):
    print(number1," is not prime")
else:
    print(number1," is prime")     