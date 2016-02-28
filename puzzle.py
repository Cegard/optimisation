#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Puzzle:
    
    
    def __init__(self, length):
        """
        Creates an ordered puzzle of dimension lengthXlength
        :param length: the size of the edge of the puzzle 
        """
        self._length = length
        self._movements = [True, False, True, False] # up, down, left, right
        self._blank_box = (length-1, length-1)
        self._board = [[i*length+j+1 for j in range(length)] for i in range(length)]
        self._board[length-1][length-1] = None
    
    
    def is_ordered(self, ):
        previous = self._board[0]
        row = 0
        is_correct = True
        
        while(row < self._length and is_correct):
            col = 0
            
            while(col < self._length and is_correct):
                is_correct = True if previous < self._board[row][col] else False
                col += 1
            
            row += 1
        
        return is_correct
    
    
    def swap(self, direction):
        """
        Changes the position of the blank box
        :param direction: the direction to move the blank box, it must be either
        one of up, down, left or right
        """
        directions = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}
        new_row = self._blank_box[0] + directions[direction][0]
        new_col = self._blank_box[1] + directions[direction][1]
        self._board[self._blank_box[0]][self._blank_box[1]] = self._board[new_row][new_col]
        self._board[new_row][new_col] = None
        self._blank_box = (new_row, new_col)
        self.__calculate_movements()
    
    
    def __calculate_movements(self, ):
        self._movements = [(self._blank_box[0] > 0), (self._blank_box[0] < self._length-1),
            (self._blank_box[1] > 0), (self._blank_box[1] < self._length-1)]