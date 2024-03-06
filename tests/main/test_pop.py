import pytest

# def test_one(main):
#   assert main(text = """
# - in: [1, 2, 3, 4, 5]
# - pop
# """).queue == [5]

# def test_two(main):
#   assert main(text = """
# - in: [1, 2, 3, 4, 5]
# - out: cnt
# - pop: cnt
# - print: pop
# - in: ~cnt                            
# - print: cnt
# """).queue == [1, 2, 3, 4]

def test_three(main):
  assert main(text = """
- in: [1, 2, 3, 4, 5]
- out: cnt
- while:
    - pop: cnt
    - break
    - print: cycle                  
""").queue == [1]
