# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right

import random

random_num = random.randrange(1, 10)
guess_num = int(input('Guess a number between 1 and 9: '))

if random_num > guess_num:
    print("Guessed too low")

elif random_num < guess_num:
    print("Guessed too high")

else:
    print("Guessed right")

print(random_num)