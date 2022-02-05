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