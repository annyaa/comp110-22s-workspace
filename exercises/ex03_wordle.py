"""EX03 - Practising funtions and loops with Wordle."""

__author__ = "730478408"


def contains_char(character_collection: str, single_character_match: str) -> bool:
    """Given two parameters, the second of length 1, indicates if the second is found anywhere in the first."""
    assert len(single_character_match) == 1
    i: int = 0
    while i < len(character_collection):
        if character_collection[i] == single_character_match:
            return True
        i += 1    
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(user_guess: str, secret_word: str) -> str:
    """Given two strings as parameters returns a string of colored emojis that indicate character matches."""
    assert len(user_guess) == len(secret_word)
    i: int = 0
    guess_emoji: str = ""
    while i < len(secret_word):
        character_guess: bool = False
        if contains_char(secret_word, user_guess[i]) == character_guess:
            guess_emoji += WHITE_BOX
        elif contains_char(secret_word, user_guess[i]) != character_guess and secret_word[i] != user_guess[i]:
            guess_emoji += YELLOW_BOX 
        else:
            guess_emoji += GREEN_BOX  
        i += 1
    return guess_emoji
      

def input_guess(expected_character_length: int) -> str:
    """Given an integer value as a parameter continually prompts the user for input until input length equals integer value entered."""
    word_guess: str = input(f"Enter a {expected_character_length} character word: ")
    while len(word_guess) != expected_character_length:
        word_guess = input(f"That wasn't {expected_character_length} chars! Try again: ")
    return word_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Your code will go here
    secret_word: str = "codes"
    i: int = 0
    turns: int = 6
    win: bool = False
    while i < turns and not win:
        print(f"=== Turn {i + 1}/{turns} ===")
        user_guess: str = input_guess(len(secret_word))
        emoji_result: str = (emojified(user_guess, secret_word))
        print(emoji_result)
        i += 1
        if user_guess == secret_word:
            win = True
    if win:
        print(f"You won in {i}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()