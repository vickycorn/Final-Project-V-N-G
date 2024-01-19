import pygame
class Button(pygame.sprite.Sprite):
    def __init__(self, text, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.color = color
        self.width = width
        self.height = height
        self.clicked = False
        self.visible = True
        self.target = False

        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos): 
            #ADD A COLOUR HERE LATER DON"T FORGET!!!
            #self.image.fill()
            if pygame.mouse.get_pressed()[0]:
                #print(f'This player has chosen to {self.text}')
                self.clicked = True
            else:
                self.clicked = False


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
    def __init__(self, text, color, background_color, size, font_size):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.color = color
        self.background_color = background_color
        self.size = size
        self.font_size = font_size
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.image.fill(background_color)
        
    def set_text(self):
        font = pygame.font.Font(pygame.font.get_default_font())
        font.size = self.font_size
        textimage = font.render(self.text, True, self.color)
        textrect = textimage.get_rect()
        self.image.blit(textimage, textrect)