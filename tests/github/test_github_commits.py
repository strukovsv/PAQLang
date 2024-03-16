def test_1(main, request):
    main(
        text="""
- options:
    - in:
        # Подключение к github
        git_owner: ${GITHUB_OWNER}
        git_token: ${GITHUB_TOKEN}
        git_repo: ${GITHUB_REPO}
- stage:

    - in: master
    - github_commits:
      - ~options
      - since: "20240306"
    - attr:
      - authored_date
      - last_message
    - print
"""
    )


def test_2(main, request):
    main(
        text="""
- options:
    - in:
        # Подключение к github
        git_owner: ${GITHUB_OWNER}
        git_token: ${GITHUB_TOKEN}
        git_repo: ${GITHUB_REPO}
- stage:
    - in: master
    - github_commits:
      - ~options
      - until: "20240306"
    - attr:
      - authored_date
      - last_message
    - print
"""
    )


def test_3(main, request):
    main(
        text="""
- options:
    - in:
        # Подключение к github
        git_owner: ${GITHUB_OWNER}
        git_token: ${GITHUB_TOKEN}
        git_repo: ${GITHUB_REPO}
- stage:
    - in: master
    - github_commits:
      - ~options
      - path: ".github/workflows/pytest.yml"
    - attr:
      - authored_date
      - last_message
    - print
"""
    )
