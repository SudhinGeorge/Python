# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

num1 = int(input("Enter a number: "))

if(num1%2!=0):
    print(f"{num1} is an odd number")

else:
    print(f"{num1} is an even number")