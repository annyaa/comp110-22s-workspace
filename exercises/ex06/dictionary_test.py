"""This is where I will carry out tets for the invert, favorite_color, and count functions I write."""

__author__ = "730478408"


from dictionary import invert
import pytest


"""Testing the invert function."""


with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)
    

def test_invert_empty() -> None:
    """Tests the situation where the input dictionary is an empty dictionary."""
    values_to_invert: dict[str, str] = {}
    assert invert(values_to_invert) == {}


def test_invert_single_key_value_pair() -> None:
    """Tests the situation where the input dictionary contains a single key-vale pair."""
    values_to_invert: dict[str, str] = {'apple': 'cat'}
    assert invert(values_to_invert) == {'cat': 'apple'}


def test_invert_multiple_key_value_pairs() -> None:
    """Tests the situation where the input dictionary contains multiple key-vale pairs."""
    values_to_invert: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(values_to_invert) == {'z': 'a', 'y': 'b', 'x': 'c'}