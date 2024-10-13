import random

# Exercise 1
list1: list[bool] = [random.choice([True, False]) for _ in range(3)]  # a
print(list1)

print(all(list1))  # b
print(any(list1))  # c
print(not any(list1))  # d
print(not all(list1))  # e
list2: list[int] = [random.randint(-2, 2) for _ in range(5)]  # f
print(list2)
print(all([i != 0 for i in list2]))  # g
print(any([i != 0 for i in list2]))  # h
print(all([i == 0 for i in list2]))  # i
print(any([i == 0 for i in list2]))  # j

# Exercise 2
string1 = "Ori Zehavi Petah-Tikva"
print(len(string1))  # a
print(string1.upper())  # b
print(string1.lower())  # c
print(string1.startswith("Ori"))  # d
print(string1.endswith("Petah-Tikva"))  # e
print(string1.split(" "))  # f
string1 = string1.replace(" ", "*")  # g
print(string1)  # g
print(string1.split("*"))  # g
print(string1.center(50, '='))  # h
print(string1[3::])  # i
print(string1[:4:])  # j
print(string1[::2])  # k
string1 = string1.replace("*", " ")  # g
string1 = string1.title()  # l
print(string1)

# Exercise 3
print(" day-fun ".strip(" "))  # a
print("hello".isalpha())  # b
print("777".isdigit())  # c
print(" ".isspace())  # d
print("".join(['N', 'I', 'N', 'J', 'A']))  # e
print("*".join(['N', 'I', 'N', 'J', 'A']))  # f
print('e' in "hELLo".lower())  # g

string2 = input("Enter text: ")
print([i for i in string2.upper() if i.isalpha()])  # h
