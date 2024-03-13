def test_1(main):
    assert (
        main(
            text="""
- in: {"a1":10, "a2":20}
- attr
"""
        ).queue
        == []
    )


def test_2(main):
    assert (
        main(
            text="""
- in: {"a1":10, "a2":20}
- attr: a1
"""
        ).queue
        == [10]
    )


def test_3(main):
    assert (
        main(
            text="""
- in: {"a1":10, "a2":20}
- attr: a2
"""
        ).queue
        == [20]
    )


def test_4(main):
    assert (
        main(
            text="""
- in: {"a1":10, "a2":20}
- attr:
  - a1
"""
        ).queue
        == [10]
    )


def test_5(main):
    assert (
        main(
            text="""
- in: {"a1":10, "a2":20}
- attr:
  - a1
  - a2
"""
        ).queue
        == [{"a1": 10, "a2": 20}]
    )


def test_6(main):
    assert (
        main(
            text="""
- in: {"a1":10, "a2":20}
- attr:
    a1:
"""
        ).queue
        == [{"a1": 10}]
    )


def test_7(main):
    assert (
        main(
            text="""
- in: {"a1":10, "a2":20}
- attr:
    a1:
    a2:
"""
        ).queue
        == [{"a1": 10, "a2": 20}]
    )


def test_8(main):
    assert (
        main(
            text="""
- in: {"a1":10, "a2":20}
- attr:
    a1: b1
    a2: b2
"""
        ).queue
        == [{"b1": 10, "b2": 20}]
    )
