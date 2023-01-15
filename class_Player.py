from class_Deck_Of_Cards import Deck_Of_Cards
from class_Card import Card
# class Player recievs name and number of cards(deafult 26), set the deck for the player.
class Player:
    def __init__(self,player_name:str, num_cards_player:int=26):
        if num_cards_player>26 or num_cards_player<10:
            num_cards_player=26
        if type(player_name)!=str:
            raise TypeError("Player name can't be nothing but str")
        if type(num_cards_player)!=int:
            raise TypeError("number of cards must be int ")
        if len(player_name)>10:
            player_name=player_name[:10]
        self.player_name = player_name
        self.num_cards_player = num_cards_player
        self.player_deck = []

    def __str__(self):
        return f"the player name is {self.player_name}, his deck is {self.player_deck}"

    def set_hand(self,deck:Deck_Of_Cards):
        """ set deck of cards for the player """
        if type(deck) != Deck_Of_Cards:
            raise TypeError('error. argument must be class deck of cards')
        for i in range(self.num_cards_player):
            self.player_deck.append(deck.deal_one())



    def get_card(self):
        """return the last card of the player deck, and remove it"""
        return self.player_deck.pop()

    def add_card(self,card):
        """ recives a card, and add it to the player deck"""
        if type(card)!=Card:
            raise TypeError("the card must be a Card type")
        self.player_deck.insert(0,card)

