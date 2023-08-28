from __future__ import annotations

from typing import TYPE_CHECKING

from config import BLACKJACK, SCORE_VALUES

if TYPE_CHECKING:
    from player import Player

class Processor:

    @staticmethod
    def calculate_score(player: Player) -> int:
        has_ace = False
        total = 0

        for card in player.hand:
            if card.value == "A":
                has_ace = True
            total += SCORE_VALUES[card.value]

        if total > BLACKJACK and has_ace:
            total -= 10

        return total
    
    @classmethod
    def get_winner(cls, human: Player, computer: Player) -> Player | None:
        """Returns object of winner, None if tie"""

        human_score = cls.calculate_score(human)
        computer_score = cls.calculate_score(computer)

        if human_score == computer_score:
            return None

        if human_score > computer_score:
            return human

        return computer

    @classmethod
    def is_bust(cls, player: Player) -> bool:
        """Checks if player has more than 21"""

        return cls.calculate_score(player) > BLACKJACK
    
    def hand_is_blackjack(cls, player: Player) -> bool:
        """Checks if dealt hand is blackjack and returns true or false"""

        return cls.calculate_score(player) == BLACKJACK
