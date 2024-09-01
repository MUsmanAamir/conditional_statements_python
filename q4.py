age = int(input("Enter your age: "))

if(age>=18):
    pak: str = input("Do you have nationality of Pakistani (yes/no): ")
    if(pak=="yes" or pak=="Yes"):
        print("You are eligible to vote. ")
    elif(pak=="no" or pak=="No"):
        print("Please obtain a valid ID to vote. ")
else:
    print("You cannot have an ID card. ")