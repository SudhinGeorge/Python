# Ask the user for a string and print out whether this string is a palindrome or not

from importlib.util import LazyLoader


str1 = str(input("Enter the string: "))

str2 = ""

for i in str1:
    str2 = i + str2

if str1 == str2:
    print(f'{str1} is palindrome')

else:
    print(f"{str1} is not palindrome")