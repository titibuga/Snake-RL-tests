#!/usr/bin/env python3

from snake import Snake

class Board:

    def __init__(self, snake, width = 80, height = 40):
        self.width = width
        self.height = height
        self.clearBoard()
        self.snake = snake
        self.food_list = []

    def __repr__(self):
        answ = ''
        for l in self.board:
            answ += ''.join(l) + '\n'
        return answ

    def clearBoard(self):
        # TODO: Look for a way to do this without creating new lists
        self.board = [['-']*self.width for i in range(self.height)]

    def placeFood():
        return 0
        
    def checkCollisions(self):
        isColliding = False
        self.clearBoard()
        placeFood()
        (headPos, bodyPosList) = self.snake.getPositions()
        if(self.board[headPos.x][headPos.y] != '-'):
            isColliding = True
        self.board[headPos.x][headPos.y] = '@'
        for p in bodyPosList:
            if(self.board[p.x][p.y] != '-'):
                isColliding = True
            self.board[p.x][p.y] = 'O'

        return isColliding

    def update(self, cmd):
        self.snake.update(cmd)
        if(self.checkCollisions()):
            self.snake.kill()
         
            
