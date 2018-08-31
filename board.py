#!/usr/bin/env python3

class Board:

    def __init__(self):
        self.width = 80
        self.height = 40
        self.board = [['-']*self.width for i in range(self.height)]

    def __repr__(self):
        answ = ''
        for l in self.board:
            answ += ''.join(l) + '\n'
        return answ
         
            
