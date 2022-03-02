"""This is the file in which I will write and implement all the function skeletons and implementations I intend to test."""

__author__ = "730478408"


def invert(values_to_invert: dict[str, str]) -> dict[str, str]:
    """Given a dictionary [str, str], returns a dictionary [str,str] that inverts the inputted keys and the values such that the keys of the input list become the values of the output list and vice versa."""
    dictionary_after_inversion: dict = {}
    for key, value in values_to_invert:
        dictionary_after_inversion[value] = key
    return dictionary_after_inversion


def favorite_color(names_and_color_inputs: dict[str, str]) -> str:
    """Given that its only parameter is a dictionary [str, str] with names of people as keys and their corresponding favorite colors as values, returns a str which is the color that appears most frequently."""


def count(counter_input_values: list[str]) -> dict[str, int]:
    """Given a list of strings as its input, returns a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    counter_generated_dictionary: dict = {}
    for counting_variable in counter_input_values:
        if counting_variable in counter_generated_dictionary:
            counter_generated_dictionary[counting_variable] += 1
        else:
            counter_generated_dictionary[counting_variable] = 1
    return counter_generated_dictionary