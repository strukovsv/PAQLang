import pytest

def test_one(main, arr_strings):
  assert main(datas = arr_strings, text = """
- in: ~strings
- replace: 
    regex: ять
    dest: "123"
""").queue == ['Один', 'Два', 'Три', 'Четыре', 'П123', 'Шесть', 'Семь', 'Восемь', 'Дев123', 'Дес123']

def test_two(main, arr_strings):
  assert main(datas = arr_strings, text = """
- in: ~strings
- replace: ять
""").queue == ['Один', 'Два', 'Три', 'Четыре', 'П', 'Шесть', 'Семь', 'Восемь', 'Дев', 'Дес']

def test_attr_error(main, arr_dict_strings):
  with pytest.raises(Exception) as e_info:
    assert main(datas = arr_dict_strings, text = """
- in: ~strings
- replace
""")  
  assert 'Не задан атрибут поиска "regex"' in str(e_info.value)  
