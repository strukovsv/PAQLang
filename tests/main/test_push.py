def test_empty(main):
    assert (
        main(
            text="""
- in
- push
"""
        ).queue
        == []
    )


def test_one(main):
    assert (
        main(
            text="""
- in
- push: 10
"""
        ).queue
        == [10]
    )


def test_two(main):
    assert (
        main(
            text="""
- in:
  - 20
  - 30
- push:
  - 10
  - 15
"""
        ).queue
        == [20, 30, 10, 15]
    )
