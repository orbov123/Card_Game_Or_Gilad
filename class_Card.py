# The Card class recives card suit and value representing their size.

class Card:
    def __init__(self,suit:str,value:int):
        self.card_suit = suit
        self.card_value = value

    def __gt__(self,other):
        """ check greater card """
        if self.card_value > other.card_value:
            if other.card_value ==1:
                return False
            return True
        elif self.card_value ==1 and other.card_value>1:
            return True
        elif self.card_value== other.card_value:
            if self.card_suit>other.card_suit:
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        """check if cards are equal"""
        if self.card_value==other.card_value:
            if self.card_suit== other.card_suit:
                return True
        else:
            return False

    def __repr__(self):
        return f'{self.card_suit}{self.card_value}'

