import pytest

def test_dec(main, request):
    main(text = '''
main:
- start:
    - in: 5         
    - out: cnt     
- stage1:         
  while1:
    - sleep: 0.2     
    - dec: cnt
    - print: dec
    - break:
        eq: 0   
     ''')

def test_inc(main):
    main(text = '''
main:
- start:
    - in: 0         
    - out: cnt     
- stage1:         
  while1:
    - sleep: 0.2     
    - inc: cnt
    - print: inc
    - break:
        eq: 5   
     ''')

def test_while_parallel(main, request):
    pgm = main(text = '''
main:
- start:
    - in: 0         
    - out: cnt1     
    - in: 0         
    - out: cnt2     
- stage1:         
    while1:
    - break:
        ge: 5
        in: ~cnt1
    - sleep: 0.3 
    - inc: cnt1
    - in: ~cnt1 
    - print: cycle1
    while2:
    - break:
        ge: 10
        in: ~cnt2
    - sleep: 0.2 
    - inc: cnt2
    - in: ~cnt2 
    - print: cycle2
- in: 
  - ~cnt1               
  - ~cnt2               
     ''')
