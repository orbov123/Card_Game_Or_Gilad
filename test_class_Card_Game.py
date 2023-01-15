from unittest import TestCase,mock
from unittest.mock import patch

import class_Player
from class_Card_Game import Card_Game
from class_Player import Player
class TestCard_Game(TestCase):
    def setUp(self):
        self.game = Card_Game("alon","meira")

    def test__init__valid_name(self):
        self.assertEqual("alon",self.game.player1.player_name)
        self.assertEqual("meira",self.game.player2.player_name)

    def test__init__invalid_player_name(self):
        with self.assertRaises(TypeError):
            game = Card_Game(32,"or")
            game = Card_Game("or",50)
            game = Card_Game(12,24)

    def test__init__invalid_type_num_cards(self):
        with self.assertRaises(TypeError):
            game = Card_Game('kobi','gilad','or1')

    def test_init_invalid_num_cards(self):
        self.milhama = Card_Game('OR','GILAD',50)
        self.assertEqual(self.milhama.player1.num_cards_player,26)

    def test_get_winner_valid_tie(self):
        """test get winner for a tie """
        self.game = Card_Game('gilad','tamir')
        self.assertEqual(None,self.game.get_winner())

    #def test_get_winner_valid(self):