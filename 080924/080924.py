# Exercise 1

slices = int(input("How man pizza slices? "))

print("Each friend recieved: ", slices // 4, "pizza slices left: ", slices % 4)

friends = int(input("How many friends? "))
slices = int(input("How man pizza slices? "))

print("Each friend recieved: ", slices // friends, "pizza slices left: ", slices % friends)


# Exercise 3

# if 4 < 9: ? True
# if (2 * 3 + 4) * (7 + 7): ? True
# if 18 + 18: ? True
# if 10 == 10: ? True
# if 10 == 10 and 20 == 30: ? False
# if 10 == 10 or 20 == 30: ? True
# if 20 == 30 or 10 == 10: ? True
# if not 3: ? False
# if 3: ? True
# if (33 > 20) and (2 < 12) and 10: ? True
# if True and True: ? True
# if True and False: ? False
# if True or False: ? True
# if False or True: ? True
# if (not 10) and (10): ? False
# if (not 10) and (not 10): ? False
# if 5 != 5 and 5 == 5: ? False
# if 2 == 2 or 3 == 3: ? True
# if 2 == 2 and 3 == 3: ? True
# if 40 == 30 and 1 >= 4: ? False
# if 13 >= 3 or 47 >= 5: ? True


# Exercise 4
i = 10
while i <= 20:
    print(i)
    i += 1

i = 10
while i <= 20:
    print(i)
    i += 2

i = 10
a = int(input("Give me a number between 1 and 20: "))
while i <= 20:
    print(i)
    i += a