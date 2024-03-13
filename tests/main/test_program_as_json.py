def test_one(main):
    assert main(
        js=[{"in": [1, 2, 3]}, {"print": None}, {"last": None}]
    ).queue == [3]
