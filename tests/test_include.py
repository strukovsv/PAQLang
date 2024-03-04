import pytest
import logging

def test_one(main, request):
  pgm = main(text = '''
- in:
  - /tests/data/lib1.yaml
  - /tests/data/lib2.yml
  - /tests/data/lib3.json
- include             
''')
  logging.info(f'{pgm.macros}')

def test_two(main, request):
  pgm = main(text = '''
- in:
  - /tests/data/lib1.yaml
  - /tests/data/lib2.yml
  - /tests/data/lib3.json
# Параллельно загрузить библиотеки             
- include    
- call: sub1
- call: sub2
- call: sub3
- call: sub4
''')
  logging.info(f'{pgm.macros}')  