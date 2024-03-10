import pytest

def test_1(main):
    pgm = main(text = '''
main:
- in: |
    begin
      dbms_output.put_line('test dbms_output - 1');
    end;            
    /           
    begin
      dbms_output.put_line('test dbms_output - 2');
    end;            
- oracle_execute:
    oracle_dsn: ${ORACLE_HOST}
    oracle_user: ${ORACLE_USER}
    oracle_password: ${ORACLE_PASSWORD}
- print               
''')
    assert pgm.queue == [{'result': 1, 'output': 'test dbms_output - 1\ntest dbms_output - 2'}]

def test_2(main):
    pgm = main(text = '''
main:
- in: 
  - |
        begin
          dbms_output.put_line('test dbms_output - 1');
        end;            
  - |
        begin
          dbms_output.put_line('test dbms_output - 2');
        end;            
- oracle_execute:
    oracle_dsn: ${ORACLE_HOST}
    oracle_user: ${ORACLE_USER}
    oracle_password: ${ORACLE_PASSWORD}
- print               
''')
    assert len(pgm.queue) == 2

def test_3(main):
    pgm = main(text = '''
main:
- in: /tests/oracle/sql/test4.sql
- oracle_execute:
    oracle_dsn: ${ORACLE_HOST}
    oracle_user: ${ORACLE_USER}
    oracle_password: ${ORACLE_PASSWORD}
    path:           
- print               
''')
    assert pgm.queue[0]["output"] == 'test dbms_output - 1\ntest dbms_output - 2'

def test_4(main):
    pgm = main(text = '''
main:
- in: 
  - test5
  - test6
  - test7
- oracle_execute:
    oracle_dsn: ${ORACLE_HOST}
    oracle_user: ${ORACLE_USER}
    oracle_password: ${ORACLE_PASSWORD}
    path: "/tests/oracle/sql/:1.sql"           
- print               
''')
    assert len(pgm.queue) == 3

def test_5(main):
    pgm = main(text = '''
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
''')
    assert len(pgm.queue) == 1
