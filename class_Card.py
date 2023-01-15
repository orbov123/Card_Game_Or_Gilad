# The Card class recives card suit and value representing their size.
class Card:
    def __init__(self,suit:str,value:int):
        if type(suit) != str:
            raise TypeError('Error,card suit must be type string')
        if type(value) != int:
            raise TypeError('Error,card value must be type int')
        if value > 13 or value < 1:
            raise ValueError('Error,card value must be between 1 to 13')
        self.dict_suit = {'Diamond': 1, 'Spade': 2, 'Heart': 3, 'Club': 4}
        self.card_suit = suit
        self.card_value = value

    def __gt__(self,other):
        """ check greater card """
        if type(other) != Card:
            raise TypeError('Error,other must be the same class of Card')
        if self.card_value > other.card_value:
            if other.card_value ==1:
                return False
            return True
        elif self.card_value ==1 and other.card_value>1:
            return True
        elif self.card_value== other.card_value:
            if self.dict_suit[self.card_suit]>other.dict_suit[other.card_suit]:
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        """check if cards are equal"""
        if type(other) != Card:
            raise TypeError('Error,other must be the same class Card')
        if self.card_value==other.card_value:
            if self.card_suit== other.card_suit:
                return True
        else:
            return False

    def __repr__(self):
        return f'{self.card_suit}{self.card_value}'

