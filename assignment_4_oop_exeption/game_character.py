"""This module is designed for developing GameCharacter class for processing various
game events and collected resources, as well as to provide detailed information about
the game event that occurred and the lack of resources."""

from game_data_classes import CharacterMetrics, DeathInfo, CharacterResources
from game_exceptions import GameEventException, InsufficientResourcesException

LEVELS = {
    1: 100,
    2: 200,
    3: 400,
    4: 800,
    5: 1600,
}


class GameCharacter:
    """Class that represents character."""

    def __init__(
            self,
            character_metrics: CharacterMetrics = CharacterMetrics(),
            character_resources: CharacterResources = CharacterResources(),
            death_info: DeathInfo = DeathInfo(),
    ) -> None:
        """Initializes GameCharacter class with optional attributes:
         - character_metrics (includes level, experience_points (xp), health_points (hp));
         - character_resources (includes required_resource, required_amount, current_amount);
         - death info (includes cause_death, death_place)."""
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
