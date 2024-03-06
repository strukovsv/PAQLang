import pytest
import logging

def test_one(main):
  pgm = main(text = """
- in: '[{"test": 1, "test2":2}]'
- to_json
- print                          
""")
  assert pgm.queue == [{"test": 1, "test2":2}]

def test_two(main):
  pgm = main(text = """
- in: |
    [
      {"test": 1, "test2":2}, 
      {"test": 10, "test3":20}
    ]
- to_json
""")  
  assert pgm.queue == [{"test": 1, "test2":2}, {"test": 10, "test3":20}]

def test_three(main):
  pgm = main(text = """
- in: '{"test": 1, "test2":2}'
- to_json
""")
  assert pgm.queue == [{"test": 1, "test2":2}]

def test_4(main):
  pgm = main(text = """
- in: 'text string'
- to_json
""")
  assert pgm.queue == ['text string']

def test_5(main):
  pgm = main(text = """
- in: '10'
- to_json
""")
  assert pgm.queue == [10]

def test_6(main):
  pgm = main(text = """
- in: '[1, 2, 3, 4]'
- to_json
""")
  assert pgm.queue == [1, 2, 3, 4]

def test_7(main):
  pgm = main(text = """
- in:
  - text: "[1, 2, 3, 4]"
  - text: "[5, 6, 7, 8]"
- to_json: text
""")
  assert pgm.queue == [1, 2, 3, 4, 5, 6, 7, 8]

def test_8(main):
  pgm = main(text = """
- in:
  - text: "[1, 2, 3, 4]"
  - text: "[5, 6, 7, 8]"
- to_json:
    attr: text
""")
  assert pgm.queue == [1, 2, 3, 4, 5, 6, 7, 8]
