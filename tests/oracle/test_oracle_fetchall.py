def test_1(main):
    pgm = main(
        text="""
main:
- in: |
    select 'EMAIL' code from dual union select 'FAX' code from dual
    union select 'NONE' code from dual
- oracle_fetchall:
    oracle_dsn: ${ORACLE_HOST}
    oracle_user: ${ORACLE_USER}
    oracle_password: ${ORACLE_PASSWORD}
- attr: code
- sort
"""
    )
    assert pgm.get_queue() == ["EMAIL", "FAX", "NONE"]


def test_2(main):
    pgm = main(
        text="""
main:
- in:
  - select 'EMAIL' code from dual
  - select 'FAX' code from dual
  - select 'NONE' code from dual
- oracle_fetchall:
    oracle_dsn: ${ORACLE_HOST}
    oracle_user: ${ORACLE_USER}
    oracle_password: ${ORACLE_PASSWORD}
- attr: code
- sort
"""
    )
    assert pgm.get_queue() == ["EMAIL", "FAX", "NONE"]


def test_3(main):
    pgm = main(
        text="""
main:
- in: /tests/oracle/sql/test0.sql
- oracle_fetchall:
    oracle_dsn: ${ORACLE_HOST}
    oracle_user: ${ORACLE_USER}
    oracle_password: ${ORACLE_PASSWORD}
    path:
- attr: code
- sort
"""
    )
    assert pgm.get_queue() == ["EMAIL", "FAX", "NONE"]


def test_4(main):
    pgm = main(
        text="""
main:
- in:
  - test1
  - test2
  - test3
- oracle_fetchall:
    oracle_dsn: ${ORACLE_HOST}
    oracle_user: ${ORACLE_USER}
    oracle_password: ${ORACLE_PASSWORD}
    path: "/tests/oracle/sql/:1.sql"
- attr: code
- sort
"""
    )
    assert pgm.get_queue() == ["EMAIL", "FAX", "NONE"]
