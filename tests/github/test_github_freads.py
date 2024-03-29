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
      - ".github/workflows/pytest.yml"
      - "requirements.txt"
    # Прочитать два файла в два асинхронных потока
    - github_freads:
      - ~options
      - git_branch: master
    - attr: text
    - split
    - print
"""
    )
