def test_1(main):
    main(
        text="""
- options:
    - in:
        # Подключение к github
        git_owner: ${MYGITHUB_OWNER}
        git_token: ${MYGITHUB_TOKEN}
        git_repo: ${MYGITHUB_REPO}
- stage:
    - github_branches:
      - ~options
    - print: branches
"""
    )


def test_2(main):
    main(
        text="""
- options:
    - in:
        # Подключение к github
        git_owner: ${MYGITHUB_OWNER}
        git_token: ${MYGITHUB_TOKEN}
        git_repo: ${MYGITHUB_REPO}
- stage:
    - github_branches:
      - ~options
      - regex: 'feat/.*'
    - print: branches
"""
    )


def test_3(main):
    main(
        text="""
- options:
    - in:
        # Подключение к github
        git_owner: ${MYGITHUB_OWNER}
        git_token: ${MYGITHUB_TOKEN}
        git_repo: ${MYGITHUB_REPO}
- stage:
    - github_branches:
      - ~options
      - search: master
    - print: branches
"""
    )
