from bank import value

def test_keyword():
    assert value("hello") == 0
    assert value("HELlo") == 0

def test_letter():
    assert value("hey") == 20
    assert value("hEy") == 20

def test_else():
    assert value("random") == 100
    assert value("rAndom") == 100
