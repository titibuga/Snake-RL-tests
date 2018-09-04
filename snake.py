#!/usr/bin/env python3

from collections import deque
from point import Point
from misc import *

class Snake:

    def __init__(self):
        self.head_pos = Point(5,5)
        self.orientation = Directions.UP
        self.length = 5
        self.food_reserve = 0
        self.body_pos_list = deque(Point(5, y) for y in
                                   reversed(range(1,5)))
        self.isAlive = True

    def __repr__(self):
        return str(self.head_pos) + '\n' + '\n'.join(str(e) for e in
                                                      self.body_pos_list)

    def getPositions(self):
        return (self.head_pos, self.body_pos_list.copy())

    def update(self, cmd):
        if(not self.isAlive):
            return

    def feed(self, amount=1):
        self.food_reserve += amount

    def kill(self):
        self.isAlive = False
                                            
                                            
                                            
                                            
