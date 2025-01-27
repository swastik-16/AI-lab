number1=int(input("Enter the number of items"))
first_term=0
second_term=1
while(number1>0):
    print(first_term)
    next_term=first_term+second_term
    first_term=second_term
    second_term=next_term
    number1=number1-1