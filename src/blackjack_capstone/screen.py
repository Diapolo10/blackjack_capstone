from __future__ import annotations

from player import Player, PlayerType


class Screen:
    @staticmethod
    def show_message(message: str):
        """Prints message on console"""

        print(message)

    @staticmethod
    def get_input(message: str) -> str:
        return input(f"{message} ").strip().lower()

    @staticmethod
    def printable_hands(player: Player, is_cpu_turn: bool) -> str:
        """Retruns hand as a printable string"""

        if player.type == PlayerType.COMPUTER and not is_cpu_turn:
            return str(player.hand[0])

        return ', '.join(
            str(card) for card in player.hand
        )

    @classmethod
    def add_heavy_line(cls, length: int = 21):
        cls.show_message('=' * length)

    @classmethod
    def add_single_line(cls, length: int = 4):
        cls.show_message('-' * length)
