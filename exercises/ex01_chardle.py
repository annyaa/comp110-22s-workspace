"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = 730478408

word_selection: str = input("Enter a 5-character word: ")
if len(word_selection) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character_selection: str = input("Enter a single character: ")
if len(character_selection) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character_selection + " in " + word_selection)
if character_selection == word_selection[0]:
    print(character_selection + " found at index 0")
if character_selection == word_selection[1]:
    print(character_selection + " found at index 1")
if character_selection == word_selection[2]:
    print(character_selection + " found at index 2")
if character_selection == word_selection[3]:
    print(character_selection + " found at index 3")
if character_selection == word_selection[4]:
    print(character_selection + " found at index 4")
