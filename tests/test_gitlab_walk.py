import pytest

def test_1(main, request):
  pgm = main(text = """
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
      - "Functions"
      - "Procedures"       
    - gitlab_walk:
      - ~options
      - git_branch: master     
    - print         
""")

def test_2(main, request):
  pgm = main(text = """
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
      - "Functions"
      - "Procedures"       
    - gitlab_walk:
      - ~options
      - git_branch: master     
      - regex: "^.+/tmp_.+$"
    - print         
""")
