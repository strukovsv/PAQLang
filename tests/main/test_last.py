def test_empty(main):
    assert (
        main(
            text="""
- in
- last
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
- last
"""
        ).queue
        == [3]
    )


def test_two(main, arr_strings):
    assert (
        main(
            datas=arr_strings,
            text="""
- last: strings
""",
        ).queue
        == ["Десять"]
    )
