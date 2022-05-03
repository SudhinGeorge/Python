# Write a program that asks the user to enter their name and their age. 
# Print out a message that greets them and that tells them the year that they will turn 100 years old.


import datetime

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))



currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")

yearAt100 = int(year) + 100 - age

print(f"Hi {name}, the year you will turn 100 years old is {yearAt100}")