"""This module is designed for developing flexible mechanism for processing various
game events, providing detailed information about the events that occurred."""

from dataclasses import dataclass

LEVELS = {
    1: 100,
    2: 200,
    3: 400,
    4: 800,
    5: 1600,
}


class GameEventException(Exception):
    """Exception raised when game event occurs."""

    def __init__(self, event_type: str, details: dict) -> None:
        """Initializes GameEventException class with event_type and details to
        insert into the exception."""
        self.event_type, self.details = event_type, details
        formatted_details = "\n\t".join(
            f"{key}: {value}" for key, value in details.items()
        )

        super().__init__(f"{event_type}\n\t{formatted_details}")


@dataclass
class DeathInfo:
    """Data class that contains information about death of character."""
    cause_death: str = ""
    death_place: str = ""


class GameCharacter:
    """Class that represents character."""

    def __init__(
            self,
            level: int,
            experience_points: int,
            health_points: int,
            death_info: DeathInfo = DeathInfo(),
    ) -> None:
        """Initializes GameCharacter class with level, experience_points (xp),
        health_points (hp) and optional death info."""
        self.level = level
        self.experience_points = experience_points
        self.health_points = health_points
        self.death_info = death_info
        self.process_action()

    def process_action(self) -> None:
        """Processes actions of character."""
        if self.health_points <= 0:
            raise GameEventException(
                "death",
                {"cause of death": self.death_info.cause_death,
                 "death place": self.death_info.death_place}
            )
        self.check_level(LEVELS)

    def check_level(self, levels: dict[int, int]) -> None:
        """Checks level for character."""
        required_xp: int | None = levels.get(self.level)
        if required_xp and self.experience_points > required_xp:
            self.level_up()
        elif required_xp and self.experience_points < required_xp * 0.5:
            self.level_down()

    def level_up(self):
        """Decreases level of character."""
        self.level += 1
        raise GameEventException(
            "levelUp",
            {"experience points": self.experience_points, "new level": self.level}
        )

    def level_down(self):
        """Decreases level of character."""
        if self.level <= 1:
            raise ValueError("Level cannot be less than 1")
        self.level -= 1
        raise GameEventException(
            "levelDown",
            {"experience points": self.experience_points, "new level": self.level}
        )


def test_game_event(
        level: int,
        experience_points: int,
        health_points: int,
        death_info: DeathInfo = DeathInfo(),
) -> None:
    """Tests game events."""
    try:
        GameCharacter(level, experience_points, health_points, death_info)
    except (GameEventException, ValueError) as ex:
        print(ex)


if __name__ == "__main__":
    test_game_event(2, 50, 50)
    test_game_event(1, 200, 50)
    test_game_event(1, 50, 0, DeathInfo("headshot", "short"))
