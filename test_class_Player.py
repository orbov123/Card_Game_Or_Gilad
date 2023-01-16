from unittest import TestCase,mock
from unittest.mock import patch

import class_Player
from class_Player import Player
from class_Deck_Of_Cards import Deck_Of_Cards
from class_Card import Card
class TestPlayer(TestCase):
    def setUp(self):
        self.deck1 = Deck_Of_Cards()
        self.omer = Player("omer",26)
        self.omer.player_deck = []

    def test__init__valid(self):
        """test the valid __init__"""
        self.assertEqual("omer",self.omer.player_name)
        self.assertEqual(self.omer.num_cards_player,26)

    def test__init__invalid_type(self):
        """test the invalid __init__"""
        with self.assertRaises(TypeError):
            omer = Player(15,15)
            omer = Player("omer","26")

    def test__init__invalid_value(self):
        """test __init__value>26, value<1"""
        self.gilad = Player("gilad",50)
        self.assertEqual(self.gilad.num_cards_player, 26)
        self.gilad = Player("gilad",-10)
        self.assertEqual(self.gilad.num_cards_player,26)


    def test__init__invalid__player_nam_length(self):
        """test init, if name is bigger then 10 letters, it takes the first 10"""
        self.gilad = Player("orororororororor,26")
        self.assertEqual(self.gilad.player_name,"ororororor")


    def test_set_hand_valid(self):
        """valid test set hand"""
        self.omer_deck = Deck_Of_Cards()
        self.omer.set_hand(self.omer_deck)
        self.assertEqual(len(self.omer.player_deck),26)

    def test_set_hand_invalid_type(self):
        """testing if the type of deck is not Deck_Of_Cards"""
        with self.assertRaises(TypeError):
            self.omer.set_hand(13)
            self.omer.set_hand('deck')

    def test_get_Card_valid(self):
        """test get card is valid, return the last card in the deck"""
        self.omer.player_deck = [Card('Heart',5),Card('Diamond',7),Card('Club',8),Card('Club',10)]
        last_card = self.omer.player_deck[-1]
        self.assertEqual(last_card,self.omer.get_card())

    def test_get_Card_invalid(self):
        """test get_card invalid,check  not equal to not last card to get_card """
        self.omer.player_deck = [Card('Heart', 5), Card('Diamond', 7), Card('Club', 8), Card('Club', 10)]
        not_last_card = self.omer.player_deck[2]
        self.assertNotEqual(not_last_card, self.omer.get_card())

    def test_add_card_valid(self):
        """test add card, check if card is equal to the first card of the deck"""
        card1 = Card('Diamond',7)
        self.omer.add_card(card1)
        self.assertEqual(card1,self.omer.player_deck[0])

    def test_add_card_invalid(self):
        """test """
        card1 = Card('Heart',8)
        self.omer.add_card(card1)
        self.assertNotEqual(card1,self.omer.player_deck[1])
        self.assertNotEqual(card1,self.omer.player_deck[-1])

    def test_add_card_invalid_type(self):
        """test add_card,if the function recieve not type Card"""
        with self.assertRaises(TypeError):
            self.omer.add_card(27)
            self.omer.add_card('diamond7')


