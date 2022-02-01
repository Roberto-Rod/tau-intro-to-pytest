
#----------------------------------------------------------
# Imports
#----------------------------------------------------------

import pytest
from stuff.accum import Accumulator


#----------------------------------------------------------
# Fixtures
#----------------------------------------------------------

@pytest.fixture
def accum():
    return Accumulator()

#----------------------------------------------------------
# Tests for the Accumulator class
#----------------------------------------------------------

def test_accumulator_init(accum):
    assert accum.count == 0 


def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 1


def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3


def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2

def test_accumulator_add_in_loop(accum):

    numbers = [3, 3, 3, 9, 2]

    for n in numbers:

        accum.add(n)
    assert accum.count == 20        # Adding all the numbers in the list will result in a sum of 20


def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        accum.count = 10

