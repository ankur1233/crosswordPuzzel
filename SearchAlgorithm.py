# -*- coding: utf-8 -*-


"""
Approach:
- Build hash-set using Listwords.txt file. This is our valid dictionary.
- Generate ROW X COL size grid using python lists. Assign random characters from (a-z) to each cell in this grid.
  - display the grid on terminal.
- From any location (i,j) in this grid, words can be formed in any of 8 directions by going to east, west, north,
  south, north-east, north-west, south-east, south-west.
  - for each string made check if it exists in the hash-set, i.e., if it is valid.
  - valid string will be added to result set, containing unique words.
  - display the result on terminal.
"""


import sys
import random
import datetime


class SearchAlgorithm(object):
    """
    Class that searches a grid of letters (a-z only) for valid English words. Words can be found along any diagonal,
    forwards, upwards, downwards or backwards and must not ‘wrap’ between edges.
    """

    def __init__(self, cols, rows):
        """
        Initialize WordSearch object.
        :param cols:
        :param rows:
        """
        self.cols = cols
        self.rows = rows
        self.cut_off = None
        self.wordSet = None
        self.board = None

    def add_word(self, word):
        """
        Adding a word in the hash-set structure
        """
        self.wordSet.add(word)

    def getAllWords(self, file):
        """
        get Input file into hash set.
        """
        self.cut_off = 0
        self.wordSet = set()
        # Read a Text File Line by Line Using an Iterator in Python
        Obj = open(file)
        for line in Obj:
            line_cleaned = line.strip().lower()
            self.add_word(line_cleaned)
            n_line = len(line_cleaned)
            if n_line > self.cut_off:
                self.cut_off = n_line
        Obj.close()


    def grid(self):
        """
        Create random grid of (grid of letters (a-z only))
        """
        print ("Puzzle Grid: %d X %d" % (self.rows, self.cols))
        alphabets="abcdefghijklmnopqrstuvwxyz"
        self.board = list()
        for i in range(self.rows):
            a_row = list()
            for j in range(self.cols):
                a_row.append(random.choice(alphabets))
            self.board.append(a_row)
            print (a_row)


    def validWords(self, word):
        """
        Check if a word exists in wordSet.
        """
        validFlag = word in self.wordSet
        return validFlag

    def getWords(self):
        """
        get all words from list of words
        """
        result_set = set()
        for i in range(self.rows):
            for j in range(self.cols):
                # (i, j) new start point

                # East
                kC=j
                nC = min(self.cols, kC+self.cut_off)
                while(kC < nC):
                    # word = board[i][kC:nC]
                    q=kC
                    word = list()
                    while(q < nC):
                        word.append(self.board[i][q])
                        q+=1
                    word = "".join(word)
                    if (self.validWords(word)):
                        result_set.add(word)
                    nC -= 1

                # West
                kC=j
                nC = max(-1, kC-self.cut_off)
                while(kC > nC):
                    # word = board[i][kC:nC]
                    q=kC
                    word = list()
                    while(q > nC):
                        word.append(self.board[i][q])
                        q-=1
                    word = "".join(word)
                    if (self.validWords(word)):
                        result_set.add(word)
                    nC += 1

                # North
                kR=i
                nR = max(-1, kR-self.cut_off)
                while(kR > nR):
                    # word = board[kR:nR][j]
                    p=kR
                    word = list()
                    while(p > nR):
                        word.append(self.board[p][j])
                        p-=1
                    word = "".join(word)
                    if (self.validWords(word)):
                        result_set.add(word)
                    nR += 1

                # South
                kR=i
                nR = min(self.rows, kR+self.cut_off)
                while(kR < nR):
                    # word = board[kR:nR][j]
                    p=kR
                    word = list()
                    while(p < nR):
                        word.append(self.board[p][j])
                        p+=1
                    word = "".join(word)
                    if (self.validWords(word)):
                        result_set.add(word)
                    nR -= 1

                # North East
                kR=i
                kC=j
                nR = max(-1, kR-self.cut_off)
                nC = min(self.cols, kC+self.cut_off)
                while(kR > nR and kC < nC):
                    # word = board[kR:nR][kC:nC]
                    p=kR
                    q=kC
                    word = list()
                    while(p > nR and q < nC):
                        word.append(self.board[p][q])
                        p-=1
                        q+=1
                    word = "".join(word)
                    if (self.validWords(word)):
                        result_set.add(word)
                    nC -= 1
                    nR += 1

                # North West
                kR=i
                kC=j
                nR = max(-1, kR-self.cut_off)
                nC = max(-1, kC-self.cut_off)
                while(kR > nR and kC > nC):
                    # word = board[kR:nR][kC:nC]
                    p=kR
                    q=kC
                    word = list()
                    while(p > nR and q > nC):
                        word.append(self.board[p][q])
                        p-=1
                        q-=1
                    word = "".join(word)
                    if (self.validWords(word)):
                        result_set.add(word)
                    nC += 1
                    nR += 1

                # South East
                kR=i
                kC=j
                nR = min(self.rows, kR+self.cut_off)
                nC = min(self.cols, kC+self.cut_off)
                while(kR < nR and kC < nC):
                    # word = board[kR:nR][kC:nC]
                    p=kR
                    q=kC
                    word = list()
                    while(p < nR and q < nC):
                        word.append(self.board[p][q])
                        p+=1
                        q+=1
                    word = "".join(word)
                    if (self.validWords(word)):
                        result_set.add(word)
                    nC -= 1
                    nR -= 1

                # South West
                kR=i
                kC=j
                nR = min(self.rows, kR+self.cut_off)
                nC = max(-1, kC-self.cut_off)
                while(kR < nR and kC > nC):
                    # word = board[kR:nR][kC:nC]
                    p=kR
                    q=kC
                    word = list()
                    while(p < nR and q > nC):
                        word.append(self.board[p][q])
                        p+=1
                        q-=1
                    word = "".join(word)
                    if (self.validWords(word)):
                        result_set.add(word)
                    nC += 1
                    nR -= 1

        return result_set

