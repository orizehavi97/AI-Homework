import random

# Ex 1

list1: list[int] = [i for i in range(95, 106)]  # a
print(list1)
list2: list[int] = [i for i in range(10, 22, 2)]  # b
print(list2)
list3: list[bool] = random.choices([True, False], k=5)  # c
print(list3)
list4: list[int] = [random.randint(1, 100) for _ in range(10)]  # d
print(list4)
list5: list[int] = [num for num in list4 if num > 50]  # e
print(list5)
list6: list[int] = [num for num in [random.randint(1, 100) for _ in range(10)] if num > 50]  # f
print(list6)
list7: list[str] = [char1 for char1 in input("Enter a string: ") if char1 != 't' and char1 != ' ']  # g
print(list7)
list8: list[int] = [random.randint(10, 99) for _ in range(10)]  # h
print(list8)
list9: list[int] = [num % 10 for num in list8]  # g
print(list9)

# Ex 2
# a - try-except can catch exceptions for code blocks for debugging and error handling purposes.
# b - catching exceptions allows the programmer to prevent crashes and handle different types of errors based on his needs
# c -
try:
    88 / 0
except:
    print("Cant divide by 0")

# d -
try:
    raise IndexError("Invalid index")
except IndexError as e:
    print(e)

# e -
list10: list[int] = [25, 94, -14, -53]

while True:
    try:
        ind = int(input("Enter an index: "))
        if ind == -999:
            break
        print(list10[ind])

    except Exception as e:  # its possible to catch all types of errors and add them as an exception separetaly
        print(e)
        continue
