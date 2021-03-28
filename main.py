import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed):
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

#точка спавна игрока
start_x = 600
start_y = 500

#импорт изображения
bg = pygame.transform.scale(pygame.image.load("images/bg.png"), (width,heigth))
player_img = pygame.transform.scale(pygame.image.load("images/sf.png"), (128,128))
wall = pygame.transform.scale(pygame.image.load("images/wall.png"), (50,50))

#создание групп обьектов
all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()


#создание обьектов
player = Object(player_img, start_x, start_y, 3)
all_sprites.add(player)

#создание обьектов
wall1 = Object(wall, 0, 150, 0)
walls.add(wall1)
all_sprites.add(wall1)
wall2 = Object(wall, 0, 200, 0)
walls.add(wall2)
all_sprites.add(wall2)
wall3 = Object(wall, 0, 250, 0)
walls.add(wall3)
all_sprites.add(wall3)
wall3 = Object(wall, 0, 300, 0)
walls.add(wall3)
all_sprites.add(wall3)
wall3 = Object(wall, 0, 350, 0)
walls.add(wall3)
all_sprites.add(wall3)
wall4 = Object(wall, 0, 400, 0)
walls.add(wall4)
all_sprites.add(wall4)
wall5 = Object(wall, 0, 100, 0)
walls.add(wall5)
all_sprites.add(wall5)
wall5 = Object(wall, 0, 20, 0)
walls.add(wall5)
all_sprites.add(wall5)
wall6 = Object(wall, 0, 450, 0)
walls.add(wall6)
all_sprites.add(wall6)
wall7 = Object(wall, 0, 0, 0)
walls.add(wall7)
all_sprites.add(wall7)
wall8 = Object(wall, 0, 50, 0)
walls.add(wall8)
all_sprites.add(wall8)
wall9 = Object(wall, 0, 500, 0)
walls.add(wall9)
all_sprites.add(wall9)
wall10 = Object(wall, 0, 550, 0)
walls.add(wall10)
all_sprites.add(wall10)
wall11 = Object(wall, 0, 600, 0)
walls.add(wall11)
all_sprites.add(wall11)
wall12 = Object(wall, 0, 650, 0)
walls.add(wall12)
all_sprites.add(wall12)
wall13 = Object(wall, 100, 0, 0)
walls.add(wall13)
all_sprites.add(wall13)
wall14 = Object(wall, 150, 0, 0)
walls.add(wall14)
all_sprites.add(wall14)
wall15 = Object(wall, 200, 0, 0)
walls.add(wall15)
all_sprites.add(wall15)
wall16 = Object(wall, 250, 0, 0)
walls.add(wall16)
all_sprites.add(wall16)
wall17 = Object(wall, 50, 0, 0)
walls.add(wall17)
all_sprites.add(wall17)
wall18 = Object(wall, 300, 0, 0)
walls.add(wall18)
all_sprites.add(wall18)
wall19 = Object(wall, 350, 0, 0)
walls.add(wall19)
all_sprites.add(wall19)
wall20 = Object(wall, 400, 0, 0)
walls.add(wall20)
all_sprites.add(wall20)
wall21 = Object(wall, 450, 0, 0)
walls.add(wall21)
all_sprites.add(wall21)
wall22 = Object(wall, 500, 0, 0)
walls.add(wall22)
all_sprites.add(wall22)
wall23 = Object(wall, 550, 0, 0)
walls.add(wall23)
all_sprites.add(wall23)
wall24 = Object(wall, 600, 0, 0)
walls.add(wall24)
all_sprites.add(wall24)
wall25 = Object(wall, 650, 0, 0)
walls.add(wall25)
all_sprites.add(wall25)
wall26 = Object(wall, 700, 0, 0)
walls.add(wall26)
all_sprites.add(wall26)
wall27 = Object(wall, 750, 0, 0)
walls.add(wall27)
all_sprites.add(wall27)
wall28 = Object(wall, 750, 50, 0)
walls.add(wall28)
all_sprites.add(wall28)
wall29 = Object(wall, 750, 100, 0)
walls.add(wall29)
all_sprites.add(wall29)
wall30 = Object(wall, 750, 150, 0)
walls.add(wall30)
all_sprites.add(wall30)
wall31 = Object(wall, 750, 200, 0)
walls.add(wall31)
all_sprites.add(wall31)
wall32 = Object(wall, 750, 250, 0)
walls.add(wall32)
all_sprites.add(wall32)
wall33 = Object(wall, 750, 300, 0)
walls.add(wall33)
all_sprites.add(wall33)
wall34 = Object(wall, 750, 350, 0)
walls.add(wall34)
all_sprites.add(wall34)
wall35 = Object(wall, 750, 400, 0)
walls.add(wall35)
all_sprites.add(wall35)
wall36 = Object(wall, 750, 450, 0)
walls.add(wall36)
all_sprites.add(wall36)
wall37 = Object(wall, 750, 500, 0)
walls.add(wall37)
all_sprites.add(wall37)
wall38 = Object(wall, 750, 550, 0)
walls.add(wall38)
all_sprites.add(wall38)
wall39 = Object(wall, 750, 600, 0)
walls.add(wall39)
all_sprites.add(wall39)
wall40 = Object(wall, 750, 650, 0)
walls.add(wall40)
all_sprites.add(wall40)
wall41 = Object(wall, 700, 550, 0)
walls.add(wall41)
all_sprites.add(wall41)
wall42 = Object(wall, 650, 550, 0)
walls.add(wall42)
all_sprites.add(wall42)
wall43 = Object(wall, 600, 550, 0)
walls.add(wall43)
all_sprites.add(wall43)
wall44 = Object(wall, 550, 550, 0)
walls.add(wall44)
all_sprites.add(wall44)
wall45 = Object(wall, 500, 550, 0)
walls.add(wall45)
all_sprites.add(wall45)
wall46 = Object(wall, 450, 550, 0)
walls.add(wall46)
all_sprites.add(wall46)
wall47 = Object(wall, 400, 550, 0)
walls.add(wall47)
all_sprites.add(wall47)
wall48 = Object(wall, 350, 550, 0)
walls.add(wall48)
all_sprites.add(wall48)
wall49 = Object(wall, 300, 550, 0)
walls.add(wall49)
all_sprites.add(wall49)
wall50 = Object(wall, 250, 550, 0)
walls.add(wall50)
all_sprites.add(wall50)
wall51 = Object(wall, 200, 550, 0)
walls.add(wall51)
all_sprites.add(wall51)
wall52 = Object(wall, 150, 550, 0)
walls.add(wall52)
all_sprites.add(wall52)
wall53 = Object(wall, 100, 550, 0)
walls.add(wall53)
all_sprites.add(wall53)
wall54 = Object(wall, 50, 550, 0)
walls.add(wall54)
all_sprites.add(wall54)


















run = True
while run:
    window.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()    
    if event.type == pygame.KEYDOWN:
        if keys[pygame.K_w]:
            player.rect.y -= player.speed
        if keys[pygame.K_s]:
            player.rect.y += player.speed
        if keys[pygame.K_a]:
            player.image = pygame.transform.flip(player_img, True, False)
            player.rect.x -= player.speed
        if keys[pygame.K_d]:
            player.image = pygame.transform.flip(player_img, False, False)
            player.rect.x += player.speed
    
    all_sprites.draw(window) 
    all_sprites.update()
    pygame.display.update()