import pygame

#this is the base cllas the caricters will be bilt on
class Char(pygame.sprite.Sprite):
    def __init__(self, name, health, attack, defense, mana, speed):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.health = health
        self.origenal_helth = health
        self.attack = attack
        self.defense = defense
        self.mana = mana
        self.speed = speed
        self.alive = True
        self.block = False
        self.choice = None
        self.items = []
        self.image = pygame.Surface((100, 80))
        self.rect = self.image.get_rect()
        self.target = None 
        self.count = 0
        self.time = 4
        self.slash = False 
        self.shape = 1

        f1 = pygame.image.load("images/person/B_person_1.png")
        f2 = pygame.image.load("images/person/B_person_2.png")
        f3 = pygame.image.load("images/person/B_person_3.png")
        f4 = pygame.image.load("images/person/B_person_4.png")
        f5 = pygame.image.load("images/person/B_person_5.png")
        f6 = pygame.image.load("images/person/B_person_6.png")

        self.frams = [f1, f2, f3, f4, f5, f6]
        self.count = 0
#this is how we will deal dameg and it will skip the dameg if the charicter bloscks
    def deal_damage(self, target):
        if target.block == True:
            target.block = False
            pass
        else:
            damage = self.attack - target.defense
            if damage >= 0:
                target.health -= damage
#this is the funcshon fro magic attacks
    def magic_damage(self, target):
        if target.block == True:
            target.block = False
            pass
        else:
            damage = self.attack
            if damage >= 0:
                target.health -= damage
                
#this is the funchson for prefoming a block
    def block (self):
        self.block = True
#this is how you use items
    def use_itams(self, item):
        for i in self.items:
            if i.itype == 0:
                i.heal(self)
                self.items.remove(i)
            elif i.itype == 1:
                i.mana(self)
                self.items.remove(i)
#this is how you heal
    def heal(self):
        self.health += 30
#this is to heal
    def use_backpack(self):
        self.health += 25
#this checs for what items you have
    def check_itams(self):
        return self.items
   #makes charater move
    def animate(self, framtime):
        if self.slash:
            self.image = self.frams[int((self.count % 60/self.time) %3) + 3 + self.shape *6]
        else:
            self.image = self.frams[int((self.count % 60/self.time) %3)]
        #fix size and rotation
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (50,100))
        self.count = self.count + 1
    def update(self, framtime):
        self.animate(framtime )
    
#this is the itame class
class Item():
    #heal is how much the pochin heals and mana is how muxh mana is addid
    def __init__(self, heal, mana, itype):
        self.heal = heal
        self.mana = mana
        self.itype = itype
    #helth poshon = 0 mana poshon = 1
    #this is the heal funchon so it will add helth to the tratge
    def heal(self, target):
        target.health += self.heal
    #this is the mana funchon so it will add mana to the tratge
    def mana(self, target):
        target.mana += self.mana