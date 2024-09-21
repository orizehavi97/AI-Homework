# # Exercise 1
#
# num = 0
# count = 0
# count_pos = 0
# count_neg = 0
# count_zero = 0
# count_seven = 0
# temp_pos: int = None
# temp_neg: int = None
#
# while count < 10:
#     num = int(input("Please enter a number: "))
#     if num == -9999:
#         break
#     elif 1000 < num < -1000:
#         continue
#     else:
#         match num:
#             case 0:
#                 count_zero += 1
#                 count_seven += 1
#             case num if num > 0:
#                 count_pos += 1
#                 temp_pos = num
#                 if num % 7 == 0:
#                     count_seven += 1
#             case num if num < 0:
#                 count_neg += 1
#                 temp_neg = num
#                 if num % 7 == 0:
#                     count_seven += 1
#     count += 1
#
# else:
#     print( f"Positive numbers: {count_pos}, negative numbers: {count_neg}, number of zeroes: {count_zero}, divideable by 7: {count_seven}, last positive: {temp_pos}, last negative: {temp_neg}")


# # Exercise 2
#
# result: float = 0
# sum_res: float = 0
# current_record = 6.23
# temp_record: float = 0
# count = 0
# name: str = None
#
# for _ in range(7):
#     result = float(input("Enter your record: "))
#     if result < 5.8:
#         continue
#     count += 1
#     sum_res += result
#     if result > temp_record:
#         temp_record = result
#         if temp_record > 6.23 and temp_record > current_record:
#             name = input("Enter your name: ")
#             current_record = temp_record
# print(f"Correct results: {count}, average results: {sum_res / count :.2f}")
# print(f"Highest result :{temp_record}")
# if current_record > 6.23:
#     print(f"New world record held by {name}, the new record is: {current_record}")
# else:
#     print(None)

# Exercise 3

num = int(input("num = "))
str1 = ""
num = num // 2 * 2 - 1 # if num is not an odd number, minus 1

for i in range(1,num+1, 2):
    for j in range(1, i+1):
        str1 += f"{j}"
    print(f"{str1: ^{num}}")
    str1 = ""
for i in range(num-2,0, -2):
    for j in range(1, i+1):
        str1 += f"{j}"
    print(f"{str1: ^{num}}")
    str1 = ""

