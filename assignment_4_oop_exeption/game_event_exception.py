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


class InsufficientResourcesException(Exception):
    """Exception raised when resources are not sufficient."""

    def __init__(self, required_resource, required_amount, current_amount) -> None:
        """Initializes InsufficientResourcesException class with required_resource,
        required_amount and current_amount to insert into the exception."""
        self.required_resource = required_resource
        self.required_amount = required_amount
        self.current_amount = current_amount

        super().__init__(
            f"\nInsufficient resources: you need collect {required_amount - current_amount} "
            f"more {required_resource}"
        )


@dataclass
class DeathInfo:
    """Data class that contains information about death of character."""
    cause_death: str = ""
    death_place: str = ""


@dataclass
class CharacterMetrics:
    """Data class that contains information about character."""
    level: int = 1
    experience_points: int = 50
    health_points: int = 100


@dataclass
class CharacterResources:
    """Data class that contains information about character resources."""
    required_resource: str = "wood"
    required_amount: int = 200
    current_amount: int = 250


class GameCharacter:
    """Class that represents character."""

    def __init__(
            self,
            character_metrics: CharacterMetrics = CharacterMetrics(),
            character_resources: CharacterResources = CharacterResources(),
            death_info: DeathInfo = DeathInfo(),
    ) -> None:
        """Initializes GameCharacter class with optional attributes:
         - character_metrics (include level, experience_points (xp), health_points (hp));
         - character_resources (include required_resource, required_amount, current_amount);
         - optional death info (include cause_death, death_place)."""
        self.character_metrics = character_metrics
        self.character_resources = character_resources
        self.death_info = death_info
        self.process_action()

    def process_action(self) -> None:
        """Processes actions of character."""
        if self.character_metrics.health_points <= 0:
            raise GameEventException(
                "death",
                {"cause of death": self.death_info.cause_death,
                 "death place": self.death_info.death_place}
            )
        if self.character_resources.current_amount < self.character_resources.required_amount:
            raise InsufficientResourcesException(self.character_resources.required_resource,
                                                 self.character_resources.required_amount,
                                                 self.character_resources.current_amount)
        self.check_level(LEVELS)

    def check_level(self, levels: dict[int, int]) -> None:
        """Checks level for character."""
        required_xp: int | None = levels.get(self.character_metrics.level)
        if required_xp and self.character_metrics.experience_points > required_xp:
            self.level_up()
        elif required_xp and self.character_metrics.experience_points < required_xp * 0.5:
            self.level_down()

    def level_up(self):
        """Decreases level of character."""
        self.character_metrics.level += 1
        raise GameEventException(
            "levelUp",
            {"experience points": self.character_metrics.experience_points,
             "new level": self.character_metrics.level}
        )

    def level_down(self):
        """Decreases level of character."""
        if self.character_metrics.level <= 1:
            raise ValueError("Level cannot be less than 1")
        self.character_metrics.level -= 1
        raise GameEventException(
            "levelDown",
            {"experience points": self.character_metrics.experience_points,
             "new level": self.character_metrics.level}
        )


def test_game(
        character_metrics: CharacterMetrics = CharacterMetrics(),
        character_resources: CharacterResources = CharacterResources(),
        death_info: DeathInfo = DeathInfo(),

) -> None:
    """Tests game events and actions."""
    try:
        GameCharacter(character_metrics, character_resources, death_info)
    except (GameEventException, InsufficientResourcesException, ValueError) as ex:
        print(ex)


if __name__ == "__main__":
    test_game(CharacterMetrics(2, 50, 50))
    test_game(CharacterMetrics(1, 200, 50))
    test_game(CharacterMetrics(1, 50, 0), death_info=DeathInfo("headshot", "short"))
    test_game(character_resources=CharacterResources("gold", 200, 50))
