import pytest

def test_if1(main, request):
  pgm = main(text = '''
main:
- stage1:         
  if1:
    if0:     
      - stage0:   
        # Условие ложно, содержимое stage0 не будет выполнено    
        - when:
            in: 0
        - in: 'if00'     
      # Это будет выполнено, так как условие только внутри stage0        
      - in: 'if0'     
    if1:     
      # Условие истино, поэтому будет выполнен код после условия       
      - when: 
          in: 1
      - stage2:   
        - in: 'if1'     
  if2:
    # Условие истино, поэтому будет выполнен код после условия       
    - when:
        in: 1 
    - in: 'if2'     
    ''')#, name = request.node.name)
  assert pgm.queue == ["if0", "if1", "if2"]

def test_if2(main, request):
  pgm = main(text = '''
main:
- stage1:         
  if1:
    if0:     
      - in:
      # Пустая входная очередь, не выполняется        
      - when
      - stage0:   
        - in: 0
        - when
      - in: 'if0'     
    if1:     
      - in: 1   
      # НЕ пустая входная очередь, не выполняется        
      - when
      - stage2:   
        - in: 'if1'     
    if3:     
      - in: 1
      # НЕ пустая входная очередь, не выполняется        
      - when
      - stage0:   
        - in: 0
        - when
      - in: 'if3'     
  if2:
    - in: 1     
      # НЕ пустая входная очередь, не выполняется        
    - when
    - in: 'if2'     
    ''')#, name = request.node.name)
  assert pgm.queue == ["if1", "if3", "if2"]

def test_if3(main, request):
    pgm = main(text = '''
main:
- stage1: 
    stg1:               
    - in: 0
    # stg3 состоит параллельно из st1 и st2, но так как они не выполнились, то []           
    # Поэтому в stg1 будет записан пустой массив           
    - stg3:
       st1:   
         - in 
         - when
         - in: 10      
       st2:  
         - in
         - when
         - in: 20            
    stg2:       
    - in: 1
    ''')
    assert pgm.queue == [1]

def test_if4(main, request):
    pgm = main(text = '''
main:
- stage1: 
    stg1:               
    - in: 0
    # stg3 состоит параллельно из st1 и st2, st1 не выполниться, а st2 выполнен, поэтому получим массив из st2 == [20]
    # Поэтому в stg1 будет записан [20]
    - stg3:
       st1:   
         - in
         - when
         - in: 15      
       st2:  
         - in: 20            
         - when:
    stg2:       
    - in: 1
    ''')
    assert pgm.queue == [20, 1]
