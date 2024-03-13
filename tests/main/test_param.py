from paqlang.param import Param


def test_empty_int():
    prm = Param(param=None)
    assert prm.int == 0
    prm = Param(param=0)
    assert prm.int == 0
    prm = Param(param=[0])
    assert prm.int == 0
    prm = Param(param=[1, 2])
    assert prm.int == 0


def test_int():
    prm = Param(param=10)
    assert prm.int == 10
    prm = Param(param=[10])
    assert prm.int == 10


def test_float():
    prm = Param(param=10.2)
    assert prm.float == 10.2
    prm = Param(param=[10.2])
    assert prm.float == 10.2


def test_empty_str():
    prm = Param(param=None)
    assert prm.string == ""
    prm = Param(param="")
    assert prm.string == ""
    prm = Param(param=[""])
    assert prm.string == ""


def test_str():
    prm = Param(param="test2")
    assert prm.string == "test2"
    prm = Param(param=["test2"])
    assert prm.string == "test2"
    prm = Param(param=["test1", "test2"])
    assert prm.string == "\n".join(["test1", "test2"])
