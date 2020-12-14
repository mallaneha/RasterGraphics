import pygame
import pygame.gfxdraw
import numpy as np
from math import sin, cos, pi

 
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

# height and width of the screen
width = 900
height = 900
screen = pygame.display.set_mode([width, height], pygame.RESIZABLE)
pygame.display.set_caption("2D Transformation")

# A 2D shape to be transformed
rectangle = np.array([[400, 550, 550, 400], [300, 300, 400, 400], [1, 1, 1, 1]])


# Function to draw the shape from homogeneous coordinates
def Draw(homogeneousCoordinates, colour):
    coordinates = homogeneousCoordinates.transpose()
    pygame.gfxdraw.polygon(screen, coordinates[0:4, 0:2], colour)


# Function to translate the points
def Translate(tx, ty):
    translationMatrix = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])
    Draw(np.dot(translationMatrix, rectangle), green)


# Function to rotate the points
def Rotate(angle):
    rotationMatrix = np.array([[cos(angle), -sin(angle), 0], [sin(angle), cos(angle), 0], [0, 0, 1]])
    Draw(np.dot(rotationMatrix, rectangle), red)


# Function to scale the points
def Scale(sx, sy):
    scalingMatrix = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
    Draw(np.dot(scalingMatrix, rectangle), blue)


# Function to reflect the points
def Reflect():
    reflectionMatrix = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    pygame.gfxdraw.line(screen, 0, 0, 900, 900, cyan)
    Draw(np.dot(reflectionMatrix, rectangle), cyan)


# Function to shear the points in x axis 
def ShearX(shx):
    XshearingMatrix = np.array([[1, shx, 0], [0, 1, 0], [0, 0, 1]])
    Draw(np.dot(XshearingMatrix, rectangle), magenta)


# Function to shear the points in y axis
def ShearY(shy):
    YshearingMatrix = np.array([[1, 0, 0], [shy, 1, 0], [0, 0, 1]])
    Draw(np.dot(YshearingMatrix, rectangle), magenta)


done = False

while not done:
    # If user clicks close
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
     
    # The screen background as black
    screen.fill(black)

    # Triangle at original position (coloured white)
    Draw(rectangle, white)

    # Translate by 200, 200 (coloured green)
    Translate(200, 200)
    
    # Rotate by 45 degree (coloured red)
    Rotate(pi/4)

    # Scale to half (coloured blue)
    Scale(0.5, 0.5)

    # Reflect on y = x line (coloured cyan)
    Reflect()

    # Shear on both axis (coloured magenta)
    ShearX(0.75)
    ShearY(0.75)
    
    # Update the contents of the entire display
    pygame.display.flip()
    
pygame.quit()