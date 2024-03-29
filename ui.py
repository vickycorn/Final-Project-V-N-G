import pygame
import battlechoice

#set variables for text, color, width, height
class Button(pygame.sprite.Sprite):
    def __init__(self, text, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.color = color
        self.width = width
        self.height = height

#set booleans for clicked, visible, and target
        self.clicked = False
        self.visible = True
        self.target = False

#ensures that the textboxs get filled with a chosen color
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()

#Makes buttons print the action the player has chosen to take when clicked
    def update(self, frametime):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos): 
            if pygame.mouse.get_pressed()[0]:
                print(f'This player has chosen to {self.text}')
                self.clicked = True
                #different behavior for each button
                if self.text == "Attack":
                    print("Attack!")
                    battlechoice.choice = "attack"
                if self.text == "Defend":
                    print("Defend!")
                    battlechoice.choice = "defend"
                if self.text == "Backpack":
                    print("Open backpack")
                    battlechoice.choice = "backpack"
                if self.text == "Magic":
                    print("OoOooOoo magic")
                    battlechoice.choice = "magic"
            else:
                self.clicked = False


#sets 
    def set_text(self):
        font = pygame.font.Font(pygame.font.get_default_font())
        textimage = font.render(self.text, True, (255,255,255))
        textrect = textimage.get_rect()
        remainder = (self.width - textrect.width)/2
        textrect.x += remainder
        remainder = (self.height - textrect.height)/2
        textrect.y += remainder
        self.image.blit(textimage, textrect)


class Textbox(pygame.sprite.Sprite):
    def __init__(self, text, color, background_color, size, font_size, position, time = 0, target = None, centered = True):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.color = color
        self.background_color = background_color
        self.size = size
        self.font_size = font_size
        self.image = pygame.Surface(size)
        self.image.set_colorkey((123, 92, 0))
        self.rect = self.image.get_rect()
        self.rect.y = position[1]
        self.image.fill(background_color)
        self.time = time
        self.centered = centered

        if time == 0:
            self.countdown = False
        else:
            self.countdown = True

        self.clock = 0
        self.set_text()

        if target:
            self.target = target
        else:
            self.target = None

    def set_text(self):
        self.image.fill(self.background_color)
        font = pygame.font.Font(pygame.font.get_default_font(), self.font_size)
        textimage = font.render(self.text, True, self.color)
        textrect = textimage.get_rect()

        if self.centered:

            remainder = (self.rect.width - textrect.width)/2
            textrect.x += remainder
            remainder = (self.rect.height - textrect.height)/2
            textrect.y += remainder
        self.image.blit(textimage, textrect)

        self.image.blit(textimage, textrect)

    def update(self, frametime):
        self.clock += frametime
        if self.target:
            self.rect.x = self.target.rect.x
            self.rect.y = self.target.rect.y


        if self.clock >= self.time and self.countdown == True:
            self.kill()
        