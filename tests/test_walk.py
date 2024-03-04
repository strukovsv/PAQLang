import pytest

# def test_one(main, request):
#   pgm = main(text = """
# - walk: "/tests" 
# - print: "walk"             
# """)

def test_two(main, request):
  pgm = main(text = """
- walk: 
    path: "/tests" 
    regex: "^/tests/test_n.*py$"
- print: "walk"             
""")
  # assert pgm.queue == ['1', '2', '3', '4', '5']

