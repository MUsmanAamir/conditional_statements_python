number = int(input("Enter a number: "))

if(number%2==0 and number%3==0):
    print("Number is dvisible by both 2 and 3")
elif(number%2==0):
    print("Number is dvisible by 2")
elif(number%3==0):
    print("Number is dvisible by 3")
elif(number%2!=0 and number%3!=0):
    print("Number is not dvisible by both 2 and 3")

