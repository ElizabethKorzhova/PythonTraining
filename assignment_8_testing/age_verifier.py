"""Module provides AgeVerifier class"""


class AgeVerifier:
    """Class represents AgeVerifier"""

    @staticmethod
    def is_adult(age: int) -> bool:
        """
        Checks whether the person has reached the age of 18.
        :param age: age of person
        :return: True if age is greater than or equal to 18. Otherwise False
        """
        if not isinstance(age, int):
            raise TypeError("Age must be an integer")
        if age < 0 or age > 120:
            raise ValueError("Age cannot be less than or equal to 0 and greater than 120")
        return age >= 18
