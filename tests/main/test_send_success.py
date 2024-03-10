import pytest

def test_one(main, arr_ints):
  assert main(datas = arr_ints, text = """
- in:
  - This is test message line 1
  - This is test message line 2
- send_success: "git2oracle: success messages"
""")

def test_2(main, arr_ints):
  assert main(datas = arr_ints, text = """
- in:
  - {"result": 0, message: "This is error message"}
  - {"result": 1, message: "This is success message"}
- send_success: 
    name: "git2oracle: success messages"
    test-attr: result
    eq: 1
""")

def test_3(main, arr_ints):
  assert main(datas = arr_ints, text = """
- in:
  - {"result": 0, message: "This is error message"}
  - {"result": 1, message: "This is success message"}
- send_success: 
    name: "git2oracle: success messages"
    test-attr: result
    send-attr: message          
    eq: 1
""")
