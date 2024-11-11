import random
import statistics

# Exercise 1
list1: list[int] = [random.randint(1, 100) for _ in range(50)]
print(list1)

# a
print(list(filter(lambda x: x > 50, list1)))

# b
print(list(filter(lambda x: x % 7 == 0, list1)))

# c
print(list(filter(lambda x: 9 < x < 100, list1)))

# d
print(list(filter(lambda x: x % 10 == x // 10 and 9 < x < 100, list1)))

# e
print(list(filter(lambda x: x % 9 == 0, list1)))

# f
print(list(filter(lambda x: x > statistics.mean(list1), list1)))

# g
print(list(filter(lambda x: x > max(list1) / 2, list1)))


# Exercise 2
list2: list[str] = ["Grand Theft Auto V", "Fortnite", "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]
print(list2)
# a
print(list(filter(lambda word: len(word) > 8, list2)))

# b
print(list(filter(lambda word: str(word).upper()[0] == 'F', list2)))

# c
print(list(filter(lambda word: str(word).count(' ') == 1, list2)))

# d
print(list(filter(lambda word: 'v' in str(word).lower(), list2)))


# Exercise 3
list3: list[int] = [random.randint(-50, 50) for _ in range(20)]
print(list3)

# a
print(list(map(lambda x: x ** 3, list3)))

# b
print(list(map(lambda x: int(str(x)[-1]), list3)))

# c
print(list(map(lambda x: f"{x * 9 / 5 + 32:.1f}", list3)))

# d
print(list(map(lambda x: 'positive' if x > 0 else ('negative' if x != 0 else 0), list3)))


# Exercise 4
list4: list[str] = ["Mango", "Orange", "Banana", "Apple", "Strawberry", "Pineapple", "Grapes", "Watermelon"]
print(list4)

# a
print(list(map(lambda word: word[::-1], list4)))

# b
print(list(map(lambda word: word[0], list4)))

# c
print(list(map(lambda word: str(word).upper(), list4)))

# d
print(list(map(lambda word: word[len(word) // 2], list4)))

# e
print(list(map(lambda word: word + '!' if str(word[-1]).lower() == 's' else word, list4)))


# Exercise 5
# 'global' allows you to indicate that a variable refers to a globally scoped variable, rather than creating a new local variable
# Using the global keyword inside a function can lead to code that's harder to debug and maintain and will require significant restructuring in the future
# The code will fail because the funtion 'foo' doesnt know the variable 'x' due to its scope
