import random
import classes
import pygame
import ui

#This counts if everyone is alive
def alive_counter(side1,side2):
    #If everyone is alive, the game will continue, If everyone is not, it will stop.
    side1dead=[]
    side2dead=[]
    #This is checking side one
    for char in side1:
        if char.alive == False:
            side1dead.append[char]
    #This checks side two
    for char in side2:
        if char.alive == False:
            side2dead.append[char]
    #this makes one side dead or both sides dead
    if len(side1dead) == len(side1):
        return False
    elif len(side2dead) == len(side2):
        return False
    else:
        return True
def player_choice(side1,side2,buttons):
    choices={}
    true_choice = 0
    for char in side1:
        #The player picking all the actions for their characters
        button_input = buttons.sprites()
        if button_input[0].clicked:
            char.choice = 0
            print (f"{char.name} chose to attack")
        elif button_input[1].clicked:
            char.choice = 1
            print (f"{char.name} chose to defend")
        elif button_input[2].clicked:
            char.choice = 2
            print (f"{char.name} chose to cast a bapack")
        elif button_input[3].clicked:
            char.choice = 3
            print (f"{char.name} chose to magic")
        choices[char.speed] = char