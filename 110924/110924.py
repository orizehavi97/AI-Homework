# Exercise 1

movie_length = int(input("How many minutes are in the movie? "))
hours = movie_length // 60
minutes = movie_length % 60

print(f"Hours: {hours}, minutes: {minutes}")

# Exercise 2

for i in range(0, 11):
    print(i, end=" ")
print("")
for i in range(40, 89, 2):
    print(i, end=" ")
print("")
for i in range(77, 106, 7):
    print(i, end=" ")
print("")
for i in range(99, 65, -3):
    print(i, end=" ")
print("")

# Exercise 3.1

height: float = 0

while True:
    height = float(input("What is your height? "))
    if 0.4 < height < 2.5:
        break
    print("Wrong input")

# Exercise 3.2

a = int(input("Number 1: "))
b = int(input("Number 2: "))

if a < b:
    for i in range(a, b + 1):
        print(i, end=" ")
else:
    for i in range(a, b - 1, -1):
        print(i, end=" ")
print("")

# Exercise 3.3

pie: float = 0
count = 0

while count < 3 and pie != 3.14:
    pie = float(input("What is pie?"))
    count += 1

if count == 3:
    print("pie is 3.14")
else:
    print("you are correct")

# Exercise 3.4

num1 = 0
num2 = 0
num3 = 0

while True:
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    num3 = int(input("Third number: "))

    is_num1 = 0 <= num1 <= 10
    is_num2 = 10 <= num2 <= 60
    is_num3 = 60 <= num3 <= 100
    is_avg = num2 == (num1 + num2 + num3) / 3

    if is_num1 and is_num2 and is_num3 and is_avg:
        break

# Bonus

count = 0
age = 0

while count < 10:
    age = int(input("What is your age? "))

    if age > 18:
        print("Here's your beer")
        count += 1
