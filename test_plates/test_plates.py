from plates import is_valid

def test_two():
    assert is_valid("JJ") == True
    assert is_valid("J1") == False

def test_maxmin():
    assert is_valid("JK1234") == True
    assert is_valid("JK12345") == False

def test_numbers():
    assert is_valid("AA22") == True
    assert is_valid("AA22AA") == False
    assert is_valid("AA03") == False

def test_punctuations():
    assert is_valid("AJK12!") == False
