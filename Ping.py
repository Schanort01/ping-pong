#Подключить библиотеки
from random import randint
from pygame import *
#pygame.init()
window = display.set_mode((700, 500))
display.set_caption("Ping-Pong")
#Работа с ФПС
clock = time.Clock()
FPS = 40
clock.tick(FPS)

#Создание заготовок спрайтов
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_w, player_h, player_speed, player_speed2 = 0):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.speed = player_speed
        self.speed2 = player_speed2
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit( self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < 630:
            self.rect.y += self.speed
    def update_2(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < 630:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed2
        if self.rect.y < 0:
            self.speed2 *= -1
        if self.rect.y > 450:
            self.speed2 *= -1
        

ball = Ball("ball.png", 100, 50, 50, 50, 5, 5)
rock_1 = Player("Raketka.png", 20, 50, 50, 150, 10)
rock_2 = Player("Raketka.png", 630, 400, 50, 150, 10)
#Спрайты победы и проигрыша
font.init()
font1 = font.Font(None, 36)
lost = 0
fin1 = font1.render("Player 1 LOSE!", 1, (0, 255, 0))
fin2 = font1.render("Player 2 LOSE!", 1, (0, 255, 0))
pl_1 = font1.render("Player 1", 1, (0, 255, 0))
pl_2 = font1.render("Player 2", 1, (0, 255, 0))
kubok_1 = GameSprite("kubok.png", 550, 300, 50, 50, 0)
kubok_2 = GameSprite("kubok.png", 10, 300, 50, 50, 0)
#Игровой цикл(Финиш, счет, работа со спрайтами, столконовения со спрайтами, рестарт, перезарядка оружия)
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.fill((200, 200, 255))
    rock_1.reset()
    rock_1.update_1()
    window.blit(pl_1, (10, 10))
    window.blit(pl_2, (600, 10))
    rock_2.reset()
    rock_2.update_2()
    ball.reset()
    ball.update()
    if  ball.rect.x < 0:
        finish = True
        window.blit(fin1, (260, 250))
        kubok_1.reset()
    if  ball.rect.x > 650:
        finish = True
        window.blit(fin2, (260, 250))
        kubok_2.reset()
    if sprite.collide_rect(ball, rock_1) or sprite.collide_rect(ball, rock_2):
        ball.speed *= -1
    display.update()
    clock.tick(FPS)

