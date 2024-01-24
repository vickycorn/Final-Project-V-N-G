import pygame
import ui
def setup_buttons():
    
    #setting text, color, length, height of all buttons
    attackbutton = ui.Button("Attack", (200,0,0), 300, 70)
    attackbutton.rect.y = 260
    attackbutton.set_text()
    defendbutton = ui.Button("Defend", (0,200,0), 300, 70)
    defendbutton.rect.y = 260
    defendbutton.rect.x = 300
    defendbutton.set_text()
    backpackbutton = ui.Button("Backpack", (200,200,0), 300, 70)
    backpackbutton.rect.y = 330
    backpackbutton.set_text()
    magicbutton = ui.Button("Magic", (0, 0, 200), 300, 70)
    magicbutton.rect.y = 330
    magicbutton.rect.x = 300
    magicbutton.set_text()
    listofbuttons = [attackbutton, defendbutton, backpackbutton, magicbutton]
    return listofbuttons

# make buttons disappear
def disappearbuttons(buttons):
    for b in buttons:
        b.visible = False

#make buttons appear
def appearbuttons(buttons):
    for b in buttons:
        b.visible = True




