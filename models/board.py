class Board:
    def __init__(self,Size):
        self.__boardSize = Size
        self.__snakes = None
        self.__ladders = None
        self.__players = None

    def get_size(self):
        return self.__boardSize
    
    def get_snakes(self):
        return self.__snakes
    
    def get_ladders(self):
        return self.__ladders
    
    def get_players(self):
        return self.__players
    
    def set_snakes(self,snakes_list):
        self.__snakes = snakes_list
    
    def set_ladders(self,ladders_list):
        self.__ladders = ladders_list
    
    def set_players(self,players_dict):
        self.__players = players_dict

