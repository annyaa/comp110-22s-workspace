"""Example of a function that" searches through a list."""


# Define a function named contains
# Two parameters:
# 1. needle - string we're searching for
# 2. haystack - the list we're searching through
def contains(needle: str, haystack: list[str]) -> bool:
    for item in haystack:
        if item == needle:
            return True

# Algorithm:
# For each item in the haystack:
#   Test if it is equal to the needle
#       If so, return True
# After testing all items return false because not found
# Returns true if needle in haystack, false otherwise
    return False