import pytest

def test_1(main_gitlab, request):
  pgm = main_gitlab(text = """
- options:
    - in: 
        # Подключение к gitlab
        git_url: ${GIT_URL}
        git_token: ${GIT_TOKEN}
        git_repo: ${GIT_REPO}
- stage:
    - gitlab_tags:
      - ~options 
    - print: tags
""")

def test_2(main_gitlab, request):
  pgm = main_gitlab(text = """
- options:
    - in: 
        # Подключение к gitlab
        git_url: ${GIT_URL}
        git_token: ${GIT_TOKEN}
        git_repo: ${GIT_REPO}
- stage:
    - gitlab_tags:
      - ~options 
      - search: "2.110.0.1"       
    - print: tags
""")

def test_3(main_gitlab, request):
  pgm = main_gitlab(text = """
- options:
    - in: 
        # Подключение к gitlab
        git_url: ${GIT_URL}
        git_token: ${GIT_TOKEN}
        git_repo: ${GIT_REPO}
- stage:
    # Вывести только major release         
    - gitlab_tags:
      - ~options 
      - regex: '\\d+\\.\\d+\\.0\\.0'       
    - print: tags
""")
