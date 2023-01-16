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


    @mock.patch('class_Player.Player.set_hand',return_value = ['Club1', 'Spade11', 'Diamond13', 'Spade9', 'Heart13', 'Heart10', 'Club7', 'Diamond3', 'Spade10', 'Spade8', 'Diamond5', 'Diamond10', 'Heart1', 'Club4', 'Diamond12', 'Heart9', 'Heart8', 'Club5', 'Spade6', 'Heart11', 'Club9', 'Spade13', 'Diamond2', 'Heart4', 'Diamond9', 'Spade5'])
    def test_get_card(self,mock_player_deck):
        self.omer.player_deck = mock_player_deck
        self.spade5 = Card('Spade',5)
        self.assertEqual(self.spade5,self.omer.get_card())

    #def test_get_card(self):
        #with patch('class_Player.Player.set_hand')as mock_player_deck:
            #mock_player_deck.return_value = ['Club1', 'Spade11', 'Diamond13', 'Spade9', 'Heart13', 'Heart10', 'Club7', 'Diamond3', 'Spade10', 'Spade8', 'Diamond5', 'Diamond10', 'Heart1', 'Club4', 'Diamond12', 'Heart9', 'Heart8', 'Club5', 'Spade6', 'Heart11', 'Club9', 'Spade13', 'Diamond2', 'Heart4', 'Diamond9', 'Spade5']
            #self.assertEqual(self.omer.get_card(),'Spade5')
    def test_add_card_valid(self):
        self.card = Card('Diamond',7)
        self.omer.add_card(self.card)
        self.assertEqual(self.card,self.omer.player_deck[0])

    def test_add_card_invalid(self):
        with self.assertRaises(TypeError):
            self.omer.add_card(27)
            self.omer.add_card('diamond7')


