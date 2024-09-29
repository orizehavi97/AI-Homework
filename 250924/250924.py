# Exercise 1

temp_list: list[float] = []
temp: float

while True:
    temp = float(input("Enter the temperature: "))
    if temp == -999:
        break
    if not -50 <= temp <= 50:
        continue
    temp_list.append(temp)

temp_list.extend([-20.0,39.1,18.5])

# extend has no return value whilst '+' has a return value

if temp_list:
    print(f"Max: {max(temp_list)}")
    print(f"Min: {min(temp_list)}")

else:
    print("List is empty")

print(18.5 in temp_list)

count_minus_20 = temp_list.count(-20.0)

if temp_list:
    print(f"Average temperature: {sum(temp_list / len(temp_list))}")

else:
    print("List empty")

for temp1 in temp_list:
    print(temp1)

print(temp_list.index(39.1))

del temp_list[0]

del temp_list[::2]

if 18.5 in temp_list:
    temp_list.remove(18.5)

# if the value isn't a part of the list an exception will be thrown

temp_last = temp_list.pop()

copy_temp_list = temp_list.copy()
copy_temp_list.sort()

copy2_temp_list = temp_list.copy()
copy2_temp_list.sort(reverse=True)

# Exercise 2

num = 0
num_list: list[int] = []

while True:
    num = int(input("Enter a number between 0-10: "))
    if num == -999:
        break
    if not 0 <= num <= 10:
        continue
    num_list.append(num)

    print("Statistics: ", end="")
    for i in range(11):
        if num_list.count(i) > 0:
            print(f"[{i}]: {num_list.count(i)}", end=" ")
    print()

# Exercise 3

num = 0
index_list: list[int] = []
SENTINEL = 10

for _ in range(SENTINEL + 1):
    index_list.append(0)

while True:
    num = int(input("Enter a number between 0-10: "))
    if num == -999:
        break
    if not 0 <= num <= 10:
        continue
    index_list[num] += 1

    print("Statistics: ", end="")
    for i in range(SENTINEL+1):
        if index_list[i] > 0:
            print(f"[{i}]: {index_list[i]}", end=" ")
    print()

# yes, SENTINEL = 100.