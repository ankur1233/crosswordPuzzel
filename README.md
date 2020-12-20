# crosswordPuzzel


## Requirements

Word searches are a fun (or tedious, depending on your personality) puzzle where words are
hidden in a grid of seemingly random letters. Humans are fairly slow at solving word search
puzzles, at least when compared to a computer.
Your task is to write a Python program that searches a grid of letters (a-z only) for valid English
words much more quickly than any human possibly could. Words can be found along any
diagonal, forwards, upwards, downwards or backwards and must not ‘wrap’ between edges.

You may use the provided list of words as a dictionary for this task.

Your program should be able to:

● Generate a board of random letters. - Done

● Identify all valid words (contained in the attached word list) in the board. - Done

● Display results to the user. - Done

Things we like to see:

● Unit tests. - Done 
● Docstrings.
● Usage information. - 
● Command-line parameters. - Done
● Reasonable performance (<0.5s for a 15x15 board)
Rules:
● Any version of Python greater than 2.7 or 3.4 may be used. 

## Python version
Python > 3.2


## Run 

python Puzzel.py --rowls 12 --cols 12 --fileName Listwords.txt

## Run Test

python test_puzzel.py


## Command-line parameters

--rows

--cols

--fileName


