# Example file showing a basic pygame "game loop"
import pygame
import setup
import ui
import classes
import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
running = True
frametime = 0
framecount = 0

#game setup
listofbuttons = setup.setup_buttons()

testing_textbox = ui.Textbox("Somebody died, let's party!", (0,0,0), (123, 92, 0), (600,35), (12), (0, 210),time = 5000)
testing_character = classes.Char("bam", 10, 10, 10, 10, 10)
testing_character.rect.x = 30
testing_character.rect.y = 30
testingcharacterbox = ui.Textbox("Bam", (255, 0, 0), (123, 92, 0), (600, 16), 12, (0, 0), time = 0, target = testing_character, centered = False)
buttongroup = pygame.sprite.Group(listofbuttons)
buttongroup.add(testing_textbox)

charactergroup = pygame.sprite.Group((testing_character, testingcharacterbox))

while running:
    framecount += 1
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")
#TEMPORARY CHARACTER MOVEMENT DELETE LATER
    testing_character.rect.y = 30 + math.sin(framecount/20)*15
    testingcharacterbox.text = "bam" + str(30 + math.sin(framecount/20)*15)
    testingcharacterbox.set_text()

    # RENDER YOUR GAME HERE
    buttongroup.update(frametime)
    buttongroup.draw(screen)
    charactergroup.update(frametime)
    charactergroup.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    frametime = clock.tick(60)  # limits FPS to 60

pygame.quit()