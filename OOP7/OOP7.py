def sum_numbers(*args):
    numbers_sum = 0
    for n in args:
        numbers_sum += n
    return numbers_sum


def print_user_info(**kwargs):
    result = ''
    for key, value in kwargs.items():
        result += f'{key}: {value}, '
    print(result)


def combine_values(*args, **kwargs):
    print(f"Sum: {sum_numbers(*args)}")
    for key, value in kwargs.items():  # Could use the function above but the output is provided at the same line.
        print(f'{key}: {value}')


def greet_user(**kwargs):
    name = kwargs.get('name')
    if name:
        print(f"Hello {name}")
    else:
        print("Hello guest")


print("Ex 1:")
print(sum_numbers(1, 2, 3, 4))
print("Ex 2:")
print_user_info(name="Dana", age=30, city="Tel Aviv")
print("Ex 3:")
combine_values(2, 4, 6, name="Tom", job="Dev")
print("Ex 4:")
greet_user(name="Lior")
greet_user()
