from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        """Add is a vectorized operation that applies to all items
        When rhs is a string, it is concatenated to every item in a newly established StrArray.
        """
        # Establish a result list of strings that is empty
        # loop through every item in self.items
        # Append the concatenation of item with rhs to your result list
        # After loop, return a new StrArray object constructed with result list
        result: list[str] = []
        if isinstance(rhs, str):
            for item in self.items:
                # item += rhs
                # result.append(item)
                # The above two lines of code does the same thing as the much simpler line of code below:
                result.append(item + rhs)
            # Alternative way to do this so reult is a STrArray
            # result: StrArray(list[str]) = StArray([])
            # for item in items:
            #  result.items.append(item + rhs)
            # return result
        else:
            for i in range(0, len(self.items)):
                result.append(self.items[i] + rhs.items[i])
        return StrArray(result)


first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
print(first)
print(first + "!")
print(last + "," + first)
print(first + "//" + last)