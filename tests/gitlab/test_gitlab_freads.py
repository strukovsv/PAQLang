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
      - ".gitignore"
      - ".gitlab-ci.yml"
    # Прочитать два файла в два асинхронных потока
    - gitlab_freads:
      - ~options
      - git_branch: master
    - print
"""
    )
