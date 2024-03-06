import pytest

def test_1(main):
    pgm = main(text = """
stages:
- stage1:
    do:
    - in:
- stage2:
    do:
    - in: 1
- stage3:
    do:
    - in:
        - 1
        - 2
- stage4:
    do:
    - in:
        - 1
        - 'test2'
""")
    assert pgm.get_data("stage1") == []
    assert pgm.get_data("stage2") == [1]
    assert pgm.get_data("stage3") == [1, 2]
    assert pgm.get_data("stage4") == [1, 'test2']

def test_ref(main):
    pgm = main(text = """
stages:
- stage1:
    do:
    - in: 
        - 1
        - 2
- stage01:
    do:
    - in: 
        - 3
        - 4
- stage2:
    do:
    - in: 
- stage3:
    do:
    - in: ~stage1
- stage4:
    do:
    - in: 
        - ~stage01
- stage5:
    do:
    - in: 
        - ~stage1
        - ~stage01
""")
    assert pgm.get_data("stage1") == [1, 2]
    assert pgm.get_data("stage2") == []
    assert pgm.get_data("stage3") == [1, 2]
    assert pgm.get_data("stage4") == [3, 4]
    assert pgm.get_data("stage5") == [1, 2, 3, 4]
