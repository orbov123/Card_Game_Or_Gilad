import class_Deck_Of_Cards
# class Player recievs name and number of cards(deafult 26), set the deck for the player.
class Player:
    def __init__(self,player_name:str, num_cards_player:int=26):
        if num_cards_player>26 or num_cards_player<10:
            num_cards_player=26
        self.player_name = player_name
        self.num_cards_player = num_cards_player
        self.player_deck = []

    def __str__(self):
        return f"the player name is {self.player_name}, his deck is {self.player_deck}"

    def set_hand(self,Deck_of_cards:class_Deck_Of_Cards):
        """ set deck of cards for the player """
        for i in range(self.num_cards_player):
            self.player_deck.append(Deck_of_cards.deal_one())
        # return self.card_list

    def __str__(self):
        return f'{self.player_deck}'

    def get_card(self):
        """return the last card of the player deck, and remove it"""
        return self.player_deck.pop()

    def add_card(self,card):
        """ recives a card, and add it to the player deck"""
        return self.player_deck.insert(0,card)

