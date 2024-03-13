def test_all(main):
    main(
        text="""
- opers
- save: opers
"""
    )


def test_OtherOpers(main):
    main(
        text="""
- opers: OtherOpers
- save: OtherOpers
"""
    )
