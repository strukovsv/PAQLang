import pytest

def test_one(main, arr_ints):
  assert main(datas = arr_ints, text = """
- in:
  - This is test message line 1
  - This is test message line 2
- send_error: "git2oracle: error messages"
""")

def test_2(main, arr_ints):
  assert main(datas = arr_ints, text = """
- in:
  - {"result": 0, message: "This is error message"}
  - {"result": 1, message: "This is success message"}
- send_error: 
    name: "git2oracle: error messages"
    test-attr: result
    eq: 0
""")

def test_3(main, arr_ints):
  assert main(datas = arr_ints, text = """
- in:
  - {"result": 0, message: "This is error message"}
  - {"result": 1, message: "This is success message"}
- send_error: 
    name: "git2oracle: error messages"
    test-attr: result
    send-attr: message          
    eq: 0
""")
