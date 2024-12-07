# Ex 8

student = {'name': 'John',
           'age': 20,
           'hobbies': ['reading', 'games', 'coding'],
           }


def print_student(students: dict[str, any]):
    for key, value in students.items():
        print(f"{key}:{value}")


print_student(student)


def add_hobby(students: dict[str, any], hobby: str):
    if hobby not in students["hobbies"]:
        students["hobbies"].append(hobby)


add_hobby(student, "tennis")
print_student(student)


def remove_hobby(students: dict[str, any], hobby: str):
    if hobby in students["hobbies"]:
        students["hobbies"].pop(students["hobbies"].index(hobby))


remove_hobby(student, "tennis")
print_student(student)

student["family_name"] = "Cena"
print_student(student)

# Ex 9
matrix = [[1, 2], [3, 4], [5, 6]]


def print_values(chart: list[list[int]]):
    for i in chart:
        for j in i:
            print(j, end=" ")


print_values(matrix)

# Ex 10
matrix2: list[list[int]] = [[0, 1, 1], [0, 1, 0], [1, 0, 0]]
print()


def print_zeroes(chart: list[list[int]]):
    count2 = 0
    for i in chart:
        for j in i:
            count2 += 1 if j == 0 else 0
    print(count2)


print_zeroes(matrix2)


# Ex 11

def find_dup(arr: list[int]) -> list[int]:
    return list(set([i for i in arr if arr.count(i) > 1]))


print(find_dup([4, 2, 34, 4, 1, 12, 1, 4]))  # I know the question said to print [4, 1], this solution is shorter


# Ex 12
def reversed_arr(arr: list[any]) -> list[any]:
    return arr[::-1]


print(reversed_arr([43, "what", 9, True, "cannot", False, "be", 3, True]))


# Ex 13
def sum_arr(list1: list[int], list2: list[int]) -> list[int]:
    return [list1[i] + list2[i] for i in range(len(list1))]


print(sum_arr([4, 6, 7], [8, 1, 9]))


# Ex 14
def check_palindrome(str1: str, str2: str):
    print(f"{str1}: {str1 == str1[::-1]}\n{str2}: {str2 == str2[::-1]}")


check_palindrome("racecar", "Java")

# Ex 15
power_of_two: int = 1
while power_of_two < 100:
    print(power_of_two)
    power_of_two *= 2

# Ex 16
counter = 900000
while counter > 50:
    print(counter)
    counter /= 2


# Ex 17
def find_repeated_strings(arr: list[str]) -> list[str]:
    duplicates: list[str] = []
    i: int = 0
    while i < len(arr):
        j: int = i + 1
        while j < len(arr):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
            j += 1
        i += 1
    return duplicates


print(find_repeated_strings(["apple", "banana", "apple", "orange", "banana", "kiwi"]))


# Ex 18
def remove_duplicates(arr: list[str]) -> list[str]:
    unique_list: list[str] = []
    i: int = 0
    while i < len(arr):
        if arr[i] not in unique_list:
            unique_list.append(arr[i])
        i += 1
    return unique_list


print(remove_duplicates(['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']))


# Ex 19
def remove_duplicates_and_skip_pete(arr: list[str]) -> list[str]:
    unique_list: list[str] = []
    i: int = 0
    while i < len(arr):
        if arr[i] != "Pete" and arr[i] not in unique_list:
            unique_list.append(arr[i])
        i += 1
    return unique_list


print(remove_duplicates_and_skip_pete(['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']))


# Ex 20
def find_successive_values(array: list[bool]):
    i: int = 0
    while i < len(array) - 1:
        if array[i] == array[i + 1]:
            return i + 1
        i += 1
    return -1


print(find_successive_values([True, False, False, True, True, False]))


# Ex 21

def get_valid_full_name():
    while True:
        full_name: str = input("Enter your full name: ").strip()
        if len(full_name.split()) == 2 and all(part.isalpha() for part in full_name.split()):
            return full_name
        else:
            print("Invalid full name.")


def get_valid_age():
    while True:
        try:
            temp_age = int(input("Enter your age: "))
            if 1 <= temp_age <= 130:
                return temp_age
            else:
                print("Invalid age.")
        except ValueError:
            print("Invalid input")


def get_valid_email():
    while True:
        temp_email: str = input("Enter your email: ")
        if "@" in temp_email:
            return temp_email
        else:
            print("Invalid email..")


f_name = get_valid_full_name()
age = get_valid_age()
email = get_valid_email()

print(f"Name: {f_name}")
print(f"Age: {age}")
print(f"Email: {email}")
