def test_calc_square():
    from Calculator import Calculator
    c = Calculator()
    assert c.square(6) == 36

def test_calc_square_fail():
    from Calculator import Calculator
    c = Calculator()
    assert c.square(4) != 18
