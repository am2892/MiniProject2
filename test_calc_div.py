def test_calc_divide():
    from Calculator import Calculator
    c = Calculator()
    assert c.divide(2,2) == 1

def test_calc_divide_fail():
    from Calculator import Calculator
    c = Calculator()
    assert c.divide(10,2) != 3
