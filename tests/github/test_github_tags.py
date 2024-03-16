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
    - github_tags:
      - ~options
    - print: tags
"""
    )


def test_2(main):
    main(
        text="""
- options:
    - in:
        # Подключение к github
        git_owner: ${GITHUB_OWNER}
        git_token: ${GITHUB_TOKEN}
        git_repo: ${GITHUB_REPO}
- stage:
    - github_tags:
      - ~options
      - search: v1.0.1
    - print: tag v1.0.1
"""
    )


def test_3(main):
    main(
        text="""
- options:
    - in:
        # Подключение к github
        git_owner: ${GITHUB_OWNER}
        git_token: ${GITHUB_TOKEN}
        git_repo: ${GITHUB_REPO}
- stage:
    - github_tags:
      - ~options
      - regex: '^.*0$'
    - print: tag regex .*0
"""
    )
