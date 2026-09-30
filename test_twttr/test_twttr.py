from twttr import shorten

def test_lower():
    assert shorten("twitter") == "twttr"

def test_upper():
    assert shorten("TWITTER") == "TWTTR"

def test_numbers():
    assert shorten("CS50") == "CS50"

def test_punc():
    assert shorten("hello!!!") == "hll!!!"
