"""This is an adventure game that involves travelling through the wilderness!"""
"""While loop for above and beyond is in main function"""

from random import randint

__author__ = "730358299"

player: str = str("x")

points: int = int(0)

health: int = int(100)

emoji: str = str("\U0001F622")


def main() -> None:
    """Main function that begins the game!"""
    greet()
    print(f"Welcome { player } ! Your options are: 1)Begin Ocean Adventure 2)Begin Mountain Adventure 3)Quit")
    choice = int(input("Enter your choice as the number 1, 2, or 3: "))
    if choice < 3:
        while health > 0:
            if choice == 1:
                ocean()
            if choice == 2:
                mountains()
    end()
    return None


def greet() -> None:
    """Function to greet the player."""
    print("Welcome to Survival, an adventure game that will test your wilderness survival skills!")
    print("Every encounter you survive awards you adventure points!")
    global player
    player = str(input("Please enter your name to continue: "))
    return None


def mountains() -> None:
    """This function represents the mountain game path!"""
    print("You are attacked by a bear, what do you do?")
    print("Options: 1) Use a sword 2) Run away")
    global points
    global health
    response = int(input("Enter 1 or 2 for your choice: "))
    run = randint(1, 2)
    fight = randint(1, 2)
    if response == 2:
        if run == 1:
            print("You escape successfully, you gain 5 adventure points and lose no health!")
            points = points + 5
        else:
            print("You are too slow and the bear wounds you, you lose 50 health")
            health = health - 50
    else:
        if fight == 1:
            print("You kill the bear! You gain 10 adventure points")
            points = points + 10
        else:
            print("You wound it but he wounds you before you get away. Lose 25 health and gain 5 adventure points.")
            health = health - 25
            points = points + 5
    return None


def ocean() -> None:
    """This function represents the ocean game path!"""
    print("You are attacked by a tiger shark, what do you do?")
    print("Options 1) Use a harpoon 2) Swim away")
    response = int(input("Enter 1 or 2 for your choice: "))
    harpoon = randint(1, 2)
    swim = randint(1, 2)
    global points
    global health
    if response == 2:
        if swim == 2:
            print("You escape successfully, you gain 5 adventure points and lose no health!")
            points = points + 5
        else:
            print("You are too slow and the tiger shark bites you. Lose 50 health.")
            health = health - 50
    else:
        if harpoon == 2:
            print("Your harpoon is right on target and kills the tiger shark! Gain 10 adventure points!")
            points = points + 10
        else:
            print("You miss but wound the shark, however, he bites you. Lose 25 health, gain 5 points")
            health = health - 25
            points = points + 10
    return None


def end() -> None:
    """Ends the game!"""
    global health
    global points
    prhealth = str(health)
    prpoints = str(points)
    if health <= 0:
        print(f"You have run out of health and died.{emoji} Thank you for playing! You ended with {prpoints} points!")
    else:
        print(f"Thank you for playing! You ended with {prhealth} health and {prpoints} points!")
    return None


if __name__ == "__main__":
    main()
