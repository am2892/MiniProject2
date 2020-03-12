def test_calc_multiply():
    from Calculator import Calculator
    c = Calculator()
    assert c.multiply(2,2) == 4

def test_calc_multiply_fail():
    from Calculator import Calculator
    c = Calculator()
    assert c.multiply(3,5) != 11
