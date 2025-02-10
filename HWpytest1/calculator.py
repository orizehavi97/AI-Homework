import math
import sqlite3

# Homework starts at line 35

def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def make_error():
    raise IndexError()


def create_table(query):
    # check if table exists
    raise sqlite3.IntegrityError


def say_hello():
    name = input("enter name? ")
    return f"hello {name}"


# HOMEWORK
# a.
def power(a, b):
    return math.pow(a, b)

# b.
def sqrt(a):
    return math.sqrt(a)

# c.
def factorial(a):
    if a < 0:
        raise ValueError
    return math.factorial(a)
