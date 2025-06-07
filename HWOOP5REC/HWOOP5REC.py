def print_stars(n):
    # Prints n stars in one line, e.g., print_stars(5) => *****
    if n == 0:
        print()
        return
    print('*', end='')
    print_stars(n - 1)


def count_char(c, word):
    # Returns how many times character c appears in the word
    if len(word) == 0:
        return 0
    return (1 if word[0] == c else 0) + count_char(c, word[1:])


def print_digits_forward(num):
    # Prints the digits of the number in original order
    if num < 10:
        print(num, end=' ')
        return
    print_digits_forward(num // 10)
    print(num % 10, end=' ')


def count_odd_digits(n):
    # Returns the number of odd digits in the number
    if n < 10:
        return 1 if n % 2 == 1 else 0
    return (1 if (n % 10) % 2 == 1 else 0) + count_odd_digits(n // 10)


def reverse_print(word):
    # Prints the word in reverse order using recursion
    if len(word) == 0:
        return
    reverse_print(word[1:])
    print(word[0], end='')


print_stars(5)
print(count_char("a", "banana"))
print_digits_forward(527)
print()
print(count_odd_digits(13572))
reverse_print("hello")
