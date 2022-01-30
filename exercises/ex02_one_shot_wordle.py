"""EX02 - Practing loops with Wordle."""

__author__ = "730478408"

secret: str = "python"

guess: str = input(f"What is your {len(secret)}-letter guess? ")

while len(guess) != len(secret):
    guess = input(f"That was not {len(secret)} letters! Try again: ")
if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")   

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"