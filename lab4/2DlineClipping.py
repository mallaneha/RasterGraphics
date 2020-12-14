import pygame
import pygame.gfxdraw
from math import floor

 
# Initializing the game engine
pygame.init()
 
# Colors in RGB format
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)

# height and width of the screen
width = 800
height = 800
screen = pygame.display.set_mode([width, height], pygame.RESIZABLE)
pygame.display.set_caption("CohenSutherland Line Clipping Algorithm")

# Defining region codes 
INSIDE = 0 # 0000 
TOP = 8	 # 1000 
BOTTOM = 4 # 0100 
RIGHT = 2 # 0010 
LEFT = 1 # 0001
TOPLEFT = 9 # 1001 
TOPRIGHT = 10 # 1010 
BOTTOMLEFT = 5 # 0101 
BOTTOMRIGHT = 6 # 0110 

# Defining x_max, y_max and x_min, y_min for rectangle 
xMin = 200
yMin = 200
xMax = 600
yMax = 500


# Function to compute region code for a point(x, y) 
def RegionCode(x, y):
    if x < xMin:
        if y < yMin:
            return BOTTOMLEFT
        elif y > yMax:
            return TOPLEFT
        return LEFT
    elif x > xMax: 
        if y < yMin:
            return BOTTOMRIGHT
        elif y > yMax:
            return TOPRIGHT
        return RIGHT
    else:
        if y < yMin:
            return BOTTOM
        elif y > yMax:
            return TOP
        return INSIDE	


# Function for line clipping
def CohenSutherland(x1, y1, x2, y2):
    code1 = RegionCode(x1, y1)
    code2 = RegionCode(x2, y2)

    if code1 == 0 and code2 == 0:
        # Entire line accepted
        pygame.gfxdraw.line(screen, x1, y1, x2, y2, green)
    else:
        if code1 & code2 != 0:
            # Entire line rejected
            pygame.gfxdraw.line(screen, x1, y1, x2, y2, red)
        else:
            codes = [0, 0]
            # for points outside clipping window
            if code1 != 0:
                codes[0] = code1
            if code2 != 0:
                codes[1] = code2
            
            index = 0
            m = (y2-y1)/(x2 - x1)
            for code in codes:
                if index == 0:
                    x0 = x1
                    y0 = y1
                else:
                    x0 = x2
                    y0 = y2

                while code != 0:
                    if code & 1 == 1:
                        # Clipping from Left
                        x = xMin
                        y = y0 + m * (x - x0)                   
                        code = RegionCode(x, y)
                        codes[index] = code
                    elif code & 2 == 2:
                        # Clipping from Right
                        x = xMax
                        y = y0 + m * (x - x0)
                        code = RegionCode(x, y)
                        codes[index] = code

                    if code == 8:
                        # Clipping from Top
                        y = yMax
                        x = x0 + (y - y0)/m
                        code = RegionCode(x, y)
                        codes[index] = code
                    elif code == 4:
                        # Clipping from Bottom
                        y = yMin
                        x = x0 + (y - y0)/m
                        code = RegionCode(x, y)
                        codes[index] = code

                    if index == 0:
                        x1, y1 = floor(x), floor(y)
                    else:
                        x2, y2 = floor(x), floor(y)
                
                index += 1
            pygame.gfxdraw.line(screen, x1, y1, x2, y2, cyan)


done = False

while not done:
    # If user clicks close
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
     
    # The screen background as black
    screen.fill(black)

    # Clipping window (coloured white)
    pygame.gfxdraw.polygon(screen,[(xMin,yMin),(xMax,yMin),(xMax,yMax),(xMin,yMax)],white)

    # Trivially rejected line
    CohenSutherland(100, 400, 100, 600)

    # Trivially accepted line
    CohenSutherland(330, 400, 490, 300)

    # Original line
    pygame.gfxdraw.line(screen, 100, 100, 300, 300, magenta)
    # Clipped line
    CohenSutherland(100, 100, 300, 300)

    # Original line
    pygame.gfxdraw.line(screen, 100, 100, 400, 650, magenta)
    # Clipped line
    CohenSutherland(100, 100, 400, 650)

    # Update the contents of the entire display
    pygame.display.flip()
    
pygame.quit()