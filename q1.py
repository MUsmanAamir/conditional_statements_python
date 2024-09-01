def evenOdd_Check(num:int)->str:
    if(num%2==0):
        return "Number is even "
    else: 
        return "Number is odd "

number:int = int(input("Enter a number: "))
print(evenOdd_Check(number))