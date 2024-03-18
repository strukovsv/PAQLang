def test_3(main):
    pgm = main(
        text="""
main:
- in: tests/oracle/sql/test4.sql
- oracle_execute:
    oracle_dsn: ${ORACLE_HOST}
    oracle_user: ${ORACLE_USER}
    oracle_password: ${ORACLE_PASSWORD}
    git_owner: ${MYGITHUB_OWNER}
    git_token: ${MYGITHUB_TOKEN}
    git_repo: ${MYGITHUB_REPO}
    git_branch: master
    path:
- print
"""
    )
    assert (
        pgm.queue[0]["output"] == "test dbms_output - 1\ntest dbms_output - 2"
    )


def test_4(main):
    pgm = main(
        text="""
main:
- in:
  - test5
  - test6
  - test7
- oracle_execute:
    oracle_dsn: ${ORACLE_HOST}
    oracle_user: ${ORACLE_USER}
    oracle_password: ${ORACLE_PASSWORD}
    git_owner: ${MYGITHUB_OWNER}
    git_token: ${MYGITHUB_TOKEN}
    git_repo: ${MYGITHUB_REPO}
    git_branch: master
    path: "tests/oracle/sql/:1.sql"
- print
"""
    )
    assert len(pgm.queue) == 3
