# Example file showing a basic pygame "game loop"
import pygame
import setup
import ui

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
running = True
frametime = 0

#game setup
listofbuttons = setup.setup_buttons()

testing_textbox = ui.Textbox("Somebody died, let's party", (0,0,0), (255,0,0))
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
    buttongroup.update(frametime)
    buttongroup.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    frametime = clock.tick(60)  # limits FPS to 60

pygame.quit()