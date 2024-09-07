# EXERCISE 1 - Input 3 numbers, print their summary and multiplication

a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))

print("Sum:", a + b + c)
print("Mult:", a * b * c)



# EXERCISE 2 - Input 2 floats, calculate the difference and print it

x = float(input("First number: "))
y = float(input("Second number: "))

diff: float = abs(x - y)

print("The difference is:", diff)



# EXERCISE 3 - Input 2 strings, concat them with '*' and '-' and print alternatively

str1 = input("First string: ")
str2 = input("Second string: ")

print('*' + str1 + '*' + str2 + '*')
print('-' + str1 + '-' + str2 + '-')



# EXERCISE 4 - Input 2 numbers, print the bigger one

a = int(input("First number: "))
b = int(input("Second number: "))

if a > b:
    print(a)
else:
    print(b)



# EXERCISE 5 - Input 2 numbers, print them in ascending order

a = int(input("First number: "))
b = int(input("Second number: "))

if a > b:
    print(b)
    print(a)
else:
    print(a)
    print(b)