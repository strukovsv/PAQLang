import pytest  # noqa


def test_add(main, arr_ints):
    assert (
        main(
            datas=arr_ints,
            text="""
- in: ~ints
- add: 9
""",
        ).queue
        == [0 + 9 + 2, 1 + 9, 2 + 9, 3 + 9]
    )


def test_add_none(main, arr_ints):
    with pytest.raises(Exception) as e_info:
        assert main(
            datas=arr_ints,
            text="""
- in: ~ints
- add:
""",
        )
    assert "Не задано слогаемое" in str(e_info.value)
