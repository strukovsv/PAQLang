def test_one(main):
    assert (
        main(
            text="""
- in: [1, 2, 3, 4, 5]
- minus: [4, 5, 6, 7, 8]
"""
        ).queue
        == [1, 2, 3]
    )


def test_two(main):
    assert (
        main(
            text="""
- in: [1, 2, 3, 4, 5]
- minus
"""
        ).queue
        == [1, 2, 3, 4, 5]
    )


def test_three(main):
    assert (
        main(
            text="""
- in
- minus: [4, 5, 6, 7, 8]
"""
        ).queue
        == []
    )


def test_four(main):
    assert (
        main(
            text="""
- in: [1, 2, 3, 4, 5]
- minus: 3
"""
        ).queue
        == [1, 2, 4, 5]
    )


def test_5(main):
    assert (
        main(
            text="""
- in: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
- minus: 3
"""
        ).queue
        == [1, 2, 4, 5, 1, 2, 4, 5]
    )
