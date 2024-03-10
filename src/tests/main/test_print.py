import pytest

def test_print(main, request):
    pgm = main(text = """
- in:               
  - 1
  - 2
  - 3             
- print
""")
    assert pgm.queue == [1, 2, 3]

def test_print_dict(main):
    pgm = main(text = """
- in:               
    test1: 1
    test2: 2
- print               
""")
    assert pgm.queue == [{'test1': 1, 'test2': 2}]

def test_print_none(main):
    pgm = main(text = """
- in               
- print               
""")
    assert pgm.queue == []
