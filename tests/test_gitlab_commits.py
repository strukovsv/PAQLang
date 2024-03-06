import pytest

def test_two(main_gitlab, request):
  pgm = main_gitlab(text = """
- options:
    - in: 
        # Кол-во потоков обработки операций gitlab и oracle
        tasks: 10
        # Подключение к gitlab
        git_url: ${GIT_URL}
        git_token: ${GIT_TOKEN}
        git_repo: ${GIT_REPO}
- stage:

    - in: tests/2.133.0.0          
    - gitlab_commits:
      - ~options
      - since: "20240305"
    - print
""")

