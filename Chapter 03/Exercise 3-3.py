# Entering the age
userAge = int(input("Please enter your age: "))

if userAge <= 0:
    print("Enter a valid age!")
elif userAge <= 1:
    print("You are an infant")
elif userAge < 13:
    print("You are an child")
elif userAge < 20:
    print("You are an teenager")
elif userAge >= 20:
    print("You are an adult")
else:
    print("Enter a valid age!")
