# -*- coding: utf-8 -*-
from copy import deepcopy
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
        
        self.__length = length
        self.__possibilities = (True, False, True, False) # up, down, left, right
        self.__blank_box = (length-1, length-1)
        self.__board = [[i*length+j+1 for j in range(length)] for i in range(length)]
        self.__board[length-1][length-1] = None
        self.__sorted = deepcopy(self.__board)
        self.__previous_move = ''
        
    
    
    def is_ordered(self, ):
        return self.__board == self.__sorted
    
    
    def swap(self, direction):
        """
        Changes the position of the blank box
        :param direction: the direction to move the blank box, it must be either
        one of up, down, left or right
        """
        directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1),}
        new_row = self.__blank_box[0] + directions[direction][0]
        new_col = self.__blank_box[1] + directions[direction][1]
        new_position = self.__get_box((new_row*self.__length)+new_col)
        self.__board[self.__blank_box[0]][self.__blank_box[1]] \
                = new_position
        self.__board[new_row][new_col] = None
        self.__blank_box = (new_row, new_col)
        self.__set_possibilities()
        self.__previous_move = direction
    
    
    def __set_possibilities(self, ):
        self.__possibilities = ((self.__blank_box[0] > 0), (self.__blank_box[0] < self.__length-1),
            (self.__blank_box[1] > 0), (self.__blank_box[1] < self.__length-1))
    
    
    def __get_box(self, position):
        """
        Gets the item at the exact coordinate in the board
        :param position: An integer representation of the position.
        :returns: The item at the coordinate ((position/length), (position%length))
        """
        return self.__board[position//self.__length][position%self.__length]
    
    
    def __eq__(self, other):
        return self.__board == other.board
    
    
    def __str__(self, ):
        puzzle = ''
        max_digits = floor(log10(self.__length**2))+1
        last_col = self.__length-1
        
        for i in range(self.__length**2):
            digits = floor(log10(self.__get_box(i) or 1)+1)
            actual_col = i%self.__length
            puzzle += ' ' + ' ' * (max_digits-digits) \
                    + str(self.__get_box(i) or 'X') \
                    + ('\n' if actual_col == last_col else '') 
        
        return puzzle
    
    
    @property
    def previous_move(self, ):
        return self.__previous_move
    
    
    @property
    def length(self, ):
        return self.__length
    
    
    @property
    def possibilities(self, ):
        return self.__possibilities
    
    
    @property
    def blank_box(self, ):
        return self.__blank_box
    
    
    @property
    def board(self, ):
        return deepcopy(self.__board)