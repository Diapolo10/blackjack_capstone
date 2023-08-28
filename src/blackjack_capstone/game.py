from __future__ import annotations

from config import LOGO
from deck import Deck
from player import Player, PlayerType
from processor import Processor
from screen import Screen


class Game:   

    def __init__(self):
        self.deck = Deck()
        self.screen = Screen()
        self.pc = Processor() 

    def ask_new_game(self) -> bool:
        """Greets user and returns user choice to start game or not"""

        start_game = self.screen.get_input("Do you want to play blackjack? Print y to start, anything else to stop: ")[:1]
        self.screen.add_heavy_line()

        return start_game == 'y'

    def show_hands(self, human: Player, computer: Player, is_cpu_turn: bool):
        self.screen.show_message(f"Your hand is [{self.screen.printable_hands(human, is_cpu_turn)}]")
        self.screen.show_message(f"Your score is {self.pc.calculate_score(human)} points.")
        self.screen.show_message(f"{computer.name}'s hand is [{self.screen.printable_hands(computer, is_cpu_turn)}]")
        self.screen.add_single_line()


    def ask_username(self) -> str:
        """Asks user name from user input"""

        return self.screen.get_input("What is your name?")

    def create_player(self, player_type: PlayerType, name: str = "Computer") -> Player:
        """Creates player of chosen type. Available types are human and computer, other arguments will return None"""

        return Player(name, player_type)

    def cpu_turn(self, human_player: Player, computer_player: Player, is_cpu_turn: bool = True) -> bool:
        """CPU moving (auto draw if less than 17). Stand if >= 17. Returns True if bust and False if not bust"""

        while self.pc.calculate_score(computer_player) < 17:
            self.screen.show_message("Computer takes a new card...")
            computer_player.add_card(self.deck.deal_card())
            self.show_hands(human_player, computer_player, is_cpu_turn)
            cpu_bust = self.pc.is_bust(computer_player)    
            if cpu_bust:
                return True

        self.screen.show_message("Computer stands.")
        self.screen.show_message(f"Computer hand is {self.pc.calculate_score(computer_player)}")
        return False


    def play_game(self):
        """Function to start game, contains game logic"""

        self.screen.show_message(LOGO)
        ## Create players
        user_name = self.ask_username().capitalize()

        try:
            human_player = self.create_player(PlayerType.HUMAN, user_name)
            computer_player = self.create_player(PlayerType.COMPUTER)
        except Exception as err:
            self.screen.show_message(err)
            self.screen.show_message("Game Aborted")
            return

        is_game_on = self.ask_new_game()

        ## Main game logic
        while is_game_on:
            # clear hands on each game
            human_player.clear_hand()
            computer_player.clear_hand()

            self.screen.show_message("The Blackjack Game begins!")
            if self.deck.is_half_empty():
                self.screen.show_message("Replenishing deck...")
                self.deck = Deck()

            #shuffle deck
            self.deck.shuffle()
            # deal cards

            human_player.add_card(self.deck.deal_card())
            human_player.add_card(self.deck.deal_card())

            computer_player.add_card(self.deck.deal_card())
            computer_player.add_card(self.deck.deal_card())

            # check if game is instantly won by any of parties
            if self.pc.hand_is_blackjack(human_player):
                self.show_hands(human_player, computer_player, False)
                self.screen.show_message("You have got BLACKJACK! YOU WIN BIG!!")
                human_player.update_score()
                is_game_on = self.ask_new_game()
                continue
            elif self.pc.hand_is_blackjack(computer_player):
                self.show_hands(human_player, computer_player, True)
                self.screen.show_message("Computer has BLACKJACK! YOU LOSE!")
                computer_player.update_score()
                is_game_on = self.ask_new_game()
                continue

            # show 1 card of cpu and both cards of Player
            self.screen.add_heavy_line()
            self.screen.show_message(f"Your current score is {human_player.score}")
            self.screen.show_message(f"Computer score is {computer_player.score}")
            self.screen.add_heavy_line()
            self.show_hands(human_player, computer_player, False)


            # ask player to deal
            human_is_bust = False
            cpu_is_bust = False
            while self.screen.get_input("Would you like another card? y for yes, any button for no: ")[:1] == 'y':
                human_player.add_card(self.deck.deal_card())
                self.show_hands(human_player, computer_player, False)
                if self.pc.is_bust(human_player):
                    self.screen.show_message(f"You bust! Your score is {self.pc.calculate_score(human_player)}")
                    computer_player.update_score()
                    human_is_bust = True
                    break

            if not human_is_bust:
                self.show_hands(human_player, computer_player, False)

                # create logic for cpu to auto play
                cpu_is_bust = self.cpu_turn(human_player, computer_player, True)

                if not cpu_is_bust:
                    # compare results
                    winner = self.pc.get_winner(human_player, computer_player)

                    if winner is None:
                        self.screen.show_message("It's a tie!")
                    else:
                        self.show_hands(human_player, computer_player, True)
                        self.screen.show_message(f"Computer hand is {self.pc.calculate_score(computer_player)}")
                        self.screen.show_message(f"{winner.name} wins!")
                        winner.update_score()
                else:
                    self.screen.show_message(f"Computer bust! His score is {self.pc.calculate_score(computer_player)}. You win!")
                    human_player.update_score()

            # ask if user wants to play again
            is_game_on = self.ask_new_game()

        self.screen.show_message("Thanks for playing! Goodbye!")
