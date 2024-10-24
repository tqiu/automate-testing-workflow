from src import add, sub

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(-1, -2) == 1
    assert sub(4, 5) == -1
    print("Subtraction tests passed")
