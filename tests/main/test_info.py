def test_1(main):
    assert main(
        text="""
- in: [1, 2, 3, 4, 5, 6]
- info: write into info
"""
    )


def test_2(main):
    assert main(
        text="""
- in
- info: write into info empty lines
"""
    )


def test_3(main):
    assert main(
        text="""
- in:
    one: test one
    two: test two
- info: write into info dict
"""
    )


def test_4(main, arr_ints):
    assert main(
        datas=arr_ints,
        text="""
- in:
  - {"result": 0, message: "This is error message"}
  - {"result": 1, message: "This is success message"}
- info:
    name: "write info result 1"
    test-attr: result
    eq: 1
""",
    )


def test_5(main, arr_ints):
    assert main(
        datas=arr_ints,
        text="""
- in:
  - {"result": 0, message: "This is error message"}
  - {"result": 1, message: "This is success message"}
- info:
    name: "write info result 1, print message"
    test-attr: result
    send-attr: message
    eq: 1
""",
    )
