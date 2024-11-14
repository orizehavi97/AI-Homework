import random
import statistics

# Exercise 1
# a

list1: list[str] = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]
print(list(sorted(list1, key=lambda w: len(w))))
print(list(sorted(list1, key=lambda w: w.count(' '))))
print(list(sorted(list1, key=lambda w: w[-1])))
print(list(sorted(list1, key=lambda w: w[::-1])))
print(list(sorted(list1, key=lambda w: w.count('a'))))

# a.f
list1 = [["Tokyo", 5706, "Asia"], ["New York", 5690, "North America"], ["Paris", 2050, "Europe"],
         ["London", 2240, "Europe"], ["Sydney", 8780, "Australia"], ["Dubai", 1300, "Asia"], ["Shanghai", 4920, "Asia"]]
print(list(sorted(list1, key=lambda w: w[1])))
print(list(sorted(list1, key=lambda w: w[1], reverse=True)))
print(list(sorted(list1, key=lambda w: w[2])))
print(list(sorted(list1, key=lambda w: (w[2], w[1]))))

# b

list2: list[int] = [random.randint(1, 100) for _ in range(50)]
# print(list2)
print(list(sorted(list2, key=lambda num: num)))
avg = int(statistics.mean(list2))
# print(avg)
print(list(sorted(list2, key=lambda num: ((avg - num) ** 2) ** (0.5))))

# Exercise 2
# a
text: str = "This chocolate cake is rich, moist, and full of delicious chocolate flavor. To make the cake, you will need chocolate, flour, sugar, eggs, and butter. After baking the chocolate cake, let the cake cool before adding the chocolate frosting."
text = "".join([i for i in text if i != ',' and i != '.'])
print(text)
max_count: int = 0
max_word: str = ""
dict1: dict[str, int] = {}
for word in text.lower().split():
    if word in dict1.keys():
        dict1[word] += 1
        if max_count < dict1[word]:
            max_count = dict1[word]
            max_word = word
    else:
        dict1[word] = 1
print(dict1)
print(max_word)

# b
text = "".join([i for i in text if i != ' '])
print(text)
min_count: int = 99
min_char: str = text[0].upper()
dict1: dict[str, int] = {}
for char in text.upper():
    if char in dict1.keys():
        dict1[char] += 1
    else:
        dict1[char] = 1
for char in text.upper():
    if dict1[char] < min_count:
        min_char = char
        min_count = dict1[char]

print(dict1)
print(min_char)

# Exercise 3
dict2: dict[int, int] = {}
for i in range(1, 21):
    dict2[i] = i ** 3
# print(dict2)
num: int = int(input("Enter a number: "))
print(dict2[num] if num in dict2.keys() else "Not exist")
