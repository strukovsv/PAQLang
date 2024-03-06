import pytest

def test_1(main, request):
  pgm = main(text = """
- options:
    - in: 
        # Подключение к gitlab
        git_url: ${GIT_URL}
        git_token: ${GIT_TOKEN}
        git_repo: ${GIT_REPO}
- stage:
    - gitlab_branches:
      - ~options 
      - regex: 'feature/.*'             
    - print: branches
""")
  assert len(pgm.queue) > 1

def test_2(main, request):
  pgm = main(text = """
- options:
    - in: 
        # Подключение к gitlab
        git_url: ${GIT_URL}
        git_token: ${GIT_TOKEN}
        git_repo: ${GIT_REPO}
- stage:
    - gitlab_branches:
      - ~options 
      - search: master
    - print: branches
""")
  assert len(pgm.queue) == 1