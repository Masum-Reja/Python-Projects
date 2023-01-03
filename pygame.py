import pygame

pygame.init()
screen = pygame.disply.set_mode((400,500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #draw all the elements
    pygame.display.update()
