import pytest

def test_empty(main):
    pgm = main(text = """
stages:
- stage1:
    in:
""")
    assert pgm.get_data("stage1") == []

def test_int(main):
    pgm = main(text = """
stages:
- stage1:
    in: 1
- stage2:
    in: 
    - 1
- stage3:
    in: 
    - 1
    - 2
- stage4:
    in: 
    - 1
    - 2
    -
""")
    assert pgm.get_data("stage1") == [1]
    assert pgm.get_data("stage2") == [1]
    assert pgm.get_data("stage3") == [1, 2]
    assert pgm.get_data("stage4") == [1, 2, None]

def test_str(main):
    pgm = main(text = """
stages:
- stage1:
    in: 'test'
- stage2:
    in: 
    - 'test'
- stage3:
    in: 
    - 'test1'
    - 'test2'
- stage4:
    in: 
    - 'test1'
    - 'test2'
    -
""")
    assert pgm.get_data("stage1") == ['test']
    assert pgm.get_data("stage2") == ['test']
    assert pgm.get_data("stage3") == ['test1', 'test2']
    assert pgm.get_data("stage4") == ['test1', 'test2', None]

def test_dict(main):
    pgm = main(text = """
stages:
- stage1:
    in: 
        'test1': 1
        'test2': 2
- stage2:
    in: 
    - 'test1': 1
      'test2': 2
- stage3:
    in: 
    - 'test1': 1
      'test2': 2
    - 'test1': 3
      'test2': 4
- stage4:
    in: 
    - 'test1': 1
    - 'test2': 4
""")
    assert pgm.get_data("stage1") == [{'test1': 1, 'test2': 2}]
    assert pgm.get_data("stage2") == [{'test1': 1, 'test2': 2}]
    assert pgm.get_data("stage3") == [{'test1': 1, 'test2': 2}, {'test1': 3, 'test2': 4}]
    assert pgm.get_data("stage4") == [{'test1': 1}, {'test2': 4}]

def test_ref(main):
    pgm = main(text = """
stages:
- stage1:
    in: 
        - 1
        - 2
- stage01:
    in: 
        - 3
        - 4
- stage2:
    in:
- stage3:
    in: ~stage1
- stage4:
    in: 
    - ~stage01
- stage5:
    in: 
    - ~stage1
    - ~stage01
""")
    assert pgm.get_data("stage1") == [1, 2]
    assert pgm.get_data("stage2") == []
    assert pgm.get_data("stage3") == [1, 2]
    assert pgm.get_data("stage4") == [3, 4]
    assert pgm.get_data("stage5") == [1, 2, 3, 4]
