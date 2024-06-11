# 테스트 대상 함수
def add(a: int, b: int) -> int:
    return a + b

def substract(a: int, b: int) -> int:
    return b - a

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a:int, b:int) -> int:
    return b // a


# 테스트 대상 함수를 테스트할 테스트 함수
def test_add() -> None:
    assert add(1, 1) == 2

def test_subtract() -> None:
    assert substract(2, 5) == 3

def test_multiply() -> None:
    assert multiply(10, 10) == 100

def test_divide() -> None:
    return divide(25, 100) == 4



