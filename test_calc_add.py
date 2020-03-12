def test_calc_add():
    from Calculator import Calculator
    c = Calculator()
    assert c.add(2,2) == 4

def test_calc_add_fail():
    from Calculator import Calculator
    c = Calculator()
    assert c.add(3,5) != 6
