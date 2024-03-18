def test_1(main):
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
    - github_walk:
      - ~options
      - git_branch: master
    - attr: path
    - print
"""
    )


def test_2(main):
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
    - github_walk:
      - ~options
      - git_branch: master
    - attr: path
    - print
"""
    )


def test_3(main):
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
    - github_walk:
      - ~options
      - git_branch: master
    - attr: path
    - print
"""
    )


def test_4(main):
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
    - github_walk:
      - ~options
      - git_branch: master
      - regex: '.*workflow.*'
    - attr: sha
    - print
"""
    )
