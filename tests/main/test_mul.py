import pytest  # noqa


def test_mul(main, arr_ints):
    assert (
        main(
            datas=arr_ints,
            text="""
- in: ~ints
- mul: 2
""",
        ).queue
        == [0, 2, 4, 6]
    )


def test_mul_none(main, arr_ints):
    with pytest.raises(Exception) as e_info:
        assert main(
            datas=arr_ints,
            text="""
- in: ~ints
- mul:
""",
        )
    assert "Не задан множитель" in str(e_info.value)
