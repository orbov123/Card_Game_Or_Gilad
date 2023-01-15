from unittest import TestCase,mock
from unittest.mock import patch
from class_Player import Player
from class_Card import Card
from class_Deck_Of_Cards import Deck_Of_Cards

class TestPlayer(TestCase):
    def setUp(self):
        self.omer = Player("omer",26)

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
        """test __init__value_1-26"""
        self.gilad = Player("gilad",50)
        self.assertEqual(self.gilad.num_cards_player, 26)
        self.gilad = Player("gilad",-10)
        self.assertEqual(self.gilad.num_cards_player,26)


    def test__init__invalid__player_nam_length(self):
        self.gilad = Player("orororororororor,26")
        self.assertEqual(self.gilad.player_name,"ororororor")

    def test_set_hand_invalid_type(self):
        """testing if the type of deck is not Deck_Of_Cards"""
        with self.assertRaises(TypeError):
            self.omer.set_hand(13)
            self.omer.set_hand('deck')

    #@mock.patch('class_Player.Player.set_hand',return_value = ['Club1', 'Spade11', 'Diamond13', 'Spade9', 'Heart13', 'Heart10', 'Club7', 'Diamond3', 'Spade10', 'Spade8', 'Diamond5', 'Diamond10', 'Heart1', 'Club4', 'Diamond12', 'Heart9', 'Heart8', 'Club5', 'Spade6', 'Heart11', 'Club9', 'Spade13', 'Diamond2', 'Heart4', 'Diamond9', 'Spade5'])
    #def test_get_card(self,mock_set_hand):
        #self.omer.player_deck = mock_set_hand
        #self.assertEqual('Spade5',self.omer.get_card())

    def test_add_card_valid(self):
        self.card = Card('Diamond',7)
        self.omer.add_card(self.card)
        self.assertIn(self.card,self.omer.player_deck)

    def test_add_card_invalid(self):
        with self.assertRaises(TypeError):
            self.omer.add_card(27)
            self.omer.add_card('diamond7')


