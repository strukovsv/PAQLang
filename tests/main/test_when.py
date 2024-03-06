import pytest

def test_when1(main, request):
  pgm = main(text = '''
main:
  stage1:    
  # Пустая очередь, when не выполнится
  - when
  - in: 10
  stage2:         
  - in: 20
    ''')#, name = request.node.name)
  # pgm.save_stack(request)  
  assert pgm.queue == [20]

def test_when2(main, request):
  pgm = main(text = '''
main:
  stage1: 
  - in: 10        
  - when:
      eq: 10
  - in: 15
  stage2:         
  - in: 20
    ''')#, name = request.node.name)
  # pgm.save_stack(request)  
  assert pgm.queue == [15, 20]

def test_when3(main, request):
  pgm = main(text = '''
main:
- stage0:
  - in: 10
  - out: test                                   
- stage1: 
  - in: 25        
  - when:
      in: ~test
      eq: 10
  - in: 15
  stage2:         
  - in: 20
    ''')#, name = request.node.name)
  # pgm.save_stack(request)  
  assert pgm.queue == [15, 20]

def test_when4(main, request):
  pgm = main(text = '''
main:
- stage0:
  - in: 10
  - out: test                                   
- stage1: 
  - in: 25      
  # 10 не равно None             
  - when:
      in: ~test
      eq:
  - in: 15
  stage2:         
  - in: 20
    ''')#, name = request.node.name)
  assert pgm.queue == [20]

def test_when5(main, request):
  pgm = main(text = '''
main:
- stage1: 
  - in: 25      
  # 25 < 30, то должно выполнится
  - when:
      lt: 30
  - in: 15
  stage2:         
  - in: 20
    ''')
  assert pgm.queue == [15, 20]

def test_when6(main, request):
  pgm = main(text = '''
main:
- stage1: 
  - in: 30      
  # 30 < 30, не выполнится
  - when:
      lt: 30
  - in: 15
  stage2:         
  - in: 20
    ''')
  assert pgm.queue == [20]

def test_when7(main, request):
  pgm = main(text = '''
main:
- stage1: 
  - in: 30      
  # 25 < 30 < 35, то должно выполнится
  - when:
      gt: 25
      lt: 35
  - in: 15
  stage2:         
  - in: 20
    ''')
  assert pgm.queue == [15, 20]

def test_when8(main, request):
  pgm = main(text = '''
main:
- stage1: 
  - in: 30      
  # 30 != 20
  - when:
      ne: 20
  - in: 15
  stage2:         
  - in: 20
    ''')
  assert pgm.queue == [15, 20]

def test_when9(main, request):
  pgm = main(text = '''
main:
- stage1: 
  - in: 'strukov'      
  # 'strukov' in 'strukov sergey'
  - when:
      instr: strukov sergey
  - in: 15
  stage2:         
  - in: 20
    ''')
  assert pgm.queue == [15, 20]

def test_when9(main, request):
  pgm = main(text = '''
main:
- stage1: 
  - in: 'strukov'      
  # 'strukov' in 'sergey'
  - when:
      instr: sergey
  - in: 15
  stage2:         
  - in: 20
    ''')
  assert pgm.queue == [20]

def test_when9(main, request):
  pgm = main(text = '''
main:
- stage1: 
  - in: 'strukov'      
  # 'strukov' in 'sergey'
  - when:
      notinstr: sergey
  - in: 15
  stage2:         
  - in: 20
    ''')
  assert pgm.queue == [15, 20]
