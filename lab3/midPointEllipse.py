import pygame
import pygame.gfxdraw
 
# Initializing the game engine
pygame.init()
 
# Colors in RGB format
white = (255, 255, 255)
black = (0, 0, 0)

# height and width of the screen
width = 400
height = 400
screen = pygame.display.set_mode([width, height], pygame.RESIZABLE)
pygame.display.set_caption("Mid Point Ellipse Drawing Algorithm")


# Function for mid point ellipse drawing algo
def MidPointEllipse(rx, ry, xc, yc):
    # Region 1
    x , y = 0 , ry
    pygame.gfxdraw.pixel(screen, x + xc, y + yc, white)
    OtherThreeQuadrants(x, y, xc, yc)

    # Initial decision parameter
    p1 = ry**2 - (rx**2 * ry) + (1/4)*(rx**2)
    A = 2 * ry**2 * x
    B = 2 * rx**2 * y

    while A < B:
        x = x + 1
        A = A + 2 * ry**2
        if p1 < 0:
            p1 = p1 + A + ry**2
        else:
            y = y -1
            B = B - 2 * rx**2
            p1 = p1 + A - B + ry**2
        pygame.gfxdraw.pixel(screen, x + xc, y + yc, white)
        OtherThreeQuadrants(x, y, xc, yc)

    # Region 2
    # Initial decision parameter
    p2 = ry**2 * (x + (1/2))**2 + rx**2 * (y-1)**2 - (rx**2 * ry**2)

    while y >= 0:
        y = y - 1
        B = B - 2 * rx**2
        if p2 > 0:
            p2 = p2 + rx**2 - B
        else:
            x = x+1
            A = A + 2 * ry**2
            p2 = p2 + A - B + rx**2
        pygame.gfxdraw.pixel(screen, x + xc, y + yc, white)
        OtherThreeQuadrants(x, y, xc, yc)


# Drawing pixels in other 3 quadrants
def OtherThreeQuadrants(x, y, xc, yc):
    pygame.gfxdraw.pixel(screen, x + xc, -y + yc, white)
    pygame.gfxdraw.pixel(screen, -x + xc, y + yc, white)
    pygame.gfxdraw.pixel(screen, -x + xc, -y + yc, white)


done = False

while not done:
    # If user clicks close
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
     
    # The screen background as white
    screen.fill(black)
    
    # circle with rx = 120, ry = 80 & center at 200, 200
    MidPointEllipse(120, 80, 200, 200)
    
    # Update the contents of the entire display
    pygame.display.flip()
    
pygame.quit()