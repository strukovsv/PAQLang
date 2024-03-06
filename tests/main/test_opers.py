import pytest

def test_all(main):
    pgm = main(text = """
- opers
- save: opers               
""")

def test_OtherOpers(main):
    pgm = main(text = """
- opers: OtherOpers
- save: OtherOpers
""")
