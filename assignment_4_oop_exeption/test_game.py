"""This module is designed for testing game events and resource shortages."""

from game_data_classes import CharacterMetrics, DeathInfo, CharacterResources
from game_exceptions import GameEventException, InsufficientResourcesException
from game_character import GameCharacter


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
