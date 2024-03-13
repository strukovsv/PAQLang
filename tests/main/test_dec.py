def test_dec(main):
    assert (
        main(
            text="""
- in: 2
- dec
"""
        ).queue
        == [1]
    )


def test_dec_step_attr(main):
    assert (
        main(
            text="""
- in: 3
- dec:
    step: 2
"""
        ).queue
        == [1]
    )


def test_dec_mem_default(main):
    assert (
        main(
            text="""
- in: 10
- out: test
- in: 0
- dec: test
"""
        ).get_data("test")
        == [9]
    )


def test_dec_mem(main):
    assert (
        main(
            text="""
- in: 10
- out: test
- in: 0
- dec:
    mem: test
"""
        ).get_data("test")
        == [9]
    )


def test_dec_2(main):
    assert (
        main(
            text="""
- in: 10
- out: test
- in: 0
- dec:
    mem: test
    step: 2.3
"""
        ).get_data("test")
        == [7.7]
    )


def test_dec_minus(main):
    assert (
        main(
            text="""
- in: 1
- dec:
    step: -2.3
"""
        ).queue
        == [3.3]
    )


def test_dec_mem_create(main):
    pgm = main(
        text="""
- dec:
    mem: test
    step: 2.3
"""
    )
    pgm.queue == [0 - 2.3]
    pgm.get_data("test") == [0 - 2.3]


def test_dec_step_default(main):
    assert (
        main(
            text="""
- in: 4
- dec:
    step: 2
"""
        ).queue
        == [2]
    )
