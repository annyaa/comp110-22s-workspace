"""EX02 - Practing loops with Wordle."""

__author__ = "730478408"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret: str = "python"

guess: str = input(f"What is your {len(secret)}-letter guess? ")

while len(guess) != len(secret):
    guess = input(f"That was not {len(secret)} letters! Try again: ")
if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")   


i: int = 0
guess_emoji: str = ""
while i < len(secret):
    if guess[i] == secret[i]:
        guess_emoji += GREEN_BOX
    else:
        character_guess: bool = False
        j: int = 0              
        while not character_guess and j < len(secret):
            if secret[j] == guess[i]:
                character_guess = True
            j = j + 1   
        if not character_guess:
            guess_emoji += WHITE_BOX   
        else:
            guess_emoji += YELLOW_BOX                                                                                                                              
    i = i + 1
print(guess_emoji)
