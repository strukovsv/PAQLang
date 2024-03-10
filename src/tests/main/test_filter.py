import pytest

@pytest.fixture()
def arr_ints():
    return {"ints": [x for x in range(0, 10)] + ["error_value"]}

@pytest.fixture()
def arr_ints_dict():
    return {"ints": [{"value": x} for x in range(0, 10)] + [{"value": "error_value"}]}

def test_eq(main, arr_ints):
  assert main(datas = arr_ints, text = """
- in: ~ints
- filter:
    eq: 5                      
""").queue == [5]

def test_ne(main, arr_ints):
  assert main(datas = arr_ints, text = """
- in: ~ints
# исключить из списка 5
- filter:
    ne: 5                      
""").get_queue() == [0, 1, 2, 3, 4, 6, 7, 8, 9, "error_value"]

def test_lt(main, arr_ints):
  assert main(datas = arr_ints, text = """
- in: ~ints
- filter:
    lt: 5                      
""").get_queue() == [0, 1, 2, 3, 4]

def test_le(main, arr_ints):
  assert main(datas = arr_ints, text = """
- in: ~ints
- filter:
    le: 5                      
""").get_queue() == [0, 1, 2, 3, 4, 5]

def test_gt(main, arr_ints):
  assert main(datas = arr_ints, text = """
- in: ~ints
- filter:
    gt: 5                      
""").get_queue() == [6, 7, 8, 9, "error_value"]

def test_ge(main, arr_ints):
  assert main(datas = arr_ints, text = """
- in: ~ints
- filter:
    ge: 5                      
""").get_queue() == [5, 6, 7, 8, 9, "error_value"]

def test_between_eq(main, arr_ints):
  assert main(datas = arr_ints, text = """
- in: ~ints
- filter:
    ge: 2                      
    le: 7                      
""").get_queue() == [2, 3, 4, 5, 6, 7]

def test_between_ne(main, arr_ints):
  assert main(datas = arr_ints, text = """
- in: ~ints
- filter:
    gt: 2                      
    lt: 7                      
""").get_queue() == [3, 4, 5, 6]

def test_dict_eq(main, arr_ints_dict):
  assert main(datas = arr_ints_dict, text = """
- in: ~ints
- filter:
    attr: value          
    eq: 5          
""").get_queue() == [{"value": 5}]

def test_float(main):
  assert main(text = """
- in: 
  - 1.5
  - 2.3456            
- filter:
    eq: 2.3456          
""").get_queue() == [2.3456]

def test_dict_error_attr(main, arr_ints_dict):
  # with pytest.raises(Exception) as e_info:
  assert main(datas = arr_ints_dict, text = """
- in: ~ints
- filter:
    attr: name          
    eq: 5          
""").queue == []
  # assert 'Не найден атрибут' in str(e_info.value)  

def test_dict_eq_1(main, arr_ints_dict):
  assert main(datas = arr_ints_dict, text = """
- in: 
  - {"a": 10, "b": 11}
  - {"a": 11, "b": 11}
  - {"b": 11}
- filter:
    attr: a          
    eq: 11          
""").get_queue() == [{"a": 11, "b": 11}]
