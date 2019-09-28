import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from random import randrange

class DiceRollService:
    def __init__(self):
        pass

    @staticmethod
    def get_value():
        return randrange(1,6)