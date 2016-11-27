# The overall app framework is that we have two objects:
# First the cell
from cell import cell
# The cell object is either alive or dead and can live/die

# Second, we have the board
from board import board
# The board class defines the boardspace & its methods
# E.g.: cell by cell evolution, boundary conditions
# handling, board resizing, and graphical rendering

# another useful lib - allows time delay in graphics rendering
import time
import random

# # Let's run a simple test of the import
# a = cell()
# a.live()
# print(a.isalive)
# a.die()
# print(a.isalive)
# # Seems to be working

len = 40
b = board(len,len)

### INITIALIZATION ###

# Board with top & left edges alive
for i in range(0,len):
    b.stork(0,i)
    b.stork(i,0)

# # Random board
# for i in range(0,len):
#     for j in range(0,len):
#         if random.randint(0,1) == 1:
#             b.stork(i,j)

b.disp()

# evolve the board freq times per second over t seconds
t = 15
freq = 10
for i in range(0,t*freq):
    b.evolve()
    b.disp()
    time.sleep(1/freq)
