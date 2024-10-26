import statistics

# CONDITIONS
# Ex 1
num = float(input("Enter a number: "))
print(num - 10 if num > 10 else num * 10)

# Ex 2
numl: list[float]=[float(input("Enter a number: ")) for _ in range(3)]
print(sum(numl) if sum(numl)>100 else "Sum is less then 100")

# Ex 3
num2 = float(input("Enter a number: ")) % 1
num3 = float(input("Enter a number: ")) % 1
print(max([num2, num3]) if num2 != num3 else "Equal")

# Ex 4
num4: int = int(input("Enter your age: "))
print(num4 if 0 < num4 < 120 else "Incorrect age")

# Ex 5
num5 = input("Enter a number: ")
print(num5[1] if 99 < int(num5) < 1000 else "Incorrect number")


# LOOPS
# Ex 6
print([n for n in range(int(input("Enter a number: ")), 0, -1)])

# Ex 7
print([n for n in range(int(input("Enter number 1: ")), int(input("Enter number 2: ")) + 1) if n % 2 == 0])

# Ex 8
print([n for n in range(1, int(input("Enter number 1: ")) + 1) if n % 3 == 0 or n % 5 == 0])

# Ex 9
print([n for n in range(1, int(input("Enter number 1: ")) + 1) if n % 7 == 0])


# DATA
# Ex 11
sumd = 0
num6 = 0
while True:
    num6 = int(input("Enter a number: "))
    if num6 == 0:
        break
    sumd += num6 if num6 < 0 else 0
print(sumd)

# Ex 12
list1: list[int] = [int(input("Enter a number: ")) for _ in range(10)]
print(list1[::-1])

# Ex 13
countp = 0
num7 = 0
while True:
    num7 = int(input("Enter a number: "))
    if num7 == 0:
        break
    if num7 <= 1:
        continue
    divider = 2
    while divider <= num7 ** 0.5:
        if num7 % divider == 0:
            break
        divider += 1
    else:
        countp += 1
print(countp)

# Ex 14
list2: list[int] = [int(input("Enter a number: ")) for _ in range(5)]
print(f"Average = {statistics.mean(list2)}, There were {sum([num > statistics.mean(list2) for num in list2])} larger then the average")

# Ex 15
num8: int = int(input("Enter number 1: "))
num9: int = int(input("Enter number 2: "))
maxn: int = max(num8, num9)
minn: int = min(num8, num9)
print(sum([1 for i in range(maxn, maxn % minn, minn * -1)]))

# CHALLENGE
# Ex 16
print("Divided by 3" if int(input("Enter a number: ")) % 3 == 0 else "Not divided by 3")

# Ex 17
num = input("Enter a string: ")
print("Flipped" if num == num[::-1] else "Not flipped")
