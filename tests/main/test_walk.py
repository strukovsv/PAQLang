def test_one(main, request):
    main(
        text="""
- in: /tests
- walk:
    regex: "^/tests/main/test_n.*py$"
- print: "walk"
"""
    )


def test_two(main, request):
    main(
        text="""
- in:
  - /tests/main/data
  - /tests/.pytest_cache
- walk:
- print: "walk"
"""
    )


def test_github_1(main):
    main(
        text="""
- options:
    - in:
        # Подключение к github
        git_owner: ${MYGITHUB_OWNER}
        git_token: ${MYGITHUB_TOKEN}
        git_repo: ${MYGITHUB_REPO}
- stage:
    - in:
      - ".github"
      - "docs"
    - walk:
      - ~options
      - git_branch: master
    - print
"""
    )


def test_github_2(main):
    main(
        text="""
- options:
    - in:
        # Подключение к github
        git_owner: ${MYGITHUB_OWNER}
        git_token: ${MYGITHUB_TOKEN}
        git_repo: ${MYGITHUB_REPO}
- stage:
    - in:
      - ""
    - walk:
      - ~options
      - git_branch: master
    - print
"""
    )


def test_github_3(main):
    main(
        text="""
- options:
    - in:
        # Подключение к github
        git_owner: ${MYGITHUB_OWNER}
        git_token: ${MYGITHUB_TOKEN}
        git_repo: ${MYGITHUB_REPO}
- stage:
    - in: "/"
    - walk:
      - ~options
      - git_branch: master
    - print
"""
    )


def test_github_4(main):
    main(
        text="""
- options:
    - in:
        # Подключение к github
        git_owner: ${MYGITHUB_OWNER}
        git_token: ${MYGITHUB_TOKEN}
        git_repo: ${MYGITHUB_REPO}
- stage:
    - in:
      - ""
    - walk:
      - ~options
      - git_branch: master
      - regex: '.*workflow.*'
    - attr: sha
    - print
"""
    )


# def test_gitlab_1(main, request):
#     main(
#         text="""
# - options:
#     - in:
#         # Подключение к gitlab
#         git_url: ${MYGITLAB_URL}
#         git_token: ${MYGITLAB_TOKEN}
#         git_repo: ${MYGITLAB_REPO}
# - stage:
#     - in:
#       - "Functions"
#       - "Procedures"
#     - walk:
#       - ~options
#       - git_branch: master
#     - print
# """
#     )
