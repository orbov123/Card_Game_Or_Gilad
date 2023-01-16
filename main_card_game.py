import class_Card
import class_Deck_Of_Cards
import class_Player
import class_Card_Game

player_name_1 = input("Enter your name: ")
player_name_2 = input("Enter your opponent name: ")
War_Game = class_Card_Game.Card_Game(player_name_1,player_name_2)
#introducing of the players:
print(f'player1: {War_Game.player1}\nplayer2: {War_Game.player2}')
#Beginning of the game:
for game in range(10):
    card_player1 = War_Game.player1.get_card()
    card_player2 = War_Game.player2.get_card()
    if card_player1>card_player2:
        winner = player_name_1
        War_Game.player1.add_card(card_player1)
        War_Game.player1.add_card(card_player2)
    else:
        winner = player_name_2
        War_Game.player2.add_card(card_player2)
        War_Game.player2.add_card(card_player1)
    print(f'round {game+1}:\n{player_name_1}: {card_player1}\n{player_name_2}: {card_player2}')
    print(f'Winner is: {winner}\n')
print('')
print(f'the winner is: {War_Game.get_winner()}')


