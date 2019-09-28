import os 
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from SNAKE_AND_LADDER.models.board import Board
from SNAKE_AND_LADDER.services.dicerollservice import DiceRollService
from SNAKE_AND_LADDER.models.player import Player
from SNAKE_AND_LADDER.models.snake import Snake
from SNAKE_AND_LADDER.models.ladder import Ladder

class BoardService:
    def __init__(self,board_size):
        self.__Board = Board(board_size)
        self.__PlayersTurn = []
        self.__total_players = 0
        print("BoardSize set is : =",str(board_size))
    
    def set_players(self,list_of_players):
        players_dict = {}
        self.__total_players= len(list_of_players)
        for player in list_of_players:
            (self.__PlayersTurn).append(player)
            players_dict.update({player.get_id():0})
    
        self.__Board.set_players(players_dict)

    def set_snakes(self,list_of_snakes):
        self.__Board.set_snakes(list_of_snakes)
    
    def set_ladders(self,list_of_ladders):
        self.__Board.set_ladders(list_of_ladders)
    
    def get_new_position(self,new_pos):

        prev_pos = 0

        while True:
            prev_pos = new_pos
            for snake in self.__Board.get_snakes():
                if snake.get_snake_head() == new_pos:
                    new_pos = snake.get_snake_tail()
            for ladder in self.__Board.get_ladders():
                if ladder.get_start_point() == new_pos:
                    new_pos = ladder.get_end_point()
            
            if new_pos == prev_pos:
                break
        return new_pos
    
    def move_player(self,player,pos):
        old_position = self.__Board.get_players()[player.get_id()]
        new_pos = old_position + pos

        if new_pos > self.__Board.get_size():
            new_pos = old_position
        else:
            new_pos = self.get_new_position(new_pos)

        self.__Board.get_players()[player.get_id()] = new_pos
        print(player.get_name() + " rolled a " + str(pos) + " and moved from " + str(old_position) + " to " + str(new_pos))
    
    def get_value_from_dice_roll(self):
        return DiceRollService.get_value()

    def hasplayerwon(self,player):

        if self.__Board.get_players()[player.get_id()] == self.__Board.get_size():
            print(player.get_name() + " has won the game.")
            return True
        else:
            return False
    
    def isgamecompleted(self):
        if len(self.__PlayersTurn) < self.__total_players:
            return True
        else:
            return False
    
    def startgame(self):
        
        while not self.isgamecompleted():
            dice_value = self.get_value_from_dice_roll()
            player = self.__PlayersTurn.pop(0)
            self.move_player(player,dice_value)

            if not self.hasplayerwon(player):
                self.__PlayersTurn.append(player)

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
