from class_Deck_Of_Cards import Deck_Of_Cards
from class_Player import Player
class Card_Game:
    def __init__(self,player_name1:str,player_name2:str,num_cards:int=26):
        if num_cards>26 or num_cards<10:
            num_cards=26
        self.player1 = Player(player_name1,num_cards)
        self.player2 = Player(player_name2,num_cards)
        self.deck = Deck_Of_Cards()
        self.new_game()

    def __str__(self):
        return f'{self.player1}, {self.player2}'

    def new_game(self):
        self.deck.cards_shuffle()
        self.player1.set_hand(self.deck)
        self.player2.set_hand(self.deck)

    def get_winner(self):
        if len(self.player1.player_deck)>len(self.player2.player_deck):
            print(f"{self.player1.player_name} is the winner! has {len(self.player1.player_deck)} cards")

        elif len(self.player1.player_deck) == len(self.player2.player_deck):
            print("it's a tie!")
            return None

        else:
            print(f"{self.player2.player_name} is the winner! ,has {len(self.player2.player_deck)} cards")