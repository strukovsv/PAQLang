def test_3(main, request):
    main(
        text="""
- options:
    - in:
        # Кол-во потоков обработки операций gitlab и oracle
        tasks: 10
        # Подключение к gitlab
        git_url: ${MYGITLAB_URL}
        git_token: ${MYGITLAB_TOKEN}
        git_repo: ${MYGITLAB_REPO}
- stage:
    - in: tests/2.133.0.0
    - gitlab_commits:
      - ~options
      - since: "2024-03-05T10:20:00"
    - gitlab_diff:
      - ~options
    - distinct
    - print
"""
    )
