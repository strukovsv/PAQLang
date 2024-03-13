import pytest  # noqa


def test_sub(main, arr_ints):
    assert (
        main(
            datas=arr_ints,
            text="""
- in: ~ints
- sub: 9
""",
        ).queue
        == [0 - 9, 1 - 9, 2 - 9, 3 - 9]
    )


def test_sub_none(main, arr_ints):
    with pytest.raises(Exception) as e_info:
        assert main(
            datas=arr_ints,
            text="""
- in: ~ints
- sub:
""",
        )
    assert "Не задано вычитаемое значение" in str(e_info.value)
