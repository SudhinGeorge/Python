# Write a Python program to read a file line by line store it into an array.

content_array = []
with open("test.txt") as f:
    for line in f:
        content_array.append(line)
    print(content_array)