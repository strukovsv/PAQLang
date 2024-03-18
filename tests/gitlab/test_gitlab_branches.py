def test_1(main, request):
    pgm = main(
        text="""
- options:
    - in:
        # Подключение к gitlab
        git_url: ${MYGITLAB_URL}
        git_token: ${MYGITLAB_TOKEN}
        git_repo: ${MYGITLAB_REPO}
- stage:
    - gitlab_branches:
      - ~options
      - regex: 'feature/.*'
    - print: branches
"""
    )
    assert len(pgm.queue) > 1


def test_2(main, request):
    pgm = main(
        text="""
- options:
    - in:
        # Подключение к gitlab
        git_url: ${MYGITLAB_URL}
        git_token: ${MYGITLAB_TOKEN}
        git_repo: ${MYGITLAB_REPO}
- stage:
    - gitlab_branches:
      - ~options
      - search: master
    - print: branches
"""
    )
    assert len(pgm.queue) == 1
