def test_sleep_default(main, request):
    pgm = main(
        text="""
sleep
""",
        request=request,
    )
    assert pgm.queue == []
    assert 0.99 < pgm.get_seconds() and pgm.get_seconds() < 1.1


def test_sleep(main, request):
    pgm = main(
        text="""
sleep: 2
""",
        request=request,
    )
    assert pgm.queue == []
    assert 1.99 < pgm.get_seconds() and pgm.get_seconds() < 2.1


def test_sleep_list(main, request):
    pgm = main(
        text="""
- sleep: 1
- sleep: 2
""",
        request=request,
    )
    assert pgm.queue == []
    assert 2.99 < pgm.get_seconds() and pgm.get_seconds() < 3.1


def test_sleep_parallel(main, request):
    pgm = main(
        text="""
sleep1:
  sleep: 1
sleep2:
  sleep: 2
""",
        request=request,
    )
    assert pgm.queue == []
    assert 1.99 < pgm.get_seconds() and pgm.get_seconds() < 2.1
