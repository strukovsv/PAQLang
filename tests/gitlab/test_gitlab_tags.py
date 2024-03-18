def test_1(main, request):
    main(
        text="""
- options:
    - in:
        # Подключение к gitlab
        git_url: ${MYGITLAB_URL}
        git_token: ${MYGITLAB_TOKEN}
        git_repo: ${MYGITLAB_REPO}
- stage:
    - gitlab_tags:
      - ~options
    - print: tags
"""
    )


def test_2(main, request):
    main(
        text="""
- options:
    - in:
        # Подключение к gitlab
        git_url: ${MYGITLAB_URL}
        git_token: ${MYGITLAB_TOKEN}
        git_repo: ${MYGITLAB_REPO}
- stage:
    - gitlab_tags:
      - ~options
      - search: "2.110.0.1"
    - print: tags
"""
    )


def test_3(main, request):
    main(
        text="""
- options:
    - in:
        # Подключение к gitlab
        git_url: ${MYGITLAB_URL}
        git_token: ${MYGITLAB_TOKEN}
        git_repo: ${MYGITLAB_REPO}
- stage:
    # Вывести только major release
    - gitlab_tags:
      - ~options
      - regex: '\\d+\\.\\d+\\.0\\.0'
    - print: tags
"""
    )
