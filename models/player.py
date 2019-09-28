class Player:
    def __init__(self,PlayerName, PlayerID):
        self.__playerName = PlayerName
        self.__playerID = PlayerID
        self.__Position = 0
    
    def get_name(self):
        return self.__playerName
    
    def get_id(self):
        return self.__playerID
    
    def get_position(self):
        return self.__Position
    
    def set_position(self,newPosition):
        self.__Position = newPosition
