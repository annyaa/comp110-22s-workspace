"""EX02 - Practing loops with Wordle."""

__author__ = "730478408"

secret: str = "python"

guess: str = input("What is your 6-letter guess? ")

while len(guess) != len(secret):
    guess = input("That was not 6 letters! Try again: ")
if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")   

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"