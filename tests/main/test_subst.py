import pytest

def test_one(main):
  assert main(text = """
- in: 
  - 0
  - 15
  - test                        
- subst: =:1= 
""").queue == ['=0=', '=15=', '=test=']
  
def test_two(main):
  assert main(text = """
- in: 
  - 0
  - 15
  - test                        
- subst: 
    text: =:1= 
""").queue == ['=0=', '=15=', '=test=']  
  
def test_attr_error(main, arr_dict_strings):
  with pytest.raises(Exception) as e_info:
    assert main(text = """
- in: 
  - 0
  - 15
  - test                        
- subst:
""")  
  assert 'Не задана исходная строка - шаблон' in str(e_info.value)  
