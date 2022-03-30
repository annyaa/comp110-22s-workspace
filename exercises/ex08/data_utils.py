"""Dictionary related utility functions."""

__author__ = "730478408"

from csv import DictReader


# Define your functions below
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a csv rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the csv line by line
    for row in csv_reader:
        result.append(row)

    # Close that file when we;re done to free its resources
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented representation of the table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(col_table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with only the first `N` (a parameter) rows of data for each column."""
    head_result: dict[str, list[str]] = {}
    i: int = 0
    for column in col_table:
        values_list: list[str] = []
        for item in col_table[column]:
            if i < N:
                values_list.append(item)
            i += 1
        head_result[column] = values_list
        i = 0
    return head_result


def select(col_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with only a specific subset of the original columns."""
    select_result: dict[str, list[str]] = {}
    for columns in column_names:
        select_result[columns] = col_table[columns]
    return select_result


def concat(first_col_table: dict[str, list[str]], second_col_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with two column-based tables combined."""
    concat_result: dict[str, list[str]] = {}
    for column in first_col_table:
        concat_result[column] = first_col_table[column]
    for column in second_col_table:
        if column in concat_result:
            concat_result[column] += second_col_table[column]
        else:
            concat_result[column] = second_col_table[column]
    return concat_result


def count(values_list: list[str]) -> dict[str, int]:
    """Given a `list[str]`, this function will produce a `dict[str, int]` where each key is a unique value in the given list and each value associated is the _count_ of the number of times that value appeared in the input list."""
    count_result: dict[str, int] = {}
    for item in values_list:
        if item in count_result:
            count_result[item] += 1
        else:
            count_result[item] = 1
    return count_result


def filter_analysis(table_input: list[dict[str, str]], column: str, response_to_tally: str) -> dict[str, int]:
    """Split respondents into comp sci and non comp sci majors and further filter them by value."""
    major_responses: list[str] = []
    major_count: int = 0
    non_major_count: int = 0
    filter_majors: dict[str, int] = {}
    for row in table_input:
        item: str = row[column]
        major_responses.append(item)
    for response in major_responses:
        if response == response_to_tally:
            non_major_count += 1
        else:
            major_count += 1
    filter_majors["non comp sci major"] = non_major_count
    filter_majors["comp sci major"] = major_count
    return filter_majors