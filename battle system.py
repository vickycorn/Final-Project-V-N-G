import random
import classes
import pygame
import ui

c1 = classes.Char("a",10,1,1,1,1)
c2 = classes.Char("b",10,1,1,1,1)
c3 = classes.Char("c",10,1,1,1,1)
c4 = classes.Char("d",10,1,1,1,1)
listofchars1 = [c1, c2, c3, c4]

e1 = classes.Char("a",10,1,1,1,1)
e2 = classes.Char("b",10,1,1,1,1)
e3 = classes.Char("c",10,1,1,1,1)
e4 = classes.Char("d",10,1,1,1,1)
listofchars2 = [e1, e2, e3, e1]
#loop over list of caricters and see when they will go
def decide_turn_order(characters: list[classes.Char]):
    speed_list =[]
    for i in characters:
        speed_list.append(i.speed)
        speed_list.sort(reverse=True)
        print (speed_list)
#interface with viky s mnues to get a choice
def get_character_choice(character: classes.Char):
    pass
#run charicter funckshon for turn
def exeute_turn(character):
    pass
#ses wha hapend
def turn_sumery(somthing):
    pass
#list of character instances on 1 side
#loop over character instnces
    #for every character check what they choose
    #work with vicky to use ui system and get choice