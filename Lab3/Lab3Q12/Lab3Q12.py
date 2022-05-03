# Write a Python program to write a list to a file.

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('test.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('test.txt')
print(content.read())