# Exercise 1

# User 1
print("User 1 details: ")
id = input("Enter your ID: ")
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
height = float(input("Enter your height: "))
year = int(input("Enter your year of birth: "))

string1 = f"\nUser1 - #id: {id:<10} name: {lastName:<7} , {firstName:<7} height: {height:<5} year-of-birth: {year:<5}"

# User 2
print("User 2 details: ")
id = input("Enter your ID: ")
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
height = float(input("Enter your height: "))
year = int(input("Enter your year of birth: "))

string1 += f"\nUser2 - #id: {id:<10} name: {lastName:<7} , {firstName:<7} height: {height:<5} year-of-birth: {year:<5}"

# User 3
print("User 3 details: ")
id = input("Enter your ID: ")
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
height = float(input("Enter your height: "))
year = int(input("Enter your year of birth: "))

string1 += f"\nUser3 - #id: {id:<10} name: {lastName:<7} , {firstName:<7} height: {height:<5} year-of-birth: {year:<5}"

print(string1)


# Exercise 2

grade = int(input("Enter your test grade: "))

if 0 <= grade <= 40:
    print("try harder next time...")
elif 41 <= grade <= 60:
    print("you're getting there, need some more work")
elif 61 <= grade <= 80:
    print("good pretty")
elif 81 <= grade <= 95:
    print("!awesome")
elif 96 <= grade <= 100:
    print("excellent!!! You're a Star!")
else:
    print("grade illegal")

match grade:
    case grade if 0 <= grade <= 40:
        print("try harder next time...")
    case grade if 41 <= grade <= 60:
        print("you're getting there, need some more work")
    case grade if 61 <= grade <= 80:
        print("good pretty")
    case grade if 81 <= grade <= 95:
        print("!awesome")
    case grade if 96 <= grade <= 100:
        print("excellent!!! You're a Star!")
    case _:
        print("grade illegal")


# Exercise 3

volumeLevel = int(input("Enter volume: "))

match volumeLevel:
    case 0:
        print("mute")
    case 1 | 2:
        print("very quiet")
    case 3:
        print("quiet")
    case 4:
        print("moderately quiet")
    case 5:
        print("medium")
    case 6:
        print("moderately loud")
    case 7:
        print("loud")
    case 8:
        print("very loud")
    case 9 | 10:
        print("extremely loud")
    case _:
        print("wrong volume")
