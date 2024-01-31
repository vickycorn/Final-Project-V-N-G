# Example file showing a basic pygame "game loop"
import pygame
import setup
import ui
import classes
import math
import battlesystem

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
running = True
frametime = 0
framecount = 0

battlephase = 0 # 0 turn1 1 turn2
turncount = 0


#game setup
listofbuttons = setup.setup_buttons()
side1, side2 = setup.setup_chars()

testing_textbox = ui.Textbox("If you're reading this you're weird please go away :)", (0,0,0), (123, 92, 0), (600,35), (12), (0, 210), time = 5000)
# testing_character = classes.Char("Bam", 10, 10, 10, 10, 10)
# testing_character.rect.x = 30
# testing_character.rect.y = 30
# testingcharacterbox = ui.Textbox("Bam", (255, 0, 0), (123, 92, 0), (600, 16), 12, (0, 0), time = 0, target = testing_character, centered = False)

buttongroup = pygame.sprite.Group(listofbuttons)
buttongroup.add(testing_textbox)

char2 = classes.Char("bam", 10, 10, 10, 10, 10)
char2.rect.x = 50
char2.rect.y = 70 

charactergroup = pygame.sprite.Group((testing_character, testingcharacterbox, char2))
background = pygame.image.load ("images/backgrond.jpg")
#fix size and rotation
background = pygame.transform.rotate(background, 90)
background = pygame.transform.scale(background, (600,300))

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
    # testing_character.rect.y = 30 + math.sin(framecount/20)*15
    # testingcharacterbox.text = "bam" + str(30 + math.sin(framecount/20)*15)
    # testingcharacterbox.set_text()

    # RENDER YOUR GAME HERE
    buttongroup.update(frametime)
    buttongroup.draw(screen)
    charactergroup.update(frametime)
    charactergroup.draw(screen)

    #game logicsss
    # battlesystem.decide_turn_order()


    # flip() the display to put your work on screen
    pygame.display.flip()

    frametime = clock.tick(60)  # limits FPS to 60

pygame.quit()