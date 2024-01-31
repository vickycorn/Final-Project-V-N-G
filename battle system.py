import random
import classes
import pygame
import ui
import battlechoice

c1 = classes.Char("a",10,1,1,1,0)
c2 = classes.Char("b",10,1,1,1,9)
c3 = classes.Char("c",10,1,1,1,32)
c4 = classes.Char("d",10,1,1,1,16)
listofchars1 = [c1, c2, c3, c4]

e1 = classes.Char("e",10,1,1,1,1)
e2 = classes.Char("f",10,1,1,1,1)
e3 = classes.Char("g",10,1,1,1,1)
e4 = classes.Char("h",10,1,1,1,1)
listofchars2 = [e1, e2, e3, e1]
#loop over list of caricters and see when they will go
def decide_turn_order(characters: list[classes.Char]):
    charspeeddic = {}
    for i in characters:
        charspeeddic.update({i.speed:i})
        #print(charspeeddic)
    for char in characters:
        charspeeddic = dict(sorted(charspeeddic.items(), reverse=True))
        #print(charspeeddic)
        #csorted = dict(sorted(choices.items(), reverse=True))
        keys = list(charspeeddic.keys())
        #print(keys)
        keys.sort(reverse=True)
        #print(keys)
        charsortid = {i: charspeeddic[i] for i in keys}
        # print("a")
        # print(charspeeddic)
        # print("b")
        # print(charsortid)
        # print("a")
        return charsortid
    # speed_list =[]
    # character_list =[]
    # for i in characters:
    #     speed_list.append(i.speed)
    #     speed_list.sort(reverse=True)
    #     print (speed_list)
    #     for j in speed_list:
    #         for char in characters:
    #             if j == char.speed:
    #                 character_list.append(char)
    # for c in character_list:
    #     print (c.name)
#interface with viky s mnues to get a choice
def get_character_choice(character: classes.Char):
    if battlechoice.choice == "attack":
            i.deal_damage
    elif battlechoice.choice == "magic":
            i.magic_damage
    elif battlechoice.choice == "defnd":
            i.block
    elif battlechoice.choice == "backpack":
        for i in listofchars1:
            i.heal
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
print(decide_turn_order(listofchars1))