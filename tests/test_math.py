
#----------------------------------------------------------
# Imports
#----------------------------------------------------------

import pytest

#----------------------------------------------------------
# Simple test function
#----------------------------------------------------------

def test_one_plus_one():
    assert 1 + 1 == 2

#----------------------------------------------------------
# A function to show assertion introspection
#----------------------------------------------------------

def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c

#----------------------------------------------------------
# A function that verifies an exception
#----------------------------------------------------------

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0 

    assert 'division by zero' in str(e.value)

