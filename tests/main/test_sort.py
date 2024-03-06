import pytest

@pytest.fixture()
def arr_ints2():
    return {"ints": [x for x in range(0, 4)]}

def test_normal(main, arr_ints2, arr_strings):
  assert main(datas = arr_ints2, text = """
- in: ~ints
- sort
""").queue == [0, 1, 2, 3]

def test_asc(main, arr_ints2, arr_strings):
  assert main(datas = arr_ints2, text = """
- in: ~ints
- sort: asc
""").queue == [0, 1, 2, 3]

def test_desc(main, arr_ints2, arr_strings):
  assert main(datas = arr_ints2, text = """
- in: ~ints
- sort: desc
""").queue == [3, 2, 1, 0]

def test_diff(main, arr_ints, arr_strings):
  with pytest.raises(Exception) as e_info:
    assert main(datas = arr_ints, text = """
- in: ~ints
- sort
""")
  assert "'<' not supported between instances of 'str' and 'int'" in str(e_info.value)

def test_str_asc(main, arr_strings):
  assert main(datas = arr_strings, text = """
- in: ~strings
- sort
""").queue == ['Восемь', 'Два', 'Девять', 'Десять', 'Один', 'Пять', 'Семь', 'Три', 'Четыре', 'Шесть']

def test_str_desc(main, arr_strings):
  assert main(datas = arr_strings, text = """
- in: ~strings
- sort: desc
""").queue == ['Шесть', 'Четыре', 'Три', 'Семь', 'Пять', 'Один', 'Десять', 'Девять', 'Два', 'Восемь']
