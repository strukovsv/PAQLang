import pytest

def test_one(main, request):
  pgm = main(text = """
- in: 
  - "1;2;3;4;5"
- split: ";"
""")
  assert pgm.queue == ['1', '2', '3', '4', '5']

def test_two(main, request):
  pgm = main(text = """
- in: 
  - "1\n2\n3\n4\n5"
- split: "\n"
""")
  assert pgm.queue == ['1', '2', '3', '4', '5']  

def test_three(main, request):
  pgm = main(text = """
- in: 
  - "1\\n2\\n3\\n4\\n5"
- split
""")
  assert pgm.queue == ['1', '2', '3', '4', '5']    