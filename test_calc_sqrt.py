def test_calc_sqrt():
    from Calculator import Calculator
    c = Calculator()
    assert c.squareroot(36) == 6

def test_calc_sqrt_fail():
    from Calculator import Calculator
    c = Calculator()
    assert c.squareroot(16) != 5
