from unittest import TestCase
from class_Card import Card


class TestCard(TestCase):
    def setUp(self):
        self.card = Card('Heart',10)
        self.other_card = Card('Diamond',8)
        print('-----setUp-------')

    def test__init__valid(self):
        """testing if the suit and value valid """
        self.assertEqual(self.card.card_suit,'Heart')
        self.assertEqual(self.card.card_value,10)

    def test__init__invalid_type_suit(self):
        """testing if the type of suit is invalid"""
        with self.assertRaises(TypeError):
            self.card1 = Card(13, 10)



    def test__init__invalid_type_value(self):
        """test init card value invalid type, not int"""
        with self.assertRaises(TypeError):
            self.card1 = Card('Heart','10')

    def test__init__invalid_value_value(self):
        """test init invalid card value must be between 1 to 13"""
        with self.assertRaises(ValueError):
            self.card1 = Card('Heart',14)
            self.card1 = Card('Heart',0)
            self.card1 = Card('Heart',50)

    def test__gt__valid(self):
        """test gt valid(card to other card)"""
        self.assertTrue(self.card>self.other_card)
        self.assertFalse(self.other_card>self.card)

    def test__gt__invalid_type_other(self):
        """test __gt__ invalid card to not type card"""
        with self.assertRaises(TypeError):
            self.card>15
            self.card>'diamond'
            self.card>['diamond',8]
    def test__gt__valid_other_card_equal_1(self):
        """ test ___gt___ other = 1 (ace)"""
        self.card1 = Card('Diamond', 1)
        self.assertFalse(self.card>self.card1)

    def test__gt__valid_card_equal_1(self):
        """ test ___gt___ self.card = 1 (ace)"""
        card1 = Card('Diamond', 1)
        self.assertTrue(card1>self.card)

    def test__eq__valid(self):
        """test eq valid """
        self.card3 = Card('Heart',10)
        self.assertTrue(self.card==self.card3)

    def test__eq__valid_not_eq(self):
        """test eq valid not equal """
        self.assertFalse(self.card == self.other_card)

    def test__eq__invalid_type_other(self):
        """ test equal, other not type Card"""
        with self.assertRaises(TypeError):
            self.card == [1,2,3]
            self.card == {1:10,2:20,3:30}
            self.card == 'diamond 10'

