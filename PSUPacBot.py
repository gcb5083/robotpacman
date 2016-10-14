#!/usr/bin/env python
import random

#this is a simulation for the PacBot

def setupArena(r,c):
    arena = [[0 for x in range(r)] for y in range(c)]
    g1 = (random.randint(0,r-1),random.randint(0,c-1))
    g2 = (random.randint(0,r-1),random.randint(0,c-1))
    g3 = (random.randint(0,r-1),random.randint(0,c-1))
    g4 = (random.randint(0,r-1),random.randint(0,c-1))
    for i in range(0,r):
        for j in range(0,c):
            arena[i][j] = u"\u2610"
    arena[g1[0]][g1[1]] = "G1"
    arena[g2[0]][g2[1]] = "G2"
    arena[g3[0]][g3[1]] = "G3"
    arena[g4[0]][g4[1]] = "G4"
    lstGhstPos = [g1,g2,g3,g4]
    for i in range(0,len(arena)):
        for j in range(0,len(arena[0])):
            print(arena[i][j],end = " ")
        print()
    return arena,lstGhstPos

def updatePosGhost(posG,arena,mvDist,num):
    x = posG[0]
    y = posG[1]
    changeX,changeY = 0,0
    arena[x][y] = u"\u2610"
    #10/3/16 Saimun Shahee: the purpose of the second condition for each of the if statements is to check whether or not a Ghost already exists in that position
    #hence the "(x-1,y) not in listOfGhostPositions"
    if max(mvDist) == mvDist[0] and (x-1,y) not in listOfGhostPositions:
        changeX = -1
    elif max(mvDist) == mvDist[2] and (x+1,y) not in listOfGhostPositions:
        changeX = 1
    elif max(mvDist) == mvDist[1] and (x,y-1) not in listOfGhostPositions:
        changeY = -1
    elif max(mvDist) == mvDist[3] and (x,y+1) not in listOfGhostPositions:
        changeY = 1
    arena[x + changeX][y + changeY] = "G"+str(num)

    return arena,(x + changeX,y + changeY)

def mvDist(posG,arena):
    distList = []
    for k in range(0,5):
        distList.append(random.random())
    if posG[0] == 0:
        distList[0] = 0
    if posG[1] == 0:
        distList[1] = 0
    if posG[0] == len(arena)-1:
        distList[2] = 0       
    if posG[1] == len(arena[0])-1:
        distList[3] = 0
    return distList


board,listOfGhostPositions = setupArena(10,10)

for i in range(10):
    print()
    board,listOfGhostPositions[0] = updatePosGhost(listOfGhostPositions[0],board,mvDist(listOfGhostPositions[0],board),1)
    board,listOfGhostPositions[1] = updatePosGhost(listOfGhostPositions[1],board,mvDist(listOfGhostPositions[1],board),2)
    board,listOfGhostPositions[2] = updatePosGhost(listOfGhostPositions[2],board,mvDist(listOfGhostPositions[2],board),3)
    board,listOfGhostPositions[3] = updatePosGhost(listOfGhostPositions[3],board,mvDist(listOfGhostPositions[3],board),4)
    #10/3/16 Saimun Shahee: I changed the location for printing the board from inside the function to outside since when you change the position of x many ghosts it
    #unnecessarily prints the board x amount of times. So this is just for a cleaner output.
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            print(board[i][j],end = " ")
        print()
