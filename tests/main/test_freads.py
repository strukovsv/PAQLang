import pytest

def test_1(main):
  assert main(text = """
- in: 
  - ../tests/main/data/file4.txt
  - ../tests/main/data/file5.txt
- freads
- print: filename             
- split:
    attr: text         
- print                  
""").queue == ["test1", "test2", "test3", "test4", "test5", "test6", "test7"]
  
def test_2(main):
  assert main(text = """
- in: 
  - ../tests/main/data/file4.txt
- freads:
    split:
- print                  
""").queue == ["test1", "test2", "test3", "test4"]

def test_3(main):
  assert main(text = """
- in: 
  - ../tests/main/data/file1.txt
- freads:
    split: ';'
- print                  
""").queue == ["test1", "test2", "test3", "test4"]

def test_4(main):
  assert main(text = """
- in: 
  - ../tests/main/data/file2.yml
- freads:
    to_json:
- print                  
""").queue == [{'sub1': {'sleep': 0.2}, 'sub2': {'sleep': 0.4}}]

def test_5(main):
  assert main(text = """
- in: 
  - ../tests/main/data/file3.yml
- freads:
    to_json:
- print                  
""").queue == [{'sub1': {'sleep': 0.2}}, {'sub2': {'sleep': 0.4}}]
