"""Examples of classes and objects instantiation."""


class Pizza:
    """Modelling the idea of a Pizza."""

    # Attribute definitions

    size: str
    toppings: int
    extra_cheese: bool


def price(pizza: Pizza) -> float:
    """Calculate the price of a pizza."""
    total: float = 0.0
    if pizza.size == "large":
        total += 10
    else:
        total += 8.0

    total += pizza.toppings * 0.75

    if pizza.extra_cheese:
        total += 1.0

    return total


a_pizza: Pizza = Pizza()
a_pizza.size = "large"
a_pizza.toppings = 3
a_pizza.extra_cheese = False
print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${price(a_pizza)}")

class Point:

    a: Point = Point(1, -1)
    a.invert()