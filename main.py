import pygame

class Object(pygame.sprite.Sprite):
    def __inint__(self, img, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

width = 800
heigth = 600

window = pygame.display.set_mode((800,600))
pygame.display.set_caption("DOTA 3")

bg = pygame.transform.scale(pygame.image.load("images/bg.png"), (width,heigth))

run = True
while run:
    window.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        
    pygame.display.update()