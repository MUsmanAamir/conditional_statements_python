def numberChecker(num:int)->str:
    if(num>0):
        return "Number is positive."
    elif(num<0):
        return "Number is negative."
    else:
        return "Number is zero."

number = int(input("Enter a number: "))
print(numberChecker(number))