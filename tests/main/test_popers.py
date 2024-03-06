import pytest

def test_all(main):
    pgm = main(text = """
- popers
""")

def test_OtherOpers(main):
    pgm = main(text = """
- popers: OtherOpers
""")

def test_group_OtherOpers(main):
    pgm = main(text = """
- popers: 
    group: OtherOpers
    file: /tmp/log/OtherOpers.md
""")

def test_next_group(main):
    pgm = main(text = """
- popers: 
    group:
    - OtherOpers
    - IoOpers
""")
