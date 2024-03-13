def test_main(main):
    pgm = main(
        text="""
main:
- stage1:
    - in: 10
    - sleep: 1
  stage2:
    - in: 20
    - sleep: 2
  stage5:
    - in: 30
    - sleep: 3
  stage4:
    - in: 40
    - sleep: 4
"""
    )
    assert pgm.queue == [10, 20, 30, 40]
    assert int(pgm.get_seconds()) == 4


def test_list(main):
    pgm = main(
        text="""
main:
- stage1:
    - in: 10
    - sleep: 0.2
- stage2:
    - in: 20
    - sleep: 0.4
- stage5:
    - in: 30
    - sleep: 0.6
- stage4:
    - in: 40
    - sleep: 0.8
"""
    )
    assert pgm.queue == [40]
    assert int(pgm.get_seconds()) == (0.2 + 0.4 + 0.6 + 0.8)
