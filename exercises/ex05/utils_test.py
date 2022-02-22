"""This is where I will carry out tets for the only_evens, sub and concat functions I write."""

__author__ = "730478408"


from utils import only_evens, sub, concat


"""Testing the only_evens function."""


def test_only_evens_empty() -> None:
    """Tests the situation where the input list is an empty list."""
    even_selector_inputs: list[int] = []
    assert only_evens(even_selector_inputs) == []


def test_only_evens_all_even_values() -> None:
    """Tests the situation where all the values in the input list are even values."""
    even_selector_inputs: list[int] = [2, 4, 6]
    assert only_evens(even_selector_inputs) == [2, 4, 6]


def test_only_evens_all_odd_values() -> None:
    """Tests the situation where all the values in the input list are odd values."""
    even_selector_inputs: list[int] = [1, 5, 3]
    assert only_evens(even_selector_inputs) == []


def test_only_evens_single_even_value_and_multiple_odd_values() -> None:
    """Tests the situation where the given input list contains one even value and several odd values."""
    even_selector_inputs: list[int] = [1, 2, 3]
    assert only_evens(even_selector_inputs) == [2]


def test_only_evens_even_integer_value_repeated_multiple_times_in_the_input_list() -> None:
    """Tests the situation where the given input list contains a single even integer value repeated multiple times."""
    even_selector_inputs: list[int] = [4, 4, 4]
    assert only_evens(even_selector_inputs) == [4, 4, 4]


def test_only_evens_many_odd_and_even_integer_values_in_the_input_list() -> None:
    """Tests the situation where the given input list contains a multiple even integer values and multiple odd integer values."""
    even_selector_inputs: list[int] = [0, 5, 7, 24, 13, 38, 21, 40, 48, 55, 100, 202, 121]
    assert only_evens(even_selector_inputs) == [0, 24, 38, 40, 48, 100, 202]


"""Testing the sub function."""


def test_sub_multiple_items_no_exceptional_case() -> None:
    """Tests the situation where the given input list contains multiple integer values and input values for both the start and end index are positive and less than the length of the input list."""
    subset_generator_inputs: list[int] = [10, 20, 30, 40]
    start_index: int = 1
    end_index: int = 3
    assert sub(subset_generator_inputs, start_index, end_index) == [20, 30]


def test_sub_negative_start_index_value_exceptional_case() -> None:
    """Tests the exceptional situation where the given input list contains multiple integer values, the input value for the start index is negative and the input value for the end index is positive and less than the length of the input list."""
    subset_generator_inputs: list[int] = [5, 10, 15, 20, 25, 30, 35]
    start_index: int = -1
    end_index: int = 5
    assert sub(subset_generator_inputs, start_index, end_index) == [5, 10, 15, 20, 25]


def test_sub_end_index_value_exceeds_input_list_length_exceptional_case() -> None:
    """Tests the situation where the given input list contains multiple integer values, the input value for the start index is positive and less than the length of the input list, and the input value for the end index is positive but greater than the length of the input list."""
    subset_generator_inputs: list[int] = [4, 9, 36, 20, 80, 180, 720]
    start_index: int = 3
    end_index: int = 12
    assert sub(subset_generator_inputs, start_index, end_index) == [20, 80, 180, 720]


def test_sub_empty() -> None:
    """Tests the situation where the given input list is empty and input values for both the start and end index are positive."""
    subset_generator_inputs: list[int] = []
    start_index: int = 1
    end_index: int = 3
    assert sub(subset_generator_inputs, start_index, end_index) == []


def test_sub_start_index_exceeds_input_list_length() -> None:
    """Tests the situation where the given input list contains multiple integer values, the input value for the start index is positive and greater than the length of the input list."""
    subset_generator_inputs: list[int] = [150, 300, 450, 600, 750]
    start_index: int = 7
    end_index: int = 10
    assert sub(subset_generator_inputs, start_index, end_index) == []


def test_sub_negative_end_index() -> None:
    """Tests the situation where the given input list contains multiple integer values, the input value for the start index is positive and less than the length of the input list, and the input value for the end index is negative."""
    subset_generator_inputs: list[int] = [150, 300, 450, 600, 750]
    start_index: int = 2
    end_index: int = -1
    assert sub(subset_generator_inputs, start_index, end_index) == []


def test_concat_two_empty_lists() -> None:
    """Tests the situation where both input lists are empty lists."""
    first_list: list[int] = []
    second_list: list[int] = []
    assert concat(first_list, second_list) == []


def test_concat_two_identical_lists() -> None:
    """Tests the situation where both input lists are identical to each other."""
    first_list: list[int] = [3, 6, 9]
    second_list: list[int] = [3, 6, 9]
    assert concat(first_list, second_list) == [3, 6, 9, 3, 6, 9]


def test_concat_two_unique_lists_of_the_same_length() -> None:
    """Tests the situation where the input lists contain unique values but are of the same length."""
    first_list: list[int] = [2, 4, 5, 8, 20]
    second_list: list[int] = [3, 8, 10, 24, 80]
    assert concat(first_list, second_list) == [2, 4, 5, 8, 20, 3, 8, 10, 24, 80]


def test_concat_two_unique_lists_of_differing_lengths() -> None:
    """Tests the situation where the input lists contain unique values and are of differing lengths."""
    first_list: list[int] = [10, 20, 30, 40]
    second_list: list[int] = [100, 200, 300, 400, 500]
    assert concat(first_list, second_list) == [10, 20, 30, 40, 100, 200, 300, 400, 500]


def test_concat_a_list_with_a_single_integer_and_an_empty_list() -> None:
    """Tests the situation where the first input list contains a single integer and the second input list is an empty list."""
    first_list: list[int] = [1000]
    second_list: list[int] = []
    assert concat(first_list, second_list) == [1000]


def test_concat_an_empty_list_and_a_list_with_a_single_integer() -> None:
    """Tests the situation where the first input list is an empty list and the second input list contains a single integer."""
    first_list: list[int] = []
    second_list: list[int] = [-5000]
    assert concat(first_list, second_list) == [-5000]


def test_concat_a_list_with_multiple_integer_values_and_an_empty_list() -> None:
    """Tests the situation where the first input list contains multiple integer values and the second input list is an empty list."""
    first_list: list[int] = [-5, -10, -15, -20]
    second_list: list[int] = []
    assert concat(first_list, second_list) == [-5, -10, -15, -20]


def test_concat_an_empty_list_and_a_list_with_multiple_integer_values() -> None:
    """Tests the situation where the first input list is an empty list and the second input list contains multiple integer values."""
    first_list: list[int] = []
    second_list: list[int] = [100, 200, 300, 400, 500]
    assert concat(first_list, second_list) == [100, 200, 300, 400, 500]