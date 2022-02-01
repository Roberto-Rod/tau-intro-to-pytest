
#----------------------------------------------------------
# Imports
#----------------------------------------------------------

import pytest

#----------------------------------------------------------
# Simple test function
#----------------------------------------------------------

@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2

#----------------------------------------------------------
# A function to show assertion introspection
#----------------------------------------------------------

@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c

#----------------------------------------------------------
# A function that verifies an exception
#----------------------------------------------------------

@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0 

    assert 'division by zero' in str(e.value)

#----------------------------------------------------------
# DRY Principle: Don't Repeat Yourself
# A parametrized test function
#----------------------------------------------------------

# list of tuples to be used as arguments to be passed to the test function

products = [
    (2, 3, 6),                  # positive integers
    (1, 99, 99),                # identity
    (0, 99, 0),                 # zero
    (3, -4, -12),               # + by -
    (-5, -4, 20),              # - by -
    (2.5, 6.7, 16.75),          # floats
]

@pytest.mark.math
@pytest.mark.parametrize('a, b, product', products)         # aspect Orientated Programming using a decorator function
def test_multiplication(a, b, product):                     # This function is called once per tuple on the products list
    assert a* b == product


#----------------------------------------------------------
# Classes
#----------------------------------------------------------




