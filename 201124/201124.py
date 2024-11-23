# Exercise 1

tup1: tuple[int] = (99,)

tup2: tuple[int, int, int] = (77, 88, 99)


def tup_len(tup_temp: tuple) -> int:
    return len(tup_temp)
print(tup_len(tup2))


def tup_concat(tup_temp1: tuple, tup_temp2: tuple) -> tuple:
    return tup_temp1 + tup_temp2
print(tup_concat(tup2, tup1))


def tup_concat_share(tup_temp1: tuple, tup_temp2: tuple) -> tuple:
    return tuple(i for i in tup_temp1 if i in tup_temp1 and i in tup_temp2)
print(tup_concat_share(tup2, tup1))


def tup_concat_diff(tup_temp1: tuple, tup_temp2: tuple) -> tuple:
    return tuple(i for i in tup_temp1 + tup_temp2 if i not in tup_concat_share(tup_temp1, tup_temp2))
print(tup_concat_diff(tup2, tup1))


def tup_index(tup_temp1: tuple, num: int):
    return tup_temp1[num] if num < len(tup_temp1) else None
print(tup_index(tup2, 1))


def tup_reverse(tup_temp1: tuple) -> tuple:
    return tup_temp1[::-1]
print(tup_reverse(tup1))


def tup_mult(tup_temp1: tuple, num: int) -> tuple:
    return tup_temp1 * num
print(tup_mult(tup2, 3))


def tup_remove(tup_temp1: tuple, num: int):
    return tuple(i for i in tup_temp1 if i != num)
print(tup_remove(tup2, 88))


def tup_no_dup(tup_temp1: tuple) -> tuple:
    list1: list[int] = []
    for i in tup_temp1:
        if i not in list1:
            list1.append(i)
    return tuple(list1)
print(tup_no_dup((1, 2, 3, 3, 3, 4, 5, 6, 6)))


def tup_index_tup(tup_temp1: tuple, num: int):
    return tuple(i for i in range(len(tup_temp1)) if tup_temp1[i] == num)
print(tup_index_tup((1, 2, 3, 3, 3, 4, 5, 6, 6, 3), 3))


name: str = ""
score: int = 0
name_list: list[str] = []
score_list: list[int] = []

while True:
    name = input("Enter a name: ")
    if name == "done":
        break
    name_list.append(name)
while True:
    score = int(input("Enter a score: "))
    if score == -999:
        break
    score_list.append(score)

tup4: tuple = tuple(zip(name_list, score_list))
print(tup4)


# Exercise 2 - tuple is immutable while list isn't, I will use tuple when ever I don't want to change it's content.


# Exercise 3 - there are no errors because the user cleared the dictionary within the tuple but the dictionary is still there.
