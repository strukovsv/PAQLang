import pytest  # noqa


def test_div(main, arr_ints):
    assert (
        main(
            datas=arr_ints,
            text="""
- in: ~ints
- div: 3
""",
        ).queue
        == [0 / 3, 1 / 3, 2 / 3, 3 / 3]
    )


def test_div_zero(main, arr_ints):
    with pytest.raises(Exception) as e_info:
        assert main(
            datas=arr_ints,
            text="""
- in: ~ints
- div: 0
""",
        )
    assert "Делитель равен нулю" in str(e_info.value)


def test_div_none(main, arr_ints):
    with pytest.raises(Exception) as e_info:
        assert main(
            datas=arr_ints,
            text="""
- in: ~ints
- div:
""",
        )
    assert "Не задан делитель" in str(e_info.value)
