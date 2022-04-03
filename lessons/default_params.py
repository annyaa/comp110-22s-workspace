"""Examples of default parameters."""


def add(x: int, y: int = 0, z: int = 0) -> int:
    # if a new param is added, it must also be assigned a default value. ie.e onece a default is specified any other additional parameter after it will have to be specified
    # thus, paremeters the user must provide should be indicated before any defined parameters are indicated in the function definition statement
    # even when default params are assigned, the user can still enter new parameter values just by simply enetering a value of the same type as the assigned value as in lines 10 and 11 below
    return x + y
    print(add(1))
    print(add(1, 2))
    print(add(1, 2, 3))