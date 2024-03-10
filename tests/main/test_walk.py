import pytest

def test_one(main, request):
  pgm = main(text = """
- in: /tests               
- walk:
    regex: "^/tests/test_n.*py$"
- print: "walk"             
""")

def test_two(main, request):
  pgm = main(text = """
- in: 
  - /tests/data
  - /tests/.pytest_cache                       
- walk: 
- print: "walk"             
""")
  # assert pgm.queue == ['1', '2', '3', '4', '5']

