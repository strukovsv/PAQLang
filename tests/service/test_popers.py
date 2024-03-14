# def test_all(main):
#     main(
#         text="""
# - popers
# """
#     )


def test_OtherOpers(main):
    main(
        text="""
- popers:
    # groups: IoOpers
    path: /tmp/log
"""
    )

# def test_group_OtherOpers(main):
#     main(
#         text="""
# - popers:
#     group: OtherOpers
#     file: /tmp/log/OtherOpers.md
# """
#     )


# def test_next_group(main):
#     main(
#         text="""
# - popers:
#     group:
#     - OtherOpers
#     - IoOpers
# """
#     )
