def test_exit1(main, request):
    pgm = main(
        text="""
main:
- stage1:
  - exit
  - in: 10
- stage2:
  - in: 20
    """
    )  # , name = request.node.name)
    assert pgm.queue == []


def test_exit2(main, request):
    pgm = main(
        text="""
main:
  stage0:
  - in: 5
  stage1:
  - exit
  - in: 10
  stage2:
  - in: 20
    """
    )  # , name = request.node.name)
    # pgm.save_stack(request)
    assert pgm.queue == [5, 20]
