import pytest

def test_1(main_gitlab, request):
  pgm = main_gitlab(text = """
- options:
    - in: 
        # Кол-во потоков обработки операций gitlab
        tasks: 10
        # Подключение к gitlab
        git_url: ${GIT_URL}
        git_token: ${GIT_TOKEN}
        git_repo: ${GIT_REPO}
- stage:
    - in:
      - ".gitignore"
      - ".gitlab-ci.yml"
    # Прочитать два файла в два асинхронных потока         
    - gitlab_freads:
      - ~options
      - git_branch: master     
    - print         
""")
