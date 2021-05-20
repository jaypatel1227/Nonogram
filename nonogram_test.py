import numpy  as np
from nonogram import Nonogram, clues

# We fix the game board to be of size n by n here
GAMESIZE = 10

# x = Nonogram(GAMESIZE, np.ones((GAMESIZE,GAMESIZE), np.int8)) # the empty board
# for i in range(GAMESIZE):
#     for j in range(GAMESIZE):
#         x.reveal(i,j)

# print(str(x))
# print(x.solved())

y = np.random.randint(1,3, size=(GAMESIZE, GAMESIZE)) 
nono = Nonogram(GAMESIZE, y)
rows, cols = clues(GAMESIZE, y)[0], clues(GAMESIZE, y)[1]
print(str(nono.key_repr()))
#print("Key: ", y)
print("Rows: ")
for x in rows:
    print(x)
print("Cols: ")
for y in cols:
    print(y)