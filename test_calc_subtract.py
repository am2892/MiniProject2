def test_calc_subtract():
    from Calculator import Calculator
    c = Calculator()
    assert c.subtract(15,10) == 5

def test_calc_subtract_fail():
    from Calculator import Calculator
    c = Calculator()
    assert c.subtract(90,10) != 79
