import statistics

# Ex 1

list1: list[int] = []
for i in range(1, 101):
    list1.append(i)

print(list1[0])
print(list1[-1])
print(len(list1))

list2: list[int] = list1[2:12]
print(list2)

list3: list[int] = list1[79:]
print(list3)

list4: list[int] = list1[:17]
print(list4)

list5: list[int] = list1[::-1]
print(list5)

list6: list[int] = list1[1::2]
print(list6)

list7: list[int] = list1[2::3]
print(list7)

list8: list[int] = list1[6::7]
print(list8)

list9: list[int] = list1[9::10]
print(list9)

list10: list[int] = list1[-2:64:-3]
print(list10)

list1.insert(len(list1) // 2, 999)
print(list1)

list1.pop()
print(list1)

# Ex 2

height_list: list[float] = []
height: float
count_2m = 0

while True:
    height = float(input("Enter height: "))
    if height == -999:
        break
    if height < 1.6 or height > 3:
        continue
    if height > 2:
        count_2m += 1
    height_list.append(height)

print(f"Players: {len(height_list)}")
print(f"Tallest: {max(height_list)}")
print(f"Shortest: {min(height_list)}")
print(f"Average: {statistics.mean(height_list)}")
print(f"Taller than 2 meters: {count_2m}")

count_above_average = 0
avg = statistics.mean(height_list)

for temp_height in height_list:
    if temp_height > avg:
        count_above_average += 1

print(f"Taller than average: {count_above_average}")

# Ex 3

num_list: list[int] = []
num = 0
for i in range(1, 11):
    num_list.append(i * 10)

while True:
    num = int(input("Enter a number: "))
    if num == -999:
        break
    for i in range(len(num_list)):
        if num < num_list[i]:
            num_list.insert(i, num)
            break
        if num == num_list[i]:
            break
    if num > num_list[-1]:
        num_list.append(num)
    print(num_list)
