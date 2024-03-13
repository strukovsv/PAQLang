# import pytest
# import os
# import logging


def test_call(main, request):
    pgm = main(
        text="""
main:
# sub1:                                  
#   sleep: 0.2
# sub2:                                  
#   sleep: 0.4
- lib:
    # Загрузить библиотеки из файла
    - in: "../tests/main/data/lib1.yaml"
    - include
- stage1:
    stg1:
      - call: sub1
    stg2:
      - call: sub2
""",
        request=request,
    )
    assert 0.35 < pgm.get_seconds()
    assert pgm.get_seconds() < 0.45


def test_macros(main, request):
    pgm = main(
        text="""
macros:               
  sub1:
    sub11:                                  
      sleep: 0.2
    sub12:                                  
      sleep: 0.4
  sub2:
    sleep: 0.5
  sub3:
    sleep: 0.8
main:
- stage1:
    stage11:           
      call: sub1
    stage12:           
      call: sub2
    stage13:           
      call: sub3
""",
        request=request,
    )
    assert pgm.queue == []
    assert 0.8 < pgm.get_seconds()
    assert pgm.get_seconds() < 0.9


def test_macros_include(main, request):
    pgm = main(
        text="""
macros:               
  sub1:                                  
    sleep: 0.1
  sub2:                                  
    sleep: 0.2
main:
- lib:
    # sub1:                                  
    #   sleep: 0.2
    # sub2:                                  
    #   sleep: 0.4
    # Загрузить библиотеки из файла
    - in: "../tests/main/data/lib1.yaml"
    - include
- stage1:
    stg1:
      - call: sub1
    stg2:
      - call: sub2
""",
        request=request,
    )
    assert 0.35 < pgm.get_seconds()
    assert pgm.get_seconds() < 0.5
