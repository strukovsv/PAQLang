def test_5(main):
    pgm = main(
        text="""
main:
- in:
  - Packages/utl.pck
- oracle_execute:
    oracle_dsn: ${ORACLE_HOST}
    oracle_user: ${ORACLE_USER}
    oracle_password: ${ORACLE_PASSWORD}
    git_url: ${GIT_URL}
    git_token: ${GIT_TOKEN}
    git_repo: ${GIT_REPO}
    git_branch: master
- print
"""
    )
    assert len(pgm.queue) == 1
