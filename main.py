import pygame
import random
from enum import Enum
from collections import namedtuple # assign meaning to each position.
pygame.init()

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3 
    DOWN = 4

Point = namedtuple('Point','x', 'y')

BLOCK_SIZE = 20
class SnakeGame:

    def __init__(self, w=640,h=480) -> None:
        self.w = w
        self.h = h
        # init display 
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('snake')
        self.clock = pygame.time.clock()

        #init game state
        self.direction = Direction.RIGHT

        self.head = Poing(self.w/2, self.h/2)
        self.snake = [self.head, Point(self.head.x-BLOCK_SIZE, self.head.y), Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]
        self.score = 0
        self.food = None
        self._place_food()
    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y = random.randint(0, (self.w-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
    def play_step(self):
        pass

if __name__=='__main__':
    game =SnakeGame()

    #game loop
    while True:
        game.play_step()

        #break if game over

    
    pygame.quit()