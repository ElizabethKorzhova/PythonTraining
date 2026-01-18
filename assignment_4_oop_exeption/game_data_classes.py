"""This module is designed for representing game data classes."""

from dataclasses import dataclass


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
