def test_1(main):
    pgm = main(
        text="""
- options:
    - in:
        # Кол-во потоков обработки операций gitlab и oracle
        tasks: 10
        # Подключение к github
        git_owner: ${MYGITHUB_OWNER}
        git_token: ${MYGITHUB_TOKEN}
        git_repo: ${MYGITHUB_REPO}
- stage:
    - github_projects:
      - ~options
    - print: projects
"""
    )
    assert len(pgm.queue) > 1


def test_2(main):
    main(
        text="""
- options:
    - in:
        # Подключение к gitub
        git_owner: ${MYGITHUB_OWNER}
        git_token: ${MYGITHUB_TOKEN}
        git_repo: ${MYGITHUB_REPO}
- stage:
    - github_projects:
      - ~options
      - regex: 'P.*$'
    - print: project with P
"""
    )
