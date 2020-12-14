import pygame
import pygame.gfxdraw

 
# Initializing the game engine
pygame.init()
 
# Colors in RGB format
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
yellow = (255, 255, 0)
orange = (253, 106, 2)

colours = [white, red, magenta, green, cyan, blue, orange, yellow]

# height and width of the screen
length = 1000
screen = pygame.display.set_mode([length, length], pygame.RESIZABLE)
pygame.display.set_caption("2D Hilbert Curve")

points = []


# Function to find the points of the curve
def Hilbert(x0, y0, xi, xj, yi, yj, n):
    """ x and y are the coordinates of the bottom left corner
        xi & xj are the i & j components of the unit x vector of the frame
        similarly yi and yj """

    if n <= 0:
        X = x0 + (xi + yi)/2
        Y = y0 + (xj + yj)/2
        points.append((int(X), int(Y)))
    else:
        Hilbert(x0,               y0,               yi/2, yj/2, xi/2, xj/2, n - 1)
        Hilbert(x0 + xi/2,        y0 + xj/2,        xi/2, xj/2, yi/2, yj/2, n - 1)
        Hilbert(x0 + xi/2 + yi/2, y0 + xj/2 + yj/2, xi/2, xj/2, yi/2, yj/2, n - 1)
        Hilbert(x0 + xi/2 + yi,   y0 + xj/2 + yj,  -yi/2,-yj/2,-xi/2,-xj/2, n - 1)
    

# Function to connect the points of the curve
def draw(colour): 
    for i in range(len(points) - 1):
        pygame.gfxdraw.line(screen, points[i][0], points[i][1], points[i+1][0], points[i+1][1], colour)
    points.clear()


done = False

while not done:
    # If user clicks close
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
     
    # The screen background as black
    screen.fill(black)

    # Drawing all the Hilbert curve from order 1 to 9
    for i in range(1, 10):
        Hilbert(0.0, 0.0, length, 0.0, 0.0, length, i)
        draw(colours[i%len(colours)])

    # Drawing Hilbert curve of specific order
    # Hilbert(0.0, 0.0, length, 0.0, 0.0, length, 10)
    # draw(colours[-1])
    
    # Update the contents of the entire display
    pygame.display.flip()
    
pygame.quit()
