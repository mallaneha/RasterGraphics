import pygame
import pygame.gfxdraw
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)

x1, y1 = map(int,input("first point: ").split())
x2, y2 = map(int,input("second point: ").split())

width = 400
height = 400
screen = pygame.display.set_mode([width, height], pygame.RESIZABLE)
pygame.display.set_caption("BLA")

done = False
points = []
count = 1

def BLA(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1

    if dx == 0:
        m = 0
    else:
        m = dy / dx

    if m < 1:
        pk = 2 * dy - dx
        pygame.gfxdraw.pixel(screen, x1, y1, black)
        points.append((pk, x, y))

        for i in range(dx):
            if pk < 0:
                x += 1 if x2 > x1 else -1
                y = y
                pk = pk + 2 * dy
            else:
                x += 1 if x2 > x1 else -1
                y += 1 if y2 > y1 else -1
                pk = pk + 2 * (dy - dx)

            pygame.gfxdraw.pixel(screen, x, y, black)
            points.append((pk, x, y))
    elif m >= 1:
        pk = 2 * dx - dy
        pygame.gfxdraw.pixel(screen, x1, y1, black)
        points.append((pk, x, y))

        for i in range(dy):
            if pk < 0:
                x = x
                y += 1 if y2 > y1 else -1
                pk = pk + 2 * dx
            else:
                x += 1 if x2 > x1 else -1
                y += 1 if y2 > y1 else -1
                pk = pk + 2 * (dx - dy)

            pygame.gfxdraw.pixel(screen, x, y, black)
            points.append((pk, x, y))

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
     
    screen.fill(white)

    BLA(x1, y1, x2, y2)

    while count > 0:
        for point in points:
            print(point)
        count -= 1

    pygame.display.flip()
    
pygame.quit()