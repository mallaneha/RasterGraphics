import pygame
import pygame.gfxdraw
 
# Initializing the game engine
pygame.init()
 
# Colors in RGB format
white = (255, 255, 255)
black = (0, 0, 0)

# height and width of the screen
width = 500
height = 500
screen = pygame.display.set_mode([width, height], pygame.RESIZABLE)
pygame.display.set_caption("Mid Point Circle Drawing Algorithm")

# Function for mid point circle drawing algo
def MidPointCircle(xc, yc, radius):
	x0, y0 = 0, radius
	pygame.gfxdraw.pixel(screen, xc + x0, yc + y0, white)
	EightPointSymmetricity(x0 ,y0, xc, yc)

    # initial decision parameter
	if type(radius) == float:
		p0 = (5/4)  - radius
	else:
		p0 = 1 - radius

	pk = p0
	x, y = x0, y0

	while x <= y:
		if pk < 0:
			x, y = x + 1, y
			pk = pk + 2 * x + 1
			pygame.gfxdraw.pixel(screen, x + xc, y + yc, white)
			EightPointSymmetricity(x, y, xc, yc)
		else:
			x, y = x + 1, y - 1
			pk = pk + 2 * x - 2 * y + 1
			pygame.gfxdraw.pixel(screen, x + xc, y + yc, white)
			EightPointSymmetricity(x, y, xc, yc)

# Drawing pixels using Circle's 8 point symmetric property
def EightPointSymmetricity(x,y,xc,yc):
	pygame.gfxdraw.pixel(screen, x + xc, -y + xc, white)
	pygame.gfxdraw.pixel(screen, -x + xc, y + yc, white)
	pygame.gfxdraw.pixel(screen, -x + xc, -y + yc, white)
	pygame.gfxdraw.pixel(screen, y + xc, x + yc, white)
	pygame.gfxdraw.pixel(screen, y + xc, -x + yc, white)
	pygame.gfxdraw.pixel(screen, -y + xc, -x + yc, white)
	pygame.gfxdraw.pixel(screen, -y + xc, x + yc, white)


done = False

while not done:
    # If user clicks close
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
     
    # The screen background as white
    screen.fill(black)
    
    # circle with radius 100 & center at 230, 230
    MidPointCircle(230, 230, 100)
    
    # Update the contents of the entire display
    pygame.display.flip()
    
pygame.quit()