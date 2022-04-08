"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730478408"


class Simpy:
    """Produce a simplified NumPy library."""
    values: list[float]

    def __init__(self, initializer: list[float]) -> None:
        """Construct a new Simpy object given a self and initializer parameter."""
        self.values = initializer
    
    def __str__(self) -> str:
        """Produces a string representation of a Simpy object's values attribute."""
        string_representation: str = ""
        for i in range(0, (len(self.values) - 1)):
            string_representation += str(self.values[i])
            string_representation += ", "
        string_representation += str(self.values[len(self.values) - 1])
        return f"Simpy([{string_representation}])"

    def fill(self, fill_value: float, repetitions: int) -> None:
        """Fills a Simpy's values with a specific number of repeating values."""
        self.values = []
        self.values += repetitions * [fill_value]

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in the `values` attribute with range of values, like the `range` built-in function, but in terms of floats."""
        assert step != 0.0
        self.values = []
        self.values.append(start)
        while abs(start) < abs(stop - step):
            start += step
            self.values.append(start)

    def sum(self) -> float:
        """Compute and return the sum of all items in the `values` attribute."""
        return(sum(self.values))

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Overload the addition operator for use in Simpy with union types."""
        result: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] + rhs.values[i])
        else:
            for value in self.values:
                result.append(value + rhs)
        return Simpy(result)
            
    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Overload the power operator for use in Simpy with union types."""
        result: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
        else:
            for value in self.values:
                result.append(value ** rhs)
        return Simpy(result)

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Overload the equality operator for use in Simpy with union types."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        else:
            for value in self.values:
                result.append(value == rhs)
        return result

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Overload the greater than operator for use in Simpy with union types."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        else:
            for value in self.values:
                result.append(value > rhs)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overload the subscription operator for use with Simpy objects."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result: list[float] = []
            for i in range(len(rhs)):
                if rhs[i]:
                    result.append(self.values[i])
            return Simpy(result)
