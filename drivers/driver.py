import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from SNAKE_AND_LADDER.models.snake import Snake
from SNAKE_AND_LADDER.models.ladder import Ladder
from SNAKE_AND_LADDER.models.player import Player
from SNAKE_AND_LADDER.services.boardservice import BoardService

if __name__ == '__main__':

    print("How many snakes board will have?")
    total_snakes = int(input())
    list_of_snakes = []
    for sn in range(total_snakes):
        head_tail = list(map(int,input().split()))
        list_of_snakes.append(Snake(head_tail[0],head_tail[1]))
    
    print("How many ladders board will have?")
    total_ladders = int(input())
    list_of_ladders = []
    for ld in range(total_ladders):
        start_end = list(map(int,input().split()))
        list_of_ladders.append(Ladder(start_end[0],start_end[1]))
    
    list_of_players = []
    print("Enter first player's details:")
    list_of_players.append(Player(input(),1))
    print("Enter second player's details:")
    list_of_players.append(Player(input(),2))

    boardGame = BoardService(100)
    boardGame.set_players(list_of_players)
    boardGame.set_snakes(list_of_snakes)
    boardGame.set_ladders(list_of_ladders)

    boardGame.startgame()
