from math_utils import total, is_even, divide

def test_total_single_item():
    assert total([5]) == 5

def test_total_multiple_items():
    assert total([1, 2, 3]) == 6

def test_total_empty():
    assert total([]) == 0

def test_is_even_true():
    assert is_even(4) == True

def test_is_even_false():
    assert is_even(3) == False

def test_divide_normal():
    assert divide(7, 2) == 3.5

def test_divide_exact():
    assert divide(10, 2) == 5.0
