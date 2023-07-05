def add(alpha: int, beta: int) -> int:
    return alpha + beta


def subtract(alpha: int, beta: int) -> int:
    return alpha - beta


def multiply(alpha: int, beta: int) -> int:
    return alpha * beta


def divide(alpha: int, beta: int) -> tuple:
    return alpha // beta, alpha % beta


def test_add() -> None:
    alpha, beta = 1, 2
    result = add(alpha=alpha, beta=beta)
    assert alpha + beta == result, 'Error: function "add"'


def test_subtract() -> None:
    alpha, beta = 1, 2
    result = subtract(alpha=alpha, beta=beta)
    assert alpha - beta == result, 'Error: function "subtract"'


def test_multiply() -> None:
    alpha, beta = 1, 2
    result = multiply(alpha=alpha, beta=beta)
    assert alpha * beta == result, 'Error: function "multiply"'


def test_divide() -> None:
    alpha, beta = 1, 2
    result = divide(alpha=alpha, beta=beta)
    assert (alpha // beta, alpha % beta) == result, 'Error: function "divide"'
