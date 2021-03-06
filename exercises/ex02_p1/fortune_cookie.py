"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730358299"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie() -> str:
    """Fortune Cookie Function!"""
    fortune = randint(1, 4)
    if fortune < 3:
        if fortune == 1:
            return("You will ace all of your exams")
        else:
            return("You will get the job of your dreams")    
    else:
        if fortune == 4:
            return("You will win a million dollars")
        else:
            return("You will win an all expenses paid vacation")


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
