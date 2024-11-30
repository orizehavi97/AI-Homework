# Exercise 1

def check_parentheses_validity(s: str) -> bool:
    open_parentheses: list[str] = []
    parentheses_dict: dict[str, str] = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in parentheses_dict.values():
            open_parentheses.append(char)
        elif char in parentheses_dict.keys():
            if open_parentheses and open_parentheses[-1] == parentheses_dict[char]:
                open_parentheses.pop()
            else:
                return False
    return not open_parentheses


print(check_parentheses_validity("{()}[]"))


# Exercise 2

def remove_duplicates(list1: list[int]) -> list[int]:
    num: int = 1
    while num < len(list1):
        for i in range(num, len(list1)):
            if list1[i] == list1[i - 1]:
                list1[i - 1] = 0
                num += 1
        num += 1
    return [i for i in list1 if i != 0]


print(remove_duplicates([1, 1, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 99]))


# Exercise 3

def sort_two_lists_into_one(list1: list[int], list2: list[int]) -> list[int]:
    temp_list: list[int] = [list1.pop(0) if list1[0] < list2[0] else list2.pop(0) for _ in
                            range(len(list1) + len(list2)) if list1 and list2]
    if list1:
        temp_list.append(list1.pop())
    else:
        temp_list.append(list2.pop())
    return temp_list


print(sort_two_lists_into_one([1, 2, 4], [1, 3, 4]))
