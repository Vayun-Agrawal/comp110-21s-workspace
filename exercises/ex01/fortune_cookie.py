"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730358299"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

fortune = randint(1, 4)
# Begin your solution here...
print("Your fortune cookie says ...")
if fortune < 3:
    if fortune == 1:
        print("You will ace all of your exams")
    else:
        print("You will get the job of your dreams")    
else:
    if fortune == 4:
        print("You will win a million dollars")
    else:
        print("You will win an all expenses paid vacation")
print("Now, go spread positive vibes! ")
