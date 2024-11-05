import statistics

def my_ascending(x: int, y: int):
    print(f"{x}, {y}" if x < y else f"{y}, {x}")

my_ascending(-12,7)

def my_details(mahrozet:str):
    print(mahrozet[0], mahrozet[(len(mahrozet)//2)], mahrozet[-1])

my_details("ai is the best")

def say_bool(bool1:bool):
    print("yes" if bool1 else "no")

say_bool(True)
say_bool(False)

def print_zugi(list1: list[int]):
    print(["even" if i % 2 == 0 else "odd" for i in list1])

print_zugi([5,3,2,10,15,14,14])

def my_statistics(list2: list[int]):
    print(max(list2))
    print(min(list2))
    print(len(list2))
    print(statistics.mean(list2))

num = 0
list3: list[int] = []
while True:
    num = int(input("Enter a number: "))

    if num == -99:
        break

    if num > 100 or num < 0:
        continue

    list3.append(num)

my_statistics(list3)