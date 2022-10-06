import pygame
import random
from pprint import pprint
clock = pygame.time.Clock()
fps=60

res= 115

def one_of_three():
	if random.randint(0,8)==0:
		return 1

life = [ [ one_of_three() for _ in range(res)] for _ in range(res)]

pygame.init()

WIDTH, HEIGHT = 1000,1000

screen = pygame.display.set_mode([WIDTH, HEIGHT])

BLACK = (0,0,0)
WHITE = (255,255,255)

def check_neighbours(x,y):
	sum = 0
	for i in range(-1,2):
		for j in range(-1,2):
			if i==0 and j==0:
				continue
			if life[(x+i+res)%res][(y+j+res)%res] == 1:
				sum+=1
	return sum

new_gen=[[0 for _ in range(res)] for _ in range(res)]

#print(new_gen)

def next_life(x,y):
	#for x in range(res):
		#for y in range(res):
			neighbours = check_neighbours(x,y)
			if (life[x][y]==1 and neighbours in range(2,4)) or (life[x][y]==0 and neighbours==3):
				new_gen[x][y]=1
			else:
				new_gen[x][y]=0
	
			
			


def game_of_life():
	global life
	for i in range(res):
		for j in range(res):
			if life[i][j]== 1:
				pygame.draw.rect(screen, WHITE, pygame.Rect(
		i*(WIDTH/res), j*(HEIGHT/res), WIDTH/res, HEIGHT/res)) 
			next_life(i,j)
	life = new_gen

	
	
def border(w, color=WHITE):
    pygame.draw.line(screen, color, (1, 0), (1, WIDTH), w)
    pygame.draw.line(screen, color, (0, 0), (HEIGHT, 0), w)
    pygame.draw.line(screen, color, (WIDTH - w, 0),
                     (HEIGHT- w, WIDTH), w)
    pygame.draw.line(screen, color, (0, WIDTH), (HEIGHT, WIDTH), w)


running= True
while running:
	#pprint(life)
	#print()
	clock.tick(fps)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill(BLACK)
	#border(1)
	game_of_life()
	
	
	#pygame.draw.circle(screen,(0,0,255),(250,250),75)
	pygame.display.flip()
	
pygame.quit()
#pprint(life)
