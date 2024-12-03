
# Exercise 1
for i in range(12, 25):
    print(i, end=" ")
print()
# Exercise 2
for i in range(7, 32, 2):
    print(i, end=" ")
print()
# Exercise 3
for i in range(10, -20, -2):
    print(i, end=" ")
print()
# Exercise 4
for i in range(1, 46):
    match i:
        case i if i % 3 == 0 and i % 5 == 0:
            print(f"FizzBuzz {i}", end=" ")
        case i if i % 3 == 0:
            print(f"Fizz {i}", end=" ")
        case i if i % 5 == 0:
            print(f"Buzz {i}", end=" ")
print()
# Exercise 5
def sum_list(list1:list[int])->int:
    sum1:int=0
    for num in list1: sum1+=num
    return sum1
print(sum_list([1,2,3]))

# Exercise 6
def del_students_prop(list2:list[dict[any]], prop: str):
    for i in range(len(list2)-1):
        list2[i][prop] = "" # wasn't clear if you wanted to remove the key or the value, I chose the value.

def print_prop(list2:list[dict[any]]):
    for student in list2:
        for prop in student.keys():
            print(f"{prop} : {student[prop]}") # wasn't clear what needed to be printed, I printed every student's details.

def sort_array(list2:list[dict[any]]):
    return list(sorted(list2, key=lambda student: student["age"],reverse=True))

# Ex7
our_pets = [{"animal_type": "cat",
             "names":["Meowzer","Fluffy","Kit-Cat"]},
            {"animal_type":"dog",
             "names":["Spot","Bowser","Frankie"]}
            ]
def print_cat(list1: list[dict[str, any]]):
    for item in list1:
        if item["animal_type"] == "cat":
            print("animal_type: cat")

print_cat(our_pets)

def print_animal_names(list1: list[dict[str, any]], animal_type: str):
    for item in list1:
        if item["animal_type"] == animal_type:
            for name in item["names"]:
                print(name)

print_animal_names(our_pets, "dog")

def add_animal_name(list1: list[dict[str, any]], animal_name: str):
    for animal in list1:
        if animal_name not in animal["names"]:
            animal["names"].append(animal_name)

add_animal_name(our_pets, "David")
print(our_pets)