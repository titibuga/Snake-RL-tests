#!/usr/bin/env python3

from collections import deque
from point import Point
from misc import *


class Snake:

    def __init__(self):
        self.head_pos = Point(5,5)
        self.orientation = Directions.UP
        self.length = 5
        self.body_pos_list = deque(Point(5, y) for y in
                                   reversed(range(1,5)))

    def __repr__(self):
        return str(self.head_pos) + '\n' + '\n'.join(str(e) for e in
                                                      self.body_pos_list)
                                            
                                            
                                            
                                            
