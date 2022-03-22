"""Examples of importing in python."""


from lessons import helpers

# to alias the imported function's name use the term 'as':
from lessons import helpers as hp


# import names defined globally in a module
from lessons.helpers import powerful, THE_ANSWER


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))  # Can't just print powerful(2,4) since what is defined in globals is the name of the module itself and not the specific functions it contains
    print(f"The answer: {hp.THE_ANSWER}")
    print(powerful(2, 4))
    print(THE_ANSWER)


if __name__ == "__main__":  # since calling main evaluates the function main, the name equals main in this module
    main()