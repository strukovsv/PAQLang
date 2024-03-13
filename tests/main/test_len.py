def test_normal(main, arr_ints):
    assert (
        main(
            datas=arr_ints,
            text="""
- in: ~ints
- len
""",
        ).queue
        == [5]
    )


def test_empty(main, arr_ints):
    assert (
        main(
            datas=arr_ints,
            text="""
- in
- len
""",
        ).queue
        == [0]
    )
