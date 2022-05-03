# Write a Python program to count the number of characters (character frequency) in a string

input_char = str(input("Enter a string: "))

dict = {}
for i in input_char:
    keys = dict.keys()
    if i in keys:
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)