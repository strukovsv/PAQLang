import pytest

def test_now(main):
  assert main(text = """
- now
""")