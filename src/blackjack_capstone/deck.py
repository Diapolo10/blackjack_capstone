"""Card and Deck implementations"""

from __future__ import annotations

import random
from enum import Enum

from config import (
    CardValueType,
    CardSuitType,
    CARD_COUNT,
    CARD_SUITS,
    CARD_VALUES,
)


class Card(str, Enum):
    value: CardValueType
    suit: CardSuitType

    def __str__(self) -> str:
        return f"{self.value} {self.suit}"


class Deck:
    """Class Deck provides deck functionality, such as create deck, shuffle etc."""

    def __init__(self, card_count: int = CARD_COUNT):
        self.card_count = card_count
        self.deck = self.populate_deck()

    def populate_deck(self) -> list[Card]:
        """Populate empty deck or repopulate used deck. Returns list of Card objects"""

        deck = [
            Card(value, suit)
            for value in CARD_VALUES
            for suit in CARD_SUITS
        ]

        return deck

    def shuffle(self):
        """Shuffles deck in-place without re-creating deck"""

        random.shuffle(self.deck)

    def deal_card(self) -> Card:
        """Deals the topmost card and removes it from deck"""

        return self.deck.pop()

    def is_half_empty(self) -> bool:
        """Returns True if there are less than half of remaining cards"""

        return len(self.deck) < self.card_count / 2

    def __str__(self) -> str:
        """Prints deck in format 4 Hearts, 5 Clubs etc."""

        return f"The deck is [{', '.join(str(card) for card in self.deck)}]"
