def test_1(main):
    main(
        text="""
- options:
    - in:
        # Подключение к github
        git_owner: ${GITHUB_OWNER}
        git_token: ${GITHUB_TOKEN}
        git_repo: ${GITHUB_REPO}
- stage:
    - github_branches:
      - ~options
#      - regex: 'feat/.*'
    - print: branches
"""
    )
#    assert len(pgm.queue) > 1


# def test_2(main, request):
#     pgm = main(
#         text="""
# - options:
#     - in:
#         # Подключение к gitlab
#         git_url: ${GIT_URL}
#         git_token: ${GIT_TOKEN}
#         git_repo: ${GIT_REPO}
# - stage:
#     - gitlab_branches:
#       - ~options
#       - search: master
#     - print: branches
# """
#     )
#     assert len(pgm.queue) == 1
