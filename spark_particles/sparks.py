import pygame
import math
import random
#from helper import *
import time

pygame.init()

WIDTH, HEIGHT = 1000,1000

SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()



#------------------------------------------

BLACK = (0,0,0)
WHITE = (255,255,255)


class Particle:
	def __init__(self,pos,theta=0,lifetime=1,vel=2,acc =1,scale=1):
		self.pos = pos
		self.theta = theta
		self.vel = vel
		self.acc = acc
		self.scale = scale
		
		self.length = 60
		
		self.creation_time= time.time()
		self.lifetime = lifetime
		self.lifetime_left = self.lifetime
		
		angle = math.radians(self.theta)
		self.cos = self.scale*math.cos(angle)
		self.sin = self.scale*math.sin(angle)
		self.angleAB = None
		#self.self_kill()
		

	
	def calc_points(self,pos):
		angle = math.radians(self.theta)
		self.cos = self.scale*math.cos(angle)
		self.sin = self.scale*math.sin(angle)
		cos,sin = self.cos,self.sin
		x,y = pos.xy
		scale = self.scale
		
		
		points = [
						[x,y],
						[x+45*cos+5*sin,y-45*sin-5*cos],
						[x+60*cos,y-60*sin],
						[x+45*cos-5*sin,y-45*sin+5*cos]
		]
		head = 60*self.lifetime_left/self.lifetime
		points = [
						[x,y],
						[x+3/4*head*cos+head/12*sin,y-3/4*head*sin-head/12*cos],
						[x+head*cos,y-head*sin],
						[x+3/4*head*cos-head/12*sin,y-3/4*head*sin+head/12*cos],
		]
		'''
		l = self.length
		lifetime_effect = self.lifetime_left/self.lifetime
		
		height = l*lifetime_effect
		center = 3/4*height
		fin = height/12
		points = [
						[x,y],
						[x+center*cos+fin*sin,y-center**sin-fin*cos],
						[x+height*cos,y-height*sin],
						[x+center*cos-fin*sin,y-center*sin+fin*cos]
		]
		
		A = pos
		B = pygame.math.Vector2(x+45,y-5)
		
		if not AB:
			AB = B - A

		
		AC = pygame.math.Vector2(1,0)

		D = pygame.math.Vector2(x+45,y+5)
		AD = D - A
		
		AB.rotate(self.theta-AC.angle_to(AB))
		AD.rotate(self.theta-AC.angle_to(AB))
		
			#print(AB.x)
		points = [
						[x,y],
						#[x+lenAB*cosAB,y+lenAB*sinAB],
						[*AB.xy],
						[x+60*cos,y-60*sin],
						[x+45*cos-5*sin,y-45*sin+5*cos]
		]
		#pygame.draw.circle(SCREEN,"blue",(x+lenAB*cosAB,y-lenAB*sinAB),10)
		#pprint((self.angleAB), SCREEN)'''
		
		
		return points

	def effect(self):
		self.pos.x += self.vel*self.cos
		self.pos.y -= self.vel*self.sin
		self.vel+=self.acc
		self.theta -= self.vel#random.randint(-4,8)
		
	def life(self):
		time_passed = time.time() - self.creation_time
		self.lifetime_left = self.lifetime - time_passed 
		
	def draw(self):
		points = self.calc_points(self.pos)
		#lx, ly = zip(*points)
		#min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
		#target_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
		#shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
		#pprint(round(self.theta,2),SCREEN,self.pos.xy,20)
		pygame.draw.polygon(SCREEN, (255,255,255), points)
		#SCREEN.blit(shape_surf, target_rect)
	
	
	'''def self_kill(self):
		if self.lifetime==0:
			self.__del__()'''
	
	
	
	
	
	
	
	
	
def border(w, color=WHITE):
    pygame.draw.line(SCREEN, color, (1, 0), (1, WIDTH), w)
    pygame.draw.line(SCREEN, color, (0, 0), (HEIGHT, 0), w)
    pygame.draw.line(SCREEN, color, (WIDTH - w, 0),
                     (HEIGHT- w, WIDTH), w)
    pygame.draw.line(SCREEN, color, (0, WIDTH), (HEIGHT, WIDTH), w)








pos = pygame.math.Vector2(WIDTH//2,HEIGHT//2)
sparks = []


def create_data(mouse_pos,range):
		origin = pygame.math.Vector2(mouse_pos)
		
		
		Range = range 
		#x = random.randint(WIDTH//2-Range,WIDTH//2+Range)
		#y = random.randint(HEIGHT//2-Range,HEIGHT//2+Range)
		
		
		r= random.randint(0,Range)
		angle = math.radians(random.randint(0,360))
		x = origin.x + r * math.cos(angle)
		y = origin.y + r * math.sin(angle)
		
		

		
		
		pos = pygame.math.Vector2(x,y)
		AP = pos - pygame.math.Vector2(origin)
		A1 = pygame.math.Vector2(1,0)
		angle = -A1.angle_to(AP)
		
		return pos,angle






running = True
while running:
	clock.tick(60)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	SCREEN.fill(BLACK)
	border(1)
	mouse_pos = pygame.mouse.get_pos()
	for i in range(5):
		sparks.append(Particle(*create_data(mouse_pos,100),
			lifetime= 1,
			vel= 4,#random.randint(2,8),
			acc = 0.1,
			scale=0.5))

		
	pygame.draw.circle(SCREEN,"white",mouse_pos,5)
	for particle in sparks:
		particle.draw()
		particle.life()
		#particle.theta+=10
		#particle.pos.y+=5
		#pprint(particle.lifetime_left,SCREEN,particle.pos.xy,30)
		if particle.lifetime_left <= 0:
			sparks.remove(particle)
		#pprint(len(sparks),SCREEN,(10,10),60)
		particle.effect()
	#pprint(len(sparks),SCREEN)
	particle.theta+=0


	pygame.display.flip()
	
pygame.quit()
