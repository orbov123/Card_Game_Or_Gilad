from unittest import TestCase,mock
from unittest.mock import patch
from class_Deck_Of_Cards import Deck_Of_Cards


class TestDeck_Of_Cards(TestCase):
    def setUp(self):
        self.deck1 = Deck_Of_Cards()
        print('-----setUp------')

    def test_cards_shuffle(self):
        self.deck2 = Deck_Of_Cards()
        self.deck1.cards_shuffle()
        self.assertNotEqual(self.deck1.deck,self.deck2.deck)


    #def test_deal_one(self):


