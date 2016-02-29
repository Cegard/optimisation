#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import floor, log10


class Puzzle:
    
    
    def __init__(self, length):
        """
        Creates an ordered puzzle of dimension lengthXlength with length > 1
        :param length: Int the size of the edge of the puzzle 
        """
        
        if (length <= 1 or length.__class__ != int):
            
            try:
                raise ValueError('length must be an integer greater than 1')
            
            except:
                print('something went wrong!')
                raise
        
        self._length = length
        self._movements = [True, False, True, False] # up, down, left, right
        self._blank_box = (length-1, length-1)
        self._board = [[i*length+j+1 for j in range(length)] for i in range(length)]
        self._board[length-1][length-1] = None
    
    
    def is_ordered(self, ):
        position = 0
        is_correct = True
        
        while(position < self._length**2-2 and is_correct):
            actual = self.__get_box(position)
            position += 1
            next_one = self.__get_box(position)
            is_correct = bool(next_one and actual and actual < next_one)
        
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
        #print(new_row)
        self._board[self._blank_box[0]][self._blank_box[1]] = \
                self.__get_box((new_row*self._length)+new_col)
        self._board[new_row][new_col] = None
        self._blank_box = (new_row, new_col)
        self.__calculate_movements()
    
    
    def __calculate_movements(self, ):
        self._movements = [(self._blank_box[0] > 0), (self._blank_box[0] < self._length-1),
            (self._blank_box[1] > 0), (self._blank_box[1] < self._length-1)]
    
    
    def __str__(self, ):
        puzzle = ''
        max_digits = floor(log10(self._length**2))+1
        
        for i in range(self._length**2):
            puzzle += ' ' + ' ' * (max_digits-floor(log10(self.__get_box(i) or 1)+1)) \
                    + str(self.__get_box(i) or 'X') + \
                    ('\n' if i%self._length == self._length-1 else '') 
        
        return puzzle
    
    
    def __get_box(self, position):
        """
        Gets the item at the exact coordinate in the board
        :param position: An integer representation of the position.
        :returns: The item at the coordinate ((position/length), (position%length))
        """
        return self._board[position//self._length][position%self._length]
    