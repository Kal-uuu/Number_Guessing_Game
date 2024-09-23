from game_details import guessing_game

print("Welcome to the Number Guessing Game! 😊🎉✨")
print("I'm thinking of a number between 1 and 100.🤔"
      "\n"
      "\nRULES:"
      "\n1. You have a number chances to guess the correct number.😁"
      "\n2. Your number of guesses depends on the difficulty of your choice.😉\n"
      "\nGood Luck!😁")

understood = input("Type [OK] to play game: ")

if understood == "OK":
    guessing_game()
