import class_Card
import random
class Deck_Of_Cards:
    def __init__(self):
        self.deck = []
        list_values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        dict_suit = {'Diamond':1,'Spade':2,'Heart':3,'Club':4 }
        for value in list_values:
            for key in dict_suit:
                self.deck.append(class_Card.Card(key,value))

    def cards_shuffle(self):
        random.shuffle(self.deck)


    def deal_one(self):
        return self.deck.pop()

    def __str__(self):
        return f"{self.deck}"