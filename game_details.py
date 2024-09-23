import random


def guessing_game():

    random_number = random.randint(1, 100)

    print("\n"
          "Please select the difficulty level:"
          "\n1. Easy (10 chances)"
          "\n2. Medium (5 chances)"
          "\n3. Hard (3 chances)"
          "\n")

    level = int(input("Enter level: "))
    if level == 1:
        print("Great! You have selected the Easy difficulty level."
              "\nLet's start the game!")

    elif level == 2:
        print("Great! You have selected the Medium difficulty level."
              "\nLet's start the game!")
    elif level == 3:
        print("Great! You have selected the Hard difficulty level."
              "\nLet's start the game!")
