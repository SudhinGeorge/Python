# Write a Python program to read first n lines of a file.

f = open("test.txt","r")
n = 0
for x in f:
    if n<3:
        print(x)
    n=n+1