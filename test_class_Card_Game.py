from unittest import TestCase,mock
from unittest.mock import patch

import class_Player
from class_Card_Game import Card_Game
from class_Player import Player
from class_Deck_Of_Cards import Deck_Of_Cards
from class_Card import Card
class TestCard_Game(TestCase):
    def setUp(self):
        self.game = Card_Game("alon","meira")
        self.deck1 = Deck_Of_Cards()

    def test__init__valid_name(self):
        """test init valid,players name"""
        self.assertEqual("alon",self.game.player1.player_name)
        self.assertEqual("meira",self.game.player2.player_name)

    def test__init__invalid_player_name(self):
        """test init invalid,player name must be type string"""
        with self.assertRaises(TypeError):
            game = Card_Game(32,"or")
            game = Card_Game("or",50)
            game = Card_Game(12,24)

    def test__init__invalid_type_num_cards(self):
        """test init invalid type num_cards,must be int"""
        with self.assertRaises(TypeError):
            game = Card_Game('kobi','gilad','or1')
            game = Card_Game('kobi','gilad','26')

    def test_init_invalid_num_cards(self):
        """"test init invalid num_cards_value,must be between 10 to 26"""
        milhama = Card_Game('OR','GILAD',27)
        self.assertEqual(milhama.player1.num_cards_player,26)
        milhama = Card_Game('or','gilad',9)
        self.assertEqual(milhama.player1.num_cards_player, 26)
        milhama = Card_Game('or', 'gilad', 50)
        self.assertEqual(milhama.player1.num_cards_player, 26)
    def test_new_game_valid(self):
        """test new_game each player get deck of 26 cards"""
        self.assertEqual(len(self.game.player1.player_deck),26)
        self.assertEqual(len(self.game.player2.player_deck),26)
    def test_new_game_invalid(self):
        """ test new_game value error when new game is when game began"""
        game1 = Card_Game('alon','tal',15)
        with self.assertRaises(ValueError):
            game1.new_game()
    def test_get_winner_valid_tie(self):
        """test get winner for a tie  each player have 26 cards"""
        self.assertEqual(None,self.game.get_winner())

    def test_get_winner_valid_player1(self):
        """test get_winner for player 1 is winner"""
        game1 = Card_Game('gilad','or',10)
        card1 = Card('Heart',7)
        game1.player1.add_card(card1)
        self.assertEqual('gilad',game1.get_winner())

    def test_get_winner_valid_else_player2(self):
        """test get_winner for player 2 is winner"""
        game1 = Card_Game('gilad','or',10)
        card1 = Card('Heart',7)
        game1.player2.add_card(card1)
        self.assertEqual('or',game1.get_winner())

