import pytest

def test_one(main, arr_strings):
  assert main(datas = arr_strings, text = """
- in: ~strings
- match: .*(ять).*                      
""").queue == ['ять', 'ять', 'ять']

def test_one_regex(main, arr_strings):
  assert main(datas = arr_strings, text = """
- in: ~strings
- match: 
    regex: .*(ять).*                      
""").queue == ['ять', 'ять', 'ять']

def test_two(main, arr_strings):
  assert main(datas = arr_strings, text = """
- in: ~strings
- match: я                      
""").queue == []
