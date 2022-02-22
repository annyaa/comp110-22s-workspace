"""This is the file in which I will write and implement all the function skeletons and implementations I intend to test."""

__author__ = "730478408"


def only_evens(even_selector_inputs: list[int]) -> list[int]:
    """Given a list of ints, returns a list containing only the elements of the input list that were even."""
    even_values_list: list[int] = []
    for x in even_selector_inputs:
        if x % 2 == 0:
            even_values_list.append(x)
    return even_values_list


def sub(subset_generator_inputs: list[int], start_index: int, end_index: int) -> list[int]: 
    """Given a list of ints, a start index, and an end index (not inclusive), generates a List which is a subset of the given list, between the specified start index and the end index - 1."""
    subset_elements_list: list[int] = subset_generator_inputs[start_index: end_index]
    if start_index < 0:
        subset_elements_list = subset_generator_inputs[0: end_index]
    if end_index > len(subset_generator_inputs):
        end_index = len(subset_generator_inputs) 
        subset_elements_list = subset_generator_inputs[start_index: end_index]
    if len(subset_generator_inputs) == 0:
        subset_elements_list = []
    if start_index > len(subset_generator_inputs):
        subset_elements_list = []
    if end_index <= 0:
        subset_elements_list = []
    return subset_elements_list 


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Given two lists of integers as input values, generates a list containing all elements of the first list, followed by all elements of the second list without modifying or mutating any element of either list."""
    final_list: list[int] = []
    if first_list == [] and second_list == []:
        final_list = []
    elif first_list == [] and second_list != []:
        final_list = second_list
    elif first_list != [] and second_list == []:
        final_list = first_list
    else:
        for x in first_list:
            final_list.append(x)
        for y in second_list:
            final_list.append(y)
    return final_list
