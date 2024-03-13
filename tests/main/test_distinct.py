import pytest  # noqa


def test_normal(main):
    assert (
        main(
            text="""
- in:
  - 1
  - 2
  - 3
  - 2
- distinct
"""
        ).queue
        == [1, 2, 3]
    )


def test_str(main):
    with pytest.raises(Exception) as e_info:
        assert main(
            text="""
- in:
  - 1
  - 2
  - 3
  - 2
  - "test"
- distinct
"""
        )
    assert "'<' not supported between instances of 'str' and 'int'" in str(
        e_info.value
    )


def test_empty(main):
    assert (
        main(
            text="""
- in:
- distinct
"""
        ).queue
        == []
    )


def test_none(main):
    with pytest.raises(Exception) as e_info:
        assert main(
            text="""
- in:
  - 1
  -
- distinct
"""
        )
    assert (
        "'<' not supported between instances of 'NoneType' and 'int'"
        in str(e_info.value)
    )


def test_str_2(main):
    assert (
        main(
            text="""
- in:
  - test1
  - test2
  - test1
- distinct
"""
        ).queue
        == ["test1", "test2"]
    )
