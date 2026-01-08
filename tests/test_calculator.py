from operations.calculator import add, sub, mul, div
def test_add():
    assert add(2,3)==5
def test_sub():
    assert sub(10,7)==3
def test_mul():
    assert mul(3,4)==12
def test_div():
    assert div(20,10)==2

