def test_1(main):
    main(
        text="""
- options:
    - in:
        # Подключение к github
        git_owner: ${GITHUB_OWNER}
        git_token: ${GITHUB_TOKEN}
        git_repo: ${GITHUB_REPO}
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
