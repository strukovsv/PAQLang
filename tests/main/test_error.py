import pytest

def test_1(main):
    assert main(text = """
- in: [1, 2, 3, 4, 5, 6]                
- error: write into error
""")

def test_2(main):
    assert main(text = """
- in
- error: write into error empty lines
""")

def test_3(main):
    assert main(text = """
- in: 
    one: test one
    two: test two
- error: write into error dict
""")

def test_4(main, arr_ints):
  assert main(datas = arr_ints, text = """
- in:
  - {"result": 0, message: "This is error message"}
  - {"result": 1, message: "This is success message"}
- error: 
    name: "write error result 0"
    test-attr: result
    eq: 0
""")

def test_5(main, arr_ints):
  assert main(datas = arr_ints, text = """
- in:
  - {"result": 0, message: "This is error message"}
  - {"result": 1, message: "This is success message"}
- error: 
    name: "write error result 0, print message"
    test-attr: result
    send-attr: message          
    eq: 0
""")
