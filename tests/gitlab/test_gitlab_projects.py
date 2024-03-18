def test_1(main, request):
    pgm = main(
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
    - gitlab_projects:
      - ~options
    - print: projects
"""
    )
    assert len(pgm.queue) > 1


def test_2(main, request):
    pgm = main(
        text="""
- options:
    - in:
        # Кол-во потоков обработки операций gitlab и oracle
        tasks: 10
        # Подключение к gitlab
        git_url: ${MYGITLAB_URL}
        git_token: ${MYGITLAB_TOKEN}
- repo:
  - in: ${MYGITLAB_REPO}
- stage:
    - gitlab_projects:
      - ~options
      - search: ~repo
    - print: project repo
"""
    )
    assert len(pgm.queue) == 1


def test_3(main, request):
    pgm = main(
        text="""
- options:
    - in:
        # Кол-во потоков обработки операций gitlab и oracle
        tasks: 10
        # Подключение к gitlab
        git_url: ${MYGITLAB_URL}
        git_token: ${MYGITLAB_TOKEN}
- stage:
    - gitlab_projects:
      - ~options
      - regex: '^ora.*$'
    - print: project ARGIS
"""
    )
    assert len(pgm.queue) > 0


def test_4(main, request):
    pgm = main(
        text="""
- options:
    - in:
        # Кол-во потоков обработки операций gitlab и oracle
        tasks: 10
        # Подключение к gitlab
        git_url: ${MYGITLAB_URL}
        git_token: ${MYGITLAB_TOKEN}
- stage:
    - gitlab_projects:
      - ~options
      - regex: '^NOT.*$'
    - print: not projects
"""
    )
    assert len(pgm.queue) == 0
