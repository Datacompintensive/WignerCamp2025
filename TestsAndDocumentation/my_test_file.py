import pytest
import numpy as np

from my_functions import *

def test_square():
    assert square(2) == 4
    assert square(-3) == 9

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

def test_reciprocal():
    assert reciprocal(2.0) == pytest.approx(0.5)

def test_normalize():
    v = np.array([3.0, 4.0])
    expected = np.array([0.6, 0.8])
    np.testing.assert_allclose(normalize(v), expected, rtol=1e-5)

def test_fail():
    assert (1 + 1) == 3

def test_double():
    # Write your solution here
    pass

def test_safe_log():
    # Write your solution here
    pass