import pygame
import pygame.gfxdraw
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)

#user input starting and ending points
x1, y1 = map(int,input("first point: ").split())
x2, y2 = map(int,input("second point: ").split())

screen = pygame.display.set_mode([400, 400], pygame.RESIZABLE)
pygame.display.set_caption("DDA")

done = False
points = []
count = 1

def Round(x):
    if x >= 0:
        return round(x + 0.1)
    else:
        return round(x - 0.1)

#digital differential analyzer
def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):
        stepSize = abs(dx)
        xinc = 1
        yinc = dy/stepSize
    else:
        stepSize = abs(dy)
        xinc = abs(dx/stepSize)
        yinc = 1 if y1 < y2 else -1
        
    pygame.gfxdraw.pixel(screen, x1, y1, black)
    points.append((x1,y1))

    for i in range(stepSize):
        x1 = x1 + xinc
        y1 = y1 + yinc
        pygame.gfxdraw.pixel(screen, Round(x1), Round(y1), black)
        points.append((Round(x1),Round(y1)))
    

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
     
    screen.fill(white)

    DDA(x1, y1, x2, y2)
    
    while count > 0:
        for point in points:
            print(point)
        count -= 1

    pygame.display.flip()
    
pygame.quit()