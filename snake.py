import tensorflow as tf
import pygame
import sys
import random
import matplotlib.pyplot as plt
import numpy as np
import os
from time import sleep

class Component:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	
	def getx(self): 
		return self.x
	def gety(self): 
		return self.y
	def setx(self,x):
		self.x=x
	def sety(self,y):
		self.y=y
		
class Snake:
	def __init__(self):
		self.start=False
		self.pos=[]
		self.side=0
		self.apple=[0,0]
		self.points=0
		self.reset()
	def reset(self):
		self.start=False
		print(str(self.points)+' points!')
		self.points=0
		self.pos.clear()
		self.pos.append(Component(random.randint(0,9),random.randint(0,9)))
		self.add()
		self.setapple()
	def add(self):
		self.pos.append(Component(-1,-1))
	def point(self):
		self.points+=1
		self.add()
		if len(self.pos)==256:
			reset()
		else:
			self.setapple()
	def getpoints(self):
		return self.points
	def setapple(self):
		czy=True
		while czy:
			czy=False
			self.apple[0]=random.randint(0,9)
			self.apple[1]=random.randint(0,9)
			for i in self.pos:
				if i.getx()==self.apple[0] and i.gety()==self.apple[1]:
					czy=True
					break
		
	def getapple(self):
		return self.apple
	def setside(self,side):
		self.side=side
		self.start=True
	def move(self):
		if self.start:
			if len(self.pos)==2:
				if self.side==0 and self.pos[0].getx()==self.pos[1].getx() and self.pos[0].gety()-1==self.pos[1].gety():
					self.reset()
					return True
				elif self.side==1 and self.pos[0].getx()+1==self.pos[1].getx() and self.pos[0].gety()==self.pos[1].gety():
					self.reset()
					return True
				elif self.side==2 and self.pos[0].getx()==self.pos[1].getx() and self.pos[0].gety()+1==self.pos[1].gety():
					self.reset()
					return True
				elif self.side==3 and self.pos[0].getx()-1==self.pos[1].getx() and self.pos[0].gety()==self.pos[1].gety():
					self.reset()
					return True
			
			for i in range(len(self.pos)-1,0,-1):
				self.pos[i].setx(self.pos[i-1].getx())
				self.pos[i].sety(self.pos[i-1].gety())
			if self.side==0:
				if self.pos[0].gety()==0:
					self.reset()
					return True
				else:
					self.pos[0].sety(self.pos[0].gety()-1)
			elif self.side==1:
				if self.pos[0].getx()==9:
					self.reset()
					return True
				else:
					self.pos[0].setx(self.pos[0].getx()+1)
			elif self.side==2:
				if self.pos[0].gety()==9:
					self.reset()
					return True
				else:
					self.pos[0].sety(self.pos[0].gety()+1)
			else:
				if self.pos[0].getx()==0:
					self.reset()
					return True
				else:
					self.pos[0].setx(self.pos[0].getx()-1)
			if self.pos[0].getx()==self.apple[0] and self.pos[0].gety()==self.apple[1]: self.point()
			for i in range(1,len(self.pos)):
				if self.pos[0].getx()==self.pos[i].getx() and self.pos[0].gety()==self.pos[i].gety():
					self.reset()
					return True
		return False
	def draw(self,window):
		for i in self.pos:
			pygame.draw.rect(window,(0,0,0),pygame.Rect(i.getx()*35,i.gety()*35,35,35))
		pygame.draw.rect(window,(255,0,0),pygame.Rect(self.apple[0]*35,self.apple[1]*35,35,35))

def game():
	pygame.init()
	window = pygame.display.set_mode((350, 350))
	pygame.display.set_caption(('Snake'))
	clock = pygame.time.Clock()
	snake=Snake()
	pygame.time.set_timer(25,250)
	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit(0)				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP: snake.setside(0)
				elif event.key == pygame.K_DOWN: snake.setside(2)
				elif event.key == pygame.K_RIGHT: snake.setside(1)
				elif event.key == pygame.K_LEFT: snake.setside(3)
			if event.type==25:
				snake.move()
		window.fill((255,255,255))
		for i in range(9):
			pygame.draw.line(window,(0,0,0),(i*35+35,0),(i*35+35,350),1)
			pygame.draw.line(window,(0,0,0),(0,i*35+35),(350,i*35+35),1)
		snake.draw(window)
		pygame.display.flip()
		clock.tick(60)

game()