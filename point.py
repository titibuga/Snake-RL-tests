#!/usr/bin/env python3

class Point:

    def __init__(self):
        self.x = 0
        self.y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return ("Point(%d, %d)" % (self.x, self.y))

         
            
