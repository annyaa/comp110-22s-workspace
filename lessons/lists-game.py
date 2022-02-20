"""Examples of using lists in a simple 'game'."""


from random import randint


rolls: list[int] = list()  # lhs: read as a list of integers, within square bracket they type of elements is listed rhs: create an empty list

# # rolls.append(1)  # this is a method call; append adds an item to alist specifically append(expr[T]) i.e added element must match element type declared for list
# # rolls.append(3)  # order in the list determined by order you append in code script so if 3 were written before 1, the list would be 3,1
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)

# # Access an individual item - indexing of lists starts at 0 and follows subscription notation convention. use rolls[int expresiion]
# print(rolls[0])
# print(rolls[1])

# # Access the length of/ number of items in a list
# print(len(rolls))

# # Access the last item of a list
# print(rolls[len(rolls) - 1])
# # can also set up a variable for this i.e. 
# # last_indes: int = len(rolls) -1 
# # print(rolls[last_index])

# write a code for while the last number rolled is not 1
# while rolls[len(rolls)-1] != 1:
# rolls.append(randint(1,6))
# This gives an IndexError because our ist is empty so there's an negative and therefeore invalid index. even if inddx of 0 is used an empty list has no index

# to fix this:
while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))
print(rolls)


# Remove an item from a list 'pop'; if yopu don't add an index it removes the last item from the list
rolls.pop(len(rolls) - 1)
print(rolls)

# Summing the values of our rolls

i: int = 0
sum: int = 0
while i < len(rolls):
    sum = sum + rolls[i]
i = i + 1
print(f"Total: {sum}")