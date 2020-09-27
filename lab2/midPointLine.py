import pygame
import pygame.gfxdraw
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)

x1, y1 = map(int,input("first point: ").split())
x2, y2 = map(int,input("second point: ").split())

screen = pygame.display.set_mode([400, 400], pygame.RESIZABLE)
pygame.display.set_caption("Mid Point Line Algorithm")

done = False
points = []
count = 1

def MID(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    pk = 2 * dy - dx

    east = 2 * dy
    northeast = 2 * (dy - dx)

    pygame.gfxdraw.pixel(screen, x1, y1, black)
    x, y = x1, y1
    points.append((x, y))

    if dx > dy:
        step = dx
    else:
        step = dy

    # while x < x2 and y < y2:
    for i in range(step):
        if pk < 0:
            x += 1 if x2 > x1 else -1
            y = y
            pk = pk + east

        else:
            x += 1 if x2 > x1 else -1
            y += 1 if y2 > y1 else -1
            pk = pk + northeast

        pygame.gfxdraw.pixel(screen, x, y, black)
        points.append((x, y))

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
     
    screen.fill(white)

    MID(x1, y1, x2, y2)

    while count > 0:
        for point in points:
            print(point)
        count -= 1

    pygame.display.flip()
    
pygame.quit()