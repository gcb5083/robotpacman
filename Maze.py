from Tile import Tile
from random import random,randint,seed
import os
from time import sleep
class NewMaze:



	def __init__(self,x,y):
		self.arena=[[Tile("Space") for row in range(y)] for col in range(x)]
		self.x=x
		self.y=y
		self.freq=.5
		self.pacmanPos=(1,1)
		self.__setPacmanPos(1,1)
		
		seed(5)

		wallpositions=[]
		for i in range(y): #set left and right walls
			self.arena[0][i].type="Wall"
			self.arena[x-1][i].type="Wall"

		for i in range(x): #set top and bottom walls
			self.arena[i][0].type="Wall"
			self.arena[i][y-1].type="Wall"

		for i in range(1,x-1): #set walls randomly
			for j in range(1,y-1):
				if i%2==0 and j%2==0:
					self.arena[i][j].type="Wall"

				elif random()<=self.freq:
					self.arena[i][j].type="Wall"
					wallpositions.append((i,j))

		for i in range(1,self.x,2):
			for j in range(1,self.y,2): #visit all odd tiles
				print("x,y",i,j)
				self.arena[i][j].type="Space"
				#print("Tile:",i,j,"\n\n")
				wallCount=0
				adjacentPositions=[]
				if self.arena[i-1][j].getType()=="Wall":
					wallCount+=1
					if(not(i-1<=0 or j<=0 or j>=y-1 or i-1>=x-1)):
						adjacentPositions.append((i-1,j))
				if self.arena[i+1][j].getType()=="Wall":
					wallCount+=1
					#print("x:",i+1,"y:",j)
					if(not(j<=0 or i+1>=x-1 or j>=y-1 or i+1<=0)):
						adjacentPositions.append((i+1,j))
				if self.arena[i][j-1].getType()=="Wall":
					wallCount+=1
					if(not(i<=0 or j-1<=0 or i>=x-1 or j-1>=y-1)):
						adjacentPositions.append((i,j-1))
				if self.arena[i][j+1].getType()=="Wall":
					print("this runs at",i,j)
					wallCount+=1
					if(not(i<=0 or j+1<=0 or i>=x-1 or j+1>=y-1)):
						#print("a",i,j+1)
						adjacentPositions.append((i,j+1))


				print(adjacentPositions)

				desiredWallCount=randint(2,2)
				#print("Desired Walls",desiredWallCount)
				while(wallCount>desiredWallCount): #randomly remove adjacent walls until they hit the max allowed number (2)
					#print("Adjacent Walls:",adjacentPositions)
					#print(i,j,len(adjacentPositions))
					if(not(adjacentPositions)):
						break
					try:
						toRemove=randint(0,len(adjacentPositions)-1)
					except ValueError: #if len(adjacentPositions) is 1, just remove the only item
						toRemove=0
					#print("Removed index",toRemove)
					#print(adjacentPositions[toRemove])
					n,m=adjacentPositions[toRemove]
					self.arena[n][m].type="Space"
					adjacentPositions.pop(toRemove)
					wallCount-=1

		for i in range(1,self.x-1):
			for j in range(1,self.y-1):
				if self.arena[i][j].type=="Space":
					self.arena[i][j].type="Dot"


	def movepacman(self,direction): #returns true if the move worked, false if pacman tried to move into a wall
		if(direction=="up"):
			x,y=self.pacmanPos
			
			if y<0 or self.arena[x][y-1].type=="Wall":
				return False
			else:
				self.arena[x][y].pacman=False
				self.__setPacmanPos(x,y-1)
				return True
		elif(direction=="left"):
			x,y=self.pacmanPos
			if x<0 or self.arena[x-1][y].type=="Wall":
				return False
			else:
				self.arena[x][y].pacman=False
				self.__setPacmanPos(x-1,y)
				return True
		elif(direction=="down"):
			x,y=self.pacmanPos
			if y>=self.y or self.arena[x][y+1].type=="Wall":
				return False
			else:
				self.arena[x][y].pacman=False
				self.__setPacmanPos(x,y+1)
				return True
		if(direction=="right"):
			x,y=self.pacmanPos
			if x>=self.x or self.arena[x+1][y].type=="Wall":
				return False
			else:
				self.arena[x][y].pacman=False
				self.__setPacmanPos(x+1,y)
				return True




	def __setPacmanPos(self,x,y):
		if(self.arena[x][y].type!="Wall"):
			self.pacmanPos=x,y
			self.arena[x][y].pacman=True
		else:
			raise Exception("Tried to place pacman on a wall")


	def __str__(self):
		s=""
		for y in range(self.y):
			for x in range(self.x):
				s+=str(self.arena[x][y])
			s+="\n"

		return s

if __name__=="__main__":
	m=NewMaze(19,19)
	print(m)

	moves=["right"]*6 +["down"]*2
	#print(moves)
	for move in moves:
		sleep(1)
		m.movepacman(move)
		#os.system('cls')

		print(m)