# The overall app framework is that we have two objects:
# First the cell
from cell import cell
# The cell object is either alive or dead and can live/die

# Second, we have the board
from board import board
# The board class defines the boardspace & its methods
# E.g.: cell by cell evolution, boundary conditions
# handling, board resizing, and graphical rendering

# other classes I'm using
import time
import random
import math

# Create a blank board
len = 40
b = board(len,len)

### INITIALIZATION ###

# # Board with top left corner
# for i in range(0,math.floor(len/2)):
#     for j in range(0,math.floor(len/2)):
#             b.stork(i,j)

# # Board with top & left edges alive
# for i in range(0,len):
#     b.stork(0,i)
#     b.stork(i,0)

# Random board
for i in range(0,len):
    for j in range(0,len):
        if random.randint(0,1) == 1:
            b.stork(i,j)

### VISUALIZATION ###

b.disp()
# evolve the board 'freq' times per second over 't' seconds
t = 15
freq = 10
for i in range(0,t*freq):
    b.evolve()
    b.disp()
    time.sleep(1/freq)
