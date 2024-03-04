import pytest

def test_one(main, request):
  pgm = main(text = """
- walk: 
    path: "/etc" 
    regex: "^/etc/host.*$"
- freads
- attr: text
- split
- split: "\t"
- distinct                                             
- print                  
""")
  # assert pgm.queue == ['1', '2', '3', '4', '5']

