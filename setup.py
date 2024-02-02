import pygame
import ui
import classes

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

#kidane's code
def setup_chars():
    c1 = classes.Char("a",10,1,1,1,0)
    c2 = classes.Char("b",10,1,1,1,9)
    c1.rect.move_ip((30,30))
    c2.rect.move_ip((30,80))

    listofchars1 = [c1, c2]

    e1 = classes.Char("e",10,1,1,1,1)
    e2 = classes.Char("f",10,1,1,1,1)
    e1.rect.move_ip((450,30))
    e2.rect.move_ip((450,80))

    listofchars2 = [e1, e2]

    return (listofchars1, listofchars2)

# make buttons disappear
def disappearbuttons(buttons):
    for b in buttons:
        b.visible = False

#make buttons appear
def appearbuttons(buttons):
    for b in buttons:
        b.visible = True




