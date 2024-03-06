import pytest

def test_1(main_gitlab, request):
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
    - gitlab_projects:
      - ~options
    - print: projects       
""")
  assert len(pgm.queue) > 1

def test_2(main_gitlab, request):
  pgm = main_gitlab(text = """
- options:
    - in: 
        # Кол-во потоков обработки операций gitlab и oracle
        tasks: 10
        # Подключение к gitlab
        git_url: ${GIT_URL}
        git_token: ${GIT_TOKEN}
- repo:
  - in: ${GIT_REPO}
- stage:
    - gitlab_projects:
      - ~options
      - search: ~repo
    - print: project repo       
""")
  assert len(pgm.queue) == 1

def test_3(main_gitlab, request):
  pgm = main_gitlab(text = """
- options:
    - in: 
        # Кол-во потоков обработки операций gitlab и oracle
        tasks: 10
        # Подключение к gitlab
        git_url: ${GIT_URL}
        git_token: ${GIT_TOKEN}
- stage:
    - gitlab_projects:
      - ~options
      - regex: '^ora.*$'
    - print: project ARGIS       
""")
  assert len(pgm.queue) > 0

def test_4(main_gitlab, request):
  pgm = main_gitlab(text = """
- options:
    - in: 
        # Кол-во потоков обработки операций gitlab и oracle
        tasks: 10
        # Подключение к gitlab
        git_url: ${GIT_URL}
        git_token: ${GIT_TOKEN}
- stage:
    - gitlab_projects:
      - ~options
      - regex: '^NOT.*$'
    - print: not projects
""")
  assert len(pgm.queue) == 0

