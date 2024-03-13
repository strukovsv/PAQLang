def test_inc(main):
    assert (
        main(
            text="""
- in: 1
- inc
"""
        ).queue
        == [2]
    )


def test_inc_step_default(main):
    assert (
        main(
            text="""
- in: 1
- inc:
    step: 2
"""
        ).queue
        == [3]
    )


def test_inc_step_attr(main):
    assert (
        main(
            text="""
- in: 1
- inc:
    step: 2
"""
        ).queue
        == [3]
    )


def test_inc_mem_default(main):
    assert (
        main(
            text="""
- in: 10
- out: test
- in: 0
- inc: test
"""
        ).get_data("test")
        == [11]
    )


def test_inc_mem(main):
    assert (
        main(
            text="""
- in: 10
- out: test
- in: 0
- inc:
    mem: test
"""
        ).get_data("test")
        == [11]
    )


def test_inc_2(main):
    assert (
        main(
            text="""
- in: 10
- out: test
- in: 0
- inc:
    mem: test
    step: 2.3
"""
        ).get_data("test")
        == [12.3]
    )


def test_inc_minus(main):
    assert (
        main(
            text="""
- in: 1
- inc:
    step: -2.3
"""
        ).queue
        == [-1.2999999999999998]
    )


def test_inc_mem_create(main):
    pgm = main(
        text="""
- inc:
    mem: test
    step: 2.3
"""
    )
    assert pgm.queue == [0 + 2.3]
    assert pgm.get_data("test") == [0 + 2.3]
