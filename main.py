# Example file showing a basic pygame "game loop"
import pygame
import setup
import ui

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
running = True

#game setup
listofbuttons = setup.setup_buttons()

buttongroup = pygame.sprite.Group(listofbuttons)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    # RENDER YOUR GAME HERE
    buttongroup.update()
    buttongroup.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()