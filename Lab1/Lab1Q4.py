#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

num = int(input("Enter a number: "))
i=1
a=[]

while i<=num:
    if num%i==0:
        a.append(i)
    i+=1
print(f'The list of divisors of {num} is {a}')