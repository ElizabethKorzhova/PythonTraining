"""This module is designed to simulate a workout timer with function
that allows to change the workout time at each step."""

default_time = 60


def training_session(training_rounds: int) -> None:
    """Function to simulate the workout timer given number of training rounds."""
    time_per_round = default_time

    def adjust_time() -> None:
        """Function to change the workout time at each round by 5 minutes."""
        nonlocal time_per_round
        time_per_round -= 5

    for training_round in range(1, training_rounds + 1):
        if time_per_round == 1:
            print(f"Round {training_round}: {time_per_round} minutes")
        else:
            adjust_time()
            print(f"Round {training_round}: {time_per_round} minutes (after time adjustment)")


training_session(5)
