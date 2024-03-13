def test_continue(main, request):
    pgm = main(
        text="""
main:
- in: 0
- out: cnt_result
- while:
  - inc: cnt_result
  - print: continue
  - continue:
    - in: ~cnt_result
    - lt: 5
  - print: break
  - break:
    - in: ~cnt_result
    - eq: 10
    """
    )  # , name = request.node.name)
    assert pgm.get_data("cnt_result") == [10]


def test_continue1(main, request):
    pgm = main(
        text="""
main:
- in: 0
- out: cnt_result
- while:
    stage:
    - inc: cnt_result
    - print: continue
    - continue:
      - in: ~cnt_result
      - lt: 5
    - print: break
    - break:
      - in: ~cnt_result
      - eq: 10
    """
    )  # , name = request.node.name)
    assert pgm.get_data("cnt_result") == [10]


def test_continue2(main, request):
    pgm = main(
        text="""
main:
- in: 0
- out: cnt_result
- while:
    stage0:
    - inc: cnt_result
    - print: continue0
    - continue:
      - in: ~cnt_result
      - lt: 5
    - print: break0
    - break:
      - in: ~cnt_result
      - eq: 10
    stage1:
    - inc: cnt_result
    - print: continue1
    - continue:
      - in: ~cnt_result
      - lt: 5
    - print: break1
    - break:
      - in: ~cnt_result
      - eq: 10
    """
    )  # , name = request.node.name)
    assert pgm.get_data("cnt_result") == [10]
