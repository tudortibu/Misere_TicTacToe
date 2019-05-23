'''
Game Intro

The base version of the game is 3 3x3 grids (the each of the grids are similar to the ones in the game of tic tac toe
The game is played by  2 players and each of the players take turns inputting Xs into the respective grids
When there is in a row in a grid that grid is considered "dead" and inputs can no longer be inputed in the grid
The player that completes 3 of a kind in the final grid loses the game
'''

'''
Game setup

The game will be represented by 1 array of 27 ints  Domain = [-1, 1]
0 means that the space is empty and a player can play place their input into the grid 
1 measn that the space in the grid is occupied by player input
-1 means that the space in the grid is empty but the space is in a dead grid, input is unavailable
'''
import numpy as np

def createGame (grids =3, rowLength=3) :
    grid = [0]*(grids * (rowLength*rowLength))
    return grid

def createAvailableSpaces (grid):
    agrid = []
    for itt in range(len(grid)):
        agrid.append(itt)
    return agrid


def input(grid, space):

    if(grid[space] == 0):
        print('legal move')
        grid[space] = 1
        grida = checkDeadGrid(grid, space)
    else:
        grida = grid
        print('illegal move')
    return grida

def checkDeadGrid(grid, space=-1):
    print("checking grid")
    if(space == -1):
        checkDeadGrid(grid, 0)
        checkDeadGrid(grid, 9)
        checkDeadGrid(grid, 18)

    elif(space > -1 and space< 27):
        gridNum = int( space/9)
        minNum = gridNum * 9
        for num in range(minNum, minNum+8):
            if grid[num] == -1:
                return grid
        for itt in range (2):
            row = itt
            if((grid[row*3 + minNum]) + (grid[row*3 + minNum +1]) + (grid[row*3 + minNum + 2])) == 3:

                return fillDeadGrid(grid, space)
            if(grid[minNum + row] + grid[minNum + 3 + row] + grid[minNum + 6 + row]) == 3:

                return fillDeadGrid(grid, space)
        if(grid[minNum] + grid[minNum+ 4] + grid[minNum+ 8]) == 3:

            return fillDeadGrid(grid, space)
        if(grid[minNum+2] + grid[minNum+ 4] + grid[minNum+ 6]) ==3:

            return fillDeadGrid(grid, space)
    else:
        print("invalid input")
    return grid

def fillDeadGrid(grid, space):
    print("filling grid")
    gridNum = int( space/9)
    minNum = gridNum * 9
    agrid = grid
    for num in range (minNum, minNum+9):
        if(grid[num] == 0):
            agrid[num] = -1

    return agrid

def updateAvailableSpaces(grid, agrid):
    agrid = []
    for itt in range(len(grid)):
        if ( int(grid[itt]) == 0):
          agrid.append(itt)

    return agrid

def printGrid(grid, grids=3, rowLength=3):
    gridSize = int( len(grid) / grids)
    print('-------------------------------------------------------------------------------')
    for row in range( rowLength):
        string = ''
        for g in range (grids):

            string  +=  " " + str(grid[gridSize*g +row*rowLength])
            string +=  " " + str(grid[gridSize* g +row*rowLength +1])
            string +=  " " + str(grid[gridSize* g +row*rowLength + 2])
            string +=  " |\t"
        print(string)
    print('-------------------------------------------------------------------------------')
    return

def printAvailableSpaces(grid):
    print(grid)