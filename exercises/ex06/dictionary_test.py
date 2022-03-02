"""This is where I will carry out tets for the invert, favorite_color, and count functions I write."""

__author__ = "730478408"


from dictionary import invert, count, favorite_color
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


"""Testing the invert function."""


def test_count_empty() -> None:
    """Tests the situation where the input list is an empty list."""
    collection_to_count: list[str] = []
    assert count(collection_to_count) == {}


def test_count_single_item() -> None:
    """Tests the situation where the input list contains just one item."""
    collection_to_count: list[str] = ["Ann"]
    assert count(collection_to_count) == {'Ann': 1}


def test_count_many_strings_with_single_recurrence() -> None:
    """Tests the situation where the input list contains many items but each item occurs only once."""
    collection_to_count: list[str] = ["Ann", "Yaa", "Safo", "Nana", "Edwin"]
    assert count(collection_to_count) == {'Ann': 1, "Yaa": 1, "Safo": 1, "Nana": 1, "Edwin": 1}


def test_count_single_item_recurring_multiple_times() -> None:
    """Tests the situation where the input list contains one item that recurs five times."""
    collection_to_count: list[str] = ["Ann", "Ann", "Ann", "Ann", "Ann"]
    assert count(collection_to_count) == {'Ann': 5}


def test_count_mix_of_multiple_and_single_recurrences() -> None:
    """Tests the situation where the input list contains some items that occur once and others that recur multiple times."""
    collection_to_count: list[str] = ["Ann", "Yaa", "Safo", "Nana", "Safo", "Edwin", "Safo", "Esi", "Nana", "Tetteh"]
    assert count(collection_to_count) == {'Ann': 1, 'Yaa': 1, 'Safo': 3, 'Nana': 2, 'Edwin': 1, 'Esi': 1, 'Tetteh': 1}


def test_count_multiple_items_recurring_multiple_times() -> None:
    """Tests the situation where the input list contains multiple items that recur multiple times."""
    collection_to_count: list[str] = ["Ann", "Nana", "Safo", "Ann", "Ann", "Safo", "Safo", "Nana", "Ann", "Safo", "Nana", "Nana", "Safo"]
    assert count(collection_to_count) == {'Ann': 4, 'Nana': 4, 'Safo': 5}


"""Testing the favorite_color function."""


def test_favorite_color_single_person_single_color() -> None:
    """Tests the situation where the input dictionary comprises one name and one color."""
    name_and_color_tracker: dict[str, str] = {'Ann': 'pink'}
    assert favorite_color(name_and_color_tracker) == 'pink'


def test_favorite_color_multiple_people_like_a_single_color() -> None:
    """Tests the situation where the input dictionary comprises many people who like one color."""
    name_and_color_tracker: dict[str, str] = {'Ann': 'pink', 'Yaa': 'pink', 'Safo': 'pink'}
    assert favorite_color(name_and_color_tracker) == 'pink'


def test_favorite_color_one_color_appears_multiple_times() -> None:
    """Tests the situation where the input dictionary has one color liked by multiple people."""
    name_and_color_tracker: dict[str, str] = {'Marc': 'yellow', 'Ezri': 'blue', 'Kris': 'blue'}
    assert favorite_color(name_and_color_tracker) == 'blue'


def test_favorite_color_frequencies_of_different_colors_are_equal() -> None:
    """Tests the situation where there is a tie for most popular color and a correctly implemented function should return the color that appeared in the dictionary first."""
    name_and_color_tracker: dict[str, str] = {'Ann': 'pink', 'Yaa': 'pink', 'Marc': 'yellow', 'Ezri': 'blue', 'Kris': 'blue'}
    assert favorite_color(name_and_color_tracker) == 'pink'