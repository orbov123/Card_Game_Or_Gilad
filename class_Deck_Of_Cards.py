import class_Card
import random
# class Deck_of_cards set a full deck of 52 cards, with no duplicate.
# by the hierarchy of the values and the suits
class Deck_Of_Cards:
    def __init__(self):
        self.deck = []
        list_values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        dict_suit = {'Diamond':1,'Spade':2,'Heart':3,'Club':4 }
        for value in list_values:
            for key in dict_suit:
                self.deck.append(class_Card.Card(key,value))

    def cards_shuffle(self):
        """shuffle the deck of cards"""
        random.shuffle(self.deck)


    def deal_one(self):
        """return the last card of the deck, and remove it"""
        return self.deck.pop()

    def __str__(self):
        return f"{self.deck}"