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
    git_url: ${MYGITLAB_URL}
    git_token: ${MYGITLAB_TOKEN}
    git_repo: ${MYGITLAB_REPO}
    git_branch: master
- print
"""
    )
    assert len(pgm.queue) == 1
