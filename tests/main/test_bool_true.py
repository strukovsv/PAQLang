def test_main(main):
    assert (
        main(
            text="""
bool_true
"""
        ).queue
        == [1]
    )
