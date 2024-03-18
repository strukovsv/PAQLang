def test_1(main):
    assert (
        main(
            text="""
- in:
  - ../tests/main/data/file4.txt
  - ../tests/main/data/file5.txt
- freads
- print: filename
- split:
    attr: text
- print
"""
        ).queue
        == ["test1", "test2", "test3", "test4", "test5", "test6", "test7"]
    )


def test_2(main):
    assert (
        main(
            text="""
- in:
  - ../tests/main/data/file4.txt
- freads:
    split:
- print
"""
        ).queue
        == ["test1", "test2", "test3", "test4"]
    )


def test_3(main):
    assert (
        main(
            text="""
- in:
  - ../tests/main/data/file1.txt
- freads:
    split: ';'
- print
"""
        ).queue
        == ["test1", "test2", "test3", "test4"]
    )


def test_4(main):
    assert (
        main(
            text="""
- in:
  - ../tests/main/data/file2.yml
- freads:
    to_json:
- print
"""
        ).queue
        == [{"sub1": {"sleep": 0.2}, "sub2": {"sleep": 0.4}}]
    )


def test_5(main):
    assert (
        main(
            text="""
- in:
  - ../tests/main/data/file3.yml
- freads:
    to_json:
- print
"""
        ).queue
        == [{"sub1": {"sleep": 0.2}}, {"sub2": {"sleep": 0.4}}]
    )


def test_github(main):
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
      - ".github/workflows/pytest.yml"
      - "requirements.txt"
    # Прочитать два файла в два асинхронных потока
    - freads:
      - ~options
      - git_branch: master
      - split
    - print
"""
    )


def test_github_path(main):
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
      - "add"
      - "sub"
      - "mul"
      - "div"
    # Прочитать два файла в два асинхронных потока
    - freads:
      - ~options
      - git_branch: master
      - path: "tests/main/test_:1.py"
      - split:
    - print
"""
    )


def test_github_json(main):
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
      - ".github/workflows/pytest.yml"
    # Прочитать два файла в два асинхронных потока
    - freads:
      - ~options
      - git_branch: master
      - to_json:
    - print
"""
    )


# # Нет доступных gitlab серверов
# # тестирую на личном
# def test_gitlab(main, request):
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
#       - ".gitignore"
#       - ".gitlab-ci.yml"
#     # Прочитать два файла в два асинхронных потока
#     - freads:
#       - ~options
#       - git_branch: master
#       - split:
#     - print
# """
#     )
