def test_one(main, request):
    pgm = main(
        text="""
- in:
  - 0
  - test2
  - test
  - 15
- join: "$"
"""
    )
    assert pgm.queue == ["0$test2$test$15"]


def test_two(main, request):
    pgm = main(
        text="""
- in:
  - 0
  - test2
  - test
  - 15
- join: "\\n"
"""
    )
    assert pgm.queue == ["0\ntest2\ntest\n15"]


def test_3(main, request):
    pgm = main(
        text="""
- in:
  - 0
  - test2
  - test
  - 15
- join: '\\n'
"""
    )
    assert pgm.queue == ["0\\ntest2\\ntest\\n15"]


def test_4(main, request):
    pgm = main(
        text="""
- in:
  - 0
  - test2
  - test
  - 15
- join
"""
    )
    assert pgm.queue == ["0\ntest2\ntest\n15"]
