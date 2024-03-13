def test_one(main):
    assert (
        main(
            text="""
- in: [[1, 2], [3, 4, 5]]
# Пока не смог создать теста для этой функции
- expand
"""
        ).queue
        == [1, 2, 3, 4, 5]
    )
