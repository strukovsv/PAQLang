def test_main(main):
    assert (
        main(
            text="""
bool_false
"""
        ).queue
        == []
    )
