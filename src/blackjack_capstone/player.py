"""Code for player instances"""

from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from deck import Card

class PlayerType(str, Enum):
    COMPUTER = 'computer'
    HUMAN = 'human'


class Player:
    def __init__(self, name: str, player_type: PlayerType):
        self.score: int = 0
        self.name = name
        self.hand: list[Card] = []
        self.type = player_type

    def update_score(self):
        self.score += 1

    def add_card(self, card: Card):
        """Adds card object to players hand"""

        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

    
    
