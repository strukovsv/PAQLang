def test_3(main, request):
    main(
        text="""
- options:
    - in:
        # Подключение к github
        git_owner: ${GITHUB_OWNER}
        git_token: ${GITHUB_TOKEN}
        git_repo: ${GITHUB_REPO}
- stage:
    - in: master
    - github_commits:
      - ~options
      - since: "2024-03-15T02:53:00"
    - attr:
      - id
      - last_message
    - print
    - github_diff:
      - ~options
    - distinct
    - print
"""
    )
