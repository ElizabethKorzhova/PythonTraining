"""Module is designed to test AgeVerifier."""
import pytest
from assignment_8_testing.age_verifier import AgeVerifier

age = 200


@pytest.fixture
def age_verifier() -> AgeVerifier:
    """
    Fixture to initialize AgeVerifier for future tests.
    :return: instance of AgeVerifier
    """
    return AgeVerifier()


@pytest.mark.parametrize(("age_sample", "expected_result"),
                         ((18, True), (19, True), (1, False), (50, True), (15, False)))
def test_is_adult_success(age_verifier: AgeVerifier, age_sample: int, expected_result: bool) -> None:
    """
    Tests is_adult method of AgeVerifier for compliance of the expected result
    with the actual result
    :param age_verifier: instance of AgeVerifier class
    :param age_sample: age sample
    :param expected_result: expected answer (True or False)
    """
    assert age_verifier.is_adult(age_sample) == expected_result


@pytest.mark.parametrize(("incorrect_age", "expected_error"),
                         ((-1, ValueError), (1.3, TypeError),
                          ("", TypeError), (121, ValueError)))
def test_is_adult_wrong_data(age_verifier: AgeVerifier, incorrect_age: int,
                             expected_error: ValueError | TypeError) -> None:
    """
    Tests is_adult method of AgeVerifier for raises exception with incorrect age sample.
    :param age_verifier: instance of AgeVerifier class
    :param incorrect_age: incorrect age sample
    :param expected_error: expected type exception (ValueError or TypeError)
    :return:
    """
    with pytest.raises(expected_error):
        age_verifier.is_adult(incorrect_age)


@pytest.mark.skipif(age > 120, reason="Incorrect age value")
def test_is_adult_skip(age_verifier: AgeVerifier) -> None:
    """
    Tet is skipped if age value is more than 120
    """
    assert AgeVerifier.is_adult(121) == False
