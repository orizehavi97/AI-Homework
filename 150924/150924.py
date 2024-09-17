import random

# Exercise 1

name1 = input("What is your name?")
name2 = input("What is your name?")
name3 = input("What is your name?")
name4 = input("What is your name?")

winner = random.choice([name1,name2,name3,name4])

print("The winner is", winner)


# Exercise 2

number = random.randint(1,100)
count = 1
guess = int(input("Guess a number between 1-100: "))

while number != guess:

    if guess > number:
        print("your number is too big")
    else:
        print("your number is too small")

    guess = int(input("Guess a number between 1-100: "))
    count += 1
else:
    print(f"You guessed {count} times")


# Exercise 2.5

count = 0
sum_temp = 0
temp = 0

while count < 5:
    temp = int(input(f"Temperature #{count + 1}: "))
    if -50 <= temp <= 45:
        sum_temp += temp
        count += 1
    else:
        print("Wrong temperature")
else:
    print(f"The average temperature is: {sum_temp/count}")


# Exercise 3.1

x = int(input("Choose a number: "))

for i in range(1, x + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print("")

for i in range(x - 1, 0, -1):
    for j in range (1, i + 1):
        print(j, end=" ")
    print("")

# Exercise 3.2

y = int(input("Choose a number: "))
str1 = ""
for i in range(1, y + 1, 2):
    for j in range(1, i + 1):
        str1 += "*"
    print(f"{str1: ^10}", end="")
    print("")
    str1 = ""


# Exercise 4

num = 7
count = 0

while num % 7 == 0:
    num = int(input("num: "))
    count += 1
    if num % 11 == 0:
        break
else:
    print(count)

# Exercise 5

a = int(input("Enter a number: "))

if a % 15 == 0:
    print("Fizz Buzz")
elif a % 5 == 0:
    print("Fizz")
elif a % 3 == 0:
    print("Buzz")
else:
    print("Wrong number")