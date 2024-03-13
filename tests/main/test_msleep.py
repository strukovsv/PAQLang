def test_msleep_default(main, request):
    pgm = main(
        text="""
- in:
  - 1
  - 2
  - 3
- msleep
""",
        request=request,
    )
    assert pgm.queue == []
    assert 2.9 < pgm.get_seconds() and pgm.get_seconds() < 3.2


def test_msleep_arr(main, arr_ints):
    pgm = main(
        datas=arr_ints,
        text="""
- in: ~ints
- msleep
""",
    )
    assert pgm.queue == []
    assert 2.9 < pgm.get_seconds() and pgm.get_seconds() < 3.2
