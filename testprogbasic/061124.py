# Test 1 - 06.11.24 - Ori Zehavi
import statistics


# Conditions
# 1
first_float: float = float(input("Enter the first float: "))
second_float: float = float(input("Enter the second float: "))
print(min([first_float, second_float]))
print(min([first_float, second_float]))
print(min([first_float, second_float]))

# 2
number1: int = int(input("Enter first number: "))
number2: int = int(input("Enter second number: "))
print(f"The average is: {statistics.mean([number1, number2])}")

# 3
number1: int = int(input("Enter first number: "))
number2: int = int(input("Enter second number: "))
number3: int = int(input("Enter third number: "))
print(f"The biggest number is: {max([number1, number2, number3])}")

# 4
movie_length: int = int(input("Enter the movie's length: "))
print(f"The movie is {movie_length // 60} hours and {movie_length % 60} minutes long")

# 5
number: str = input("Enter a number: ")
try:
    print(f"The last digit is: {number[-1]}" if 999 < int(number) < 10000 else "Invalid input")
except ValueError:
    print("Not a number")

# 6
number: str = input("Enter a number: ")
try:
    print(f"The last digit is: {number[-2]}" if 999 < int(number) < 10000 else "Invalid input")
except ValueError:
    print("Not a number")

# 7
two_digit_number = input("Enter a two digit number: ")
try:
    print(f"The sum of both digits is: {int(two_digit_number[0]) + int(two_digit_number[1])}" if 9 < int(
        two_digit_number) < 100 else "Invalid input")
except ValueError:
    print("Not a number")

# 8
two_digit_number2 = input("Enter a two digit number: ")
try:
    print(f"The flipped number is: {two_digit_number2[::-1]}" if 9 < int(two_digit_number2) < 100 else "Invalid input")
except ValueError:
    print("Not a number")

# 9
try:
    number1: int = int(input("Enter a number: "))
    print("even" if number1 % 2 == 0 else "odd")
except ValueError:
    print("Not a number")

# 10
range_list: list[int] = [0, 6000, 12000, 18000, 25000, 35000, 50000]
precentage_list: list[int] = [0, 10, 20, 30, 40, 45, 51]
original_paycheck = int(input("Enter the original cost: "))
paycheck = original_paycheck
after_tax = 0

for i in range(6, -1, -1):
    after_tax += (paycheck - range_list[(i)]) * (100 - precentage_list[i]) / 100 if original_paycheck > range_list[
        i] else 0
    paycheck -= (paycheck - range_list[(i)]) if original_paycheck > range_list[i] else 0
print("Tax:", original_paycheck - after_tax)

# 11
try:
    age = int(input("Enter your age: "))
    height = int(input("Enter your height: "))
    eligibility: list[bool] = [7 < age < 19 and height > 115, age > 18 and height > 100]
    print(f"You are eligible" if any(eligibility) else "You are not eligible")
except ValueError:
    print("Not a number")

# Loops
# 1
top: int = int(input("Enter a number: "))
print([i for i in range(1, top + 1)])

# 2
number1: int = int(input("Enter a number: "))
number2: int = int(input("Enter another number: "))
print([i for i in range(min([number1, number2]), max([number1, number2]) + 1)])

# 3
n: int = int(input("Enter a natural number: "))
print([i for i in range(0, n + 1, 2)])

# 4
max_num: int = int(input("Enter a natural number: "))
den: int = int(input("Enter another natural number: "))
print([i for i in range(den, max_num + 1, den)])

# Data
# 1
number: int = 0
SENTINEL: int = -99
numbers_sum: int = None
while True:
    number = int(input("Enter a number: "))
    if number == SENTINEL:
        break
    if numbers_sum is None:
        numbers_sum = 0
    numbers_sum += number
print(numbers_sum)

# 2
number: int = 0
number_list: list[int] = []
while True:
    number = int(input("Enter a number: "))
    if number <= 0:
        break
    number_list.append(number)
print(None if number_list == [] and number == -99 else f"Max: {max(number_list)}, Min: {min(number_list)}")

# 3
number_list: list[int] = [int(input("Enter a number: ")) for _ in range(5)]
print(number_list.index(max(number_list)) + 1)

# 4
x: int = int(input("Enter a number: "))
y: int = int(input("Enter another number: "))

print(f"x * y = {sum([x for _ in range(y)])}")

# 5
x: int = int(input("Enter a number: "))
y: int = int(input("Enter another number: "))
power_of: int = 1
for i in range(y):
    power_of = power_of * x
print(power_of)

# 6
number: int = int(input("Enter a number: "))
digit: int = int(input("Enter a digit: "))
flag: bool = False
while number != 0:
    if number % 10 == digit:
        flag = True
        break
    number = number // 10
print(flag)

# 7
number1: int = int(input("Enter first number: "))
number2: int = int(input("Enter second number: "))
biggest_divider: int = 0
for i in range(1, min(number1, number2)):
    if number1 % i == 0 and number2 % i == 0:
        biggest_divider = i
print(biggest_divider)

# 8
number1: int = int(input("Enter a number: "))
divider: int = 2
flag: bool = True
while divider <= number1 ** 0.5:
    if number1 % divider == 0:
        flag = False
        break
    divider += 1
print(flag)

# Complex loops
# 1
card: int = 0
card_list: list[int] = []
flag: bool = False
counter: int = 0
while counter < 12:
    try:
        card = int(input(f"Temperature number {counter + 1}: "))
    except ValueError:
        print("Invalid input")
        continue
    if card < -5 or card > 40:
        print("Wrong data")
        break
    if flag and card == 0:
        continue
    if card == 0:
        flag = True
    else:
        flag = False
    card_list.append(card)
    counter += 1
else:
    print("Correct data")
    print("Average temp:", statistics.mean(card_list))
    print("Max temp:", max(card_list))
    print("Min temp:", min(card_list))

# 2
subject: str = input("Enter a subject for vote: ")
code_input: int = 0
count_code: int = 0
code_list: list[int] = []

while count_code < 44:
    try:
        code_input = int(input(f"Vote number #{count_code + 1}: "))
    except ValueError:
        print("Invalid input")
    if code_input == 4:
        print("Veto from country number:", count_code + 1)
        break
    if code_input > 4 or code_input < 1:
        continue
    code_list.append(code_input)
    count_code += 1
else:
    print(f"Favor: {code_list.count(1)}, object: {code_list.count(2)}, neutral: {code_list.count(3)}")
    print(f"First favor country {code_list.index(1) + 1}" if 1 in code_list else "No favor")
    print(f"Last object country {44 - code_list[::-1].index(2)}" if 2 in code_list else "No object")
