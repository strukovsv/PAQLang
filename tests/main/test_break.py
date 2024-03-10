import pytest

def test_break1(main, request):
  pgm = main(text = '''
main:
- in: 0
- out: cnt_result
- while:         
  - break:
    - in: ~cnt_result
    - eq: 5
  - inc: cnt_result           
  - print    
    ''')#, name = request.node.name)
  assert pgm.get_data("cnt_result") == [5]

def test_break2(main, request):
  pgm = main(text = '''
main:
- in: 0
- out: cnt_result
- while:       
    stage0:             
    - break:
      - in: ~cnt_result
      - eq: 5
    - inc: cnt_result           
    - print    
    ''')#, name = request.node.name)
  assert pgm.get_data("cnt_result") == [5]

def test_break3(main, request):
  pgm = main(text = '''
main:
- in: 0
- out: cnt_result
- while:       
    stage0:             
    - break:
      - in: ~cnt_result
      - eq: 10
    - inc: cnt_result           
    - print: stage0
    stage1:             
    - break:
      - in: ~cnt_result
      - eq: 10
    - inc: cnt_result           
    - print: stage1
    ''')#, name = request.node.name)
  assert pgm.queue == [9, 10]
  assert pgm.get_data("cnt_result") == [10]

def test_pop(main):
  assert main(text = """
- in: [1, 2, 3, 4, 5]
- out: cnt
- while:
    - pop: cnt
    - break
    - print: cycle                  
""").queue == [1]
