def test_1(main, request):
    main(
        text="""
- options:
    - in:
        # Кол-во потоков обработки операций gitlab
        tasks: 10
        # Подключение к gitlab
        git_url: ${MYGITLAB_URL}
        git_token: ${MYGITLAB_TOKEN}
        git_repo: ${MYGITLAB_REPO}
- stage:
    - in:
      - "Functions"
      - "Procedures"
    - gitlab_walk:
      - ~options
      - git_branch: master
    - print
"""
    )


def test_2(main, request):
    main(
        text="""
- options:
    - in:
        # Кол-во потоков обработки операций gitlab
        tasks: 10
        # Подключение к gitlab
        git_url: ${MYGITLAB_URL}
        git_token: ${MYGITLAB_TOKEN}
        git_repo: ${MYGITLAB_REPO}
- stage:
    - in:
      - "Functions"
      - "Procedures"
    - gitlab_walk:
      - ~options
      - git_branch: master
      - regex: "^.+/tmp_.+$"
    - print
"""
    )
