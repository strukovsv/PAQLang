import pytest  # noqa


def test_one(main, arr_strings):
    assert (
        main(
            datas=arr_strings,
            text="""
- in: ~strings
- search: .*я.*
""",
        ).queue
        == ["Пять", "Девять", "Десять"]
    )


def test_two(main, arr_strings):
    assert (
        main(
            datas=arr_strings,
            text="""
- in: ~strings
- search: я
""",
        ).queue
        == []
    )


def test_three(main, arr_strings):
    assert (
        main(
            datas=arr_strings,
            text="""
- in: ~strings
- search:
    regex: .*я.*
""",
        ).queue
        == ["Пять", "Девять", "Десять"]
    )


def test_attr(main, arr_dict_strings):
    assert (
        main(
            datas=arr_dict_strings,
            text="""
- in: ~strings
- search:
    attr: code
    regex: .*я.*
""",
        ).queue
        == [{"code": "Пять"}, {"code": "Девять"}, {"code": "Десять"}]
    )


def test_attr_error(main, arr_dict_strings):
    with pytest.raises(Exception) as e_info:
        assert (
            main(
                datas=arr_dict_strings,
                text="""
- in: ~strings
- search:
    attr: code2
    regex: .*я.*
""",
            ).queue
            == [{"code": "Пять"}, {"code": "Девять"}, {"code": "Десять"}]
        )
    assert "Не найден атрибут" in str(e_info.value)
