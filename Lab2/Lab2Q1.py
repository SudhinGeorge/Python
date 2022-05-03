# Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.

from ntpath import join
import random
x = ['a','e','i','o','u']
char_list = []



for numOfStrings in range(120):
    random.shuffle(x)
    randomString = ''.join(x)

    if randomString in char_list:
        pass
    
    else: 
        char_list.append(randomString)
        numOfStrings = len(char_list)
        
        

print(char_list)