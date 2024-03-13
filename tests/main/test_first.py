def test_empty(main):
    assert (
        main(
            text="""
- in
- first
"""
        ).queue
        == []
    )


def test_one(main):
    assert (
        main(
            text="""
- in:
  - 1
  - 2
  - 3
- first
"""
        ).queue
        == [1]
    )


def test_two(main, arr_ints):
    assert (
        main(
            datas=arr_ints,
            text="""
- first: ints
""",
        ).queue
        == [0]
    )
