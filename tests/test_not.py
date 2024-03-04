import pytest

def test_to_false(main):
    assert main(text = """
- bool_true
- not                
""").queue == []

def test_to_true(main):
    assert main(text = """
- bool_false
- not                
""").queue == [1]
