import pytest

def test_one(main):
  assert main(text = """
- in: [1, 2, 3, 4, 5]
- union: [4, 5, 6, 7, 8]
""").queue == [1, 2, 3, 4, 5, 6, 7, 8]

def test_two(main):
  assert main(text = """
- in
- union: [4, 5, 6, 7, 8]
""").queue == [4, 5, 6, 7, 8]

def test_three(main):
  assert main(text = """
- in: [1, 2, 3, 4, 5]
- union: 6
""").queue == [1, 2, 3, 4, 5, 6]

def test_four(main):
  assert main(text = """
- in: [1, 2, 3, 4, 5]
- union 
""").queue == [1, 2, 3, 4, 5]
