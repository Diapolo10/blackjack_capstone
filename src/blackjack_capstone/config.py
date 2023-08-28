"""Global configuration options"""

from __future__ import annotations

from typing import Literal, get_args

CardValueType = Literal["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
CardSuitType = Literal['♠', '♦', '♥', '♣']

BLACKJACK: int = 21
CARD_VALUES = get_args(CardValueType)
CARD_SUITS = get_args(CardSuitType)
CARD_COUNT: int = len(CARD_VALUES) * len(CARD_SUITS)
SCORE_VALUES: dict[CardValueType, int] = {
    card_value: score_value
    for card_value, score_value in zip(
        CARD_VALUES,
        (2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11),
        strict=True
    )
}

LOGO: str = """
 ######  #          #     #####  #    #          #    #     #####  #    # 
 #     # #         # #   #     # #   #           #   # #   #     # #   #  
 #     # #        #   #  #       #  #            #  #   #  #       #  #   
 ######  #       #     # #       ###             # #     # #       ###    
 #     # #       ####### #       #  #      #     # ####### #       #  #   
 #     # #       #     # #     # #   #     #     # #     # #     # #   #  
 ######  ####### #     #  #####  #    #     #####  #     #  #####  #    # 

"""