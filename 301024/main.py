# Exercise 1

import my_func
from my_func import print_stars

for _ in range(5):
    my_func.print_stars()  # i
    print_stars()  # ii

help(my_func)

# Exercise 2
# a
full_class = 30
students = 103

print(f"There will be {students // full_class} full classes and {students % full_class} students in the last class")

students = input("How many students are there? ")

print(f"There will be {students // full_class} full classes and {students % full_class} students in the last class")

# b
num = ''

while True:
    try:
        num = input("Enter a number between 10 and 99: ")
        if int(num) > 99 or int(num) < 10:
            print("Wrong number")
            continue
        num = num[::-1] if int(num[0]) < int(num[1]) else num
        break
    except ValueError:
        print("Not a number")
print(num)

# c
for i in range(2, 200):
    divider = 2
    while divider <= i ** 0.5:
        if i % divider == 0:
            break
        divider += 1
    else:
        print(i, end=' ')

# d
str1 = ''
count_answers: list[int] = [0, 0, 0, 0]

while True:
    str1 = input("Enter an answer: ")
    if str1 == 'x':
        break
    match (str1):
        case 'a':
            count_answers[0] += 1
        case 'b':
            count_answers[1] += 1
        case 'c':
            count_answers[2] += 1
        case 'd':
            count_answers[3] += 1
        case _:
            print("Invalid answer")
            continue
str1 = 'abcd'
for i in range(4):
    print(f"{count_answers[i]} answered '{str1[i]}', ")
print(
    f"Most popular answer: '{str1[count_answers.index(max(count_answers))]}', Least popular answer: '{str1[count_answers.index(min(count_answers))]}'")
