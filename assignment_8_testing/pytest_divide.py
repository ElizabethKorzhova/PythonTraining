"""Module for testing divide function."""
import pytest
from assignment_8_testing.divide import divide


@pytest.mark.parametrize(("a", "b", "result"), (
        (1, 1, 1.0),
        (3, 2, 1.5),
        (0, 20, 0),
        (10, 3, 3.33333333333)))
def test_divide_success(a: int, b: int, result: float) -> None:
    """Test divide function for compliance of the expected result with the actual result."""
    assert divide(a, b) == pytest.approx(result)


@pytest.mark.parametrize(("a", "b"), ((1, 0), (3, 0), (-5, 0), (0, 0)))
def test_divide_by_zero_raises_error(a: int, b: int) -> None:
    """Tets divide by zero raises error."""
    with pytest.raises(ZeroDivisionError):
        assert divide(a, b)


@pytest.mark.parametrize(("a", "b"), ((1, "0"), ("", 4), (1.3, None)))
def test_divide_with_wrong_types(a: str | int | float, b: str | int | float) -> None:
    """Tets divide with wrong types raises error."""
    with pytest.raises(TypeError):
        assert divide(a, b)
