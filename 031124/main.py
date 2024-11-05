import func_with_return

help(func_with_return.my_headline)

# Exercise 3
# a
num = 0

while True:
    num = int(input("Enter a number: "))
    if 0 < num < 9999:
        break

num = str(num)
print(all([num[0] == i for i in num]))

# b
range_list: list[int] = [0, 100, 200, 500,800]
discount_list: list[int] = [10, 20, 30, 40,50]
original_cost = int(input("Enter the original cost: "))
payment = original_cost
after_discount = 0


for i in range(4, -1, -1):
    after_discount += (payment - range_list[(i)]) * (100 - discount_list[i]) / 100 if original_cost > range_list[i] else 0
    payment -= (payment - range_list[(i)]) if original_cost > range_list[i] else 0
print(after_discount)

# c
a = float(input("Enter float 1: "))
b = float(input("Enter float 2: "))
c = float(input("Enter float 3: "))

print(any([a == b + c, b == a + c, c == a + b]))

# d

mila: str = input("Enter a word: ")
char_temp: str = ''
char_list: list[str] = []

while True:
    char_temp = input("Enter a char: ")
    if char_temp == '*':
        break
    char_list.append(char_temp)

print(all([i in mila for i in char_list]))
