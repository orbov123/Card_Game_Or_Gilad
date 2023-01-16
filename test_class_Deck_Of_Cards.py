from unittest import TestCase,mock
from unittest.mock import patch
from class_Deck_Of_Cards import Deck_Of_Cards
from class_Card import Card

class TestDeck_Of_Cards(TestCase):
    def setUp(self):
        self.deck1 = Deck_Of_Cards()
        print('-----setUp------')

    def test_init_deck(self):
        self.card1 = Card('Diamond',7)
        self.assertIn(self.card1,self.deck1.deck)
        self.assertEqual(len(self.deck1.deck),52)

    def test_init_invalid_deck(self):
        self.invalidcard = Card('GILAD',10)
        self.assertNotIn(self.invalidcard,self.deck1.deck)
        self.assertNotEqual(len(self.deck1.deck),53)

    def test_cards_shuffle(self):
        self.deck2 = Deck_Of_Cards()
        self.deck1.cards_shuffle()
        self.assertNotEqual(self.deck1.deck,self.deck2.deck)


    def test_deal_one_valid(self):
        self.deck2 = Deck_Of_Cards()
        self.assertEqual(self.deck2.deck[51],self.deck2.deal_one())

    def test_deal_one_invalid(self):
        self.deck2 = Deck_Of_Cards()
        self.assertNotEqual(self.deck2.deck[50],self.deck2.deal_one())


