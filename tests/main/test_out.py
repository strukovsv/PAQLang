import pytest  # noqa


def test_parallel(main):
    pgm = main(
        text="""
in: 10
out: test1
"""
    )
    assert pgm.queue == [10]
    assert pgm.get_data("test1") == []


def test_list(main):
    pgm = main(
        text="""
- in: 10
- out: test1
"""
    )
    assert pgm.queue == [10]
    assert pgm.get_data("test1") == [10]


def test_error_write(main):
    with pytest.raises(Exception) as e_info:
        main(
            text="""
- in: 10
- out
"""
        )
    assert "Не указано наименование перем" in str(e_info.value)


def test_error_read(main):
    with pytest.raises(Exception) as e_info:
        pgm = main(
            text="""
- in: 10
- out: test1
    """
        )
        pgm.get_data("test2")
    assert "Не определена переменная test2" in str(e_info.value)
