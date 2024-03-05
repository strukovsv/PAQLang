import pytest

def test_one(main, request):
  pgm = main(text = """
- in: 
  - /etc/hostname
  - /etc/group           
- freads
- print: filename             
- split:
    attr: text         
- print                  
""")
  
