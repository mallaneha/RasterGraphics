import pygame

pygame.init()

screen = pygame.display.set_mode([0,0])
w, h = pygame.display.get_surface().get_size()
print("Resolution: ", w, "X", h)