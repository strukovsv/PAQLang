def test_one(main, request):
    pgm = main(
        text="""
- in:
  - issue: TEST-101
    lines:
    - nline: 103
      text: "if test('TEST-101') then"
    - nline: 105
      text: "if test('TEST-101') then"
    - nline: 205
      text: "if test('TEST-101') then"
- plane
"""
    )
    assert pgm.queue == [
        {
            "issue": "TEST-101",
            "nline": 103,
            "text": "if test('TEST-101') then",
        },
        {
            "issue": "TEST-101",
            "nline": 105,
            "text": "if test('TEST-101') then",
        },
        {
            "issue": "TEST-101",
            "nline": 205,
            "text": "if test('TEST-101') then",
        },
    ]


def test_two(main, request):
    pgm = main(
        text="""
- in:
  - issue: TEST-101
    lines:
    - nline: 103
      text: "if test('TEST-101') then"
    - nline: 105
      text: "if test('TEST-101') then"
    - nline: 205
      text: "if test('TEST-101') then"
- plane
- attr:
  - issue
  - nline
"""
    )
    assert pgm.queue == [
        {"issue": "TEST-101", "nline": 103},
        {"issue": "TEST-101", "nline": 105},
        {"issue": "TEST-101", "nline": 205},
    ]
