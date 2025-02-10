import pytest
import calculator

# Homework starts at line 87

def test_calculator_add_small():
    # Arrange
    a: int = 2
    b: int = 5
    expected: int = 7

    # Act
    actual: int = calculator.add(a, b)

    # Assert
    assert expected == actual, "small numbers add"

def test_calculator_minus_small():
    # Arrange
    a: int = 10
    b: int = 10
    expected: int = 0

    # Act
    actual: int = calculator.minus(a, b)

    # Assert
    assert expected == actual, "small numbers minus"

def test_calculator_multiply_small():
    # Arrange
    a: int = 10
    b: float = 0.1
    expected: float = 1.0

    # Act
    actual: float = calculator.multiply(a, b)

    # Assert
    assert expected == actual, "small numbers multiply"

def test_calculator_div_small():
    # Arrange
    a: int = 10
    b: float = 0.1
    expected: float = 100

    # Act
    actual: float = calculator.divide(a, b)

    # Assert
    assert expected == actual, "small numbers div"

# False positive
def test_calculator_div_by_zero1():
    # Arrange
    a: int = 10
    b: float = 0

    # Act
    try:
        # next line should raise an error
        calculator.divide(a, b)
        assert False, "should raise ZeroDivisionError"

    except ZeroDivisionError as e:
        # this is the good scenario
        assert True


# False positive
def test_calculator_div_by_zero2():
    # Arrange
    a: int = 10
    b: float = 0

    # Act
    with pytest.raises(Exception) as ex:
        calculator.divide(a, b)

def test_check_error_happened():
    with pytest.raises(IndexError) as ex:
        calculator.make_error()



# HOMEWORK
# d.
def test_calculator_power():
    # Arrange
    a: int = 2
    b: int = 4
    expected: int = 16

    # Act
    actual: int = calculator.power(a, b)

    # Assert
    assert expected == actual, "small number power"

# e.
def test_calculator_power2():
    # Arrange
    a: int = 3
    b: int = 2
    expected: int = 9

    # Act
    actual: int = calculator.power(a, b)

    # Assert
    assert expected == actual, "small number power"

# f.
def test_calculator_sqrt():
    # Arrange
    a: int = 25
    expected: int = 5

    # Act
    actual: int = calculator.sqrt(a)

    # Assert
    assert expected == actual, "small number sqrt"

# g.
def test_calculator_sqrt2():
    # Arrange
    a: int = -5

    # Act & Assert
    try:
        calculator.sqrt(a)
        assert False, "should raise ValueError"

    except ValueError as e:
        assert True

# h.
def test_calculator_factorial():
    # Arrange
    a: int = 4
    expected: int = 24

    # Act
    actual: int = calculator.factorial(a)

    # Assert
    assert expected == actual, "small number factorial"

# i.
def test_calculator_factorial2():
    # Arrange
    a: int = 5
    expected: int = 120

    # Act
    actual: int = calculator.factorial(a)

    # Assert
    assert expected == actual, "small number factorial"

# j.
def test_calculator_factorial3():
    # Arrange
    a: int = -3

    # Act & Assert
    try:
        calculator.factorial(a)
        assert False, "should raise ValueError"

    except ValueError as e:
        assert True