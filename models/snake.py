class Snake:
    def __init__(self,head,tail):
        self.__head = head
        self.__tail = tail
    
    def get_snake_head(self):
        return self.__head
    
    def get_snake_tail(self):
        return self.__tail