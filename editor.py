'''
window.blit(параметры) - отобразить на окне
key.get_pressed() - получить список нажатых кнопок
display.set_mode - создать экран
window.fill(цвет) - закрасить экран цветом
time.Clock() - игровые часы
font.Font(параметры) - создать шрифт
font.render - создать надпись
event.get() - получить список событий
событие.type() - тип события
sprite.collide_rect(объект 1,объект 2) - проверка столкновения
'''


from pygame import *
#создать класс class GameSprite(sprite.Sprite):
    #конструктор (self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) 
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    #функция reset(self):
        #отобразить на окне (self.image, (self.rect.x, self.rect.y))


#Создать класс Player(GameSprite):
    #функция update_r(self):
        #keys = список нажатых кнопок
        #если keys[K_UP] И self.rect.y > 5:
            #Из self.rect.y вычитаем self.speed
        #если keys[K_DOWN] И self.rect.y < win_height - 80:
            #К self.rect.y прибавить self.speed
    #функция update_l(self):
        #keys = список нажатых кнопок
        #если keys[K_w] И self.rect.y > 5:
            #из self.rect.y вычесть self.speed
        #если if keys[K_s] и self.rect.y < win_height - 80:
            #к self.rect.y прибавить self.speed


back = (200, 255, 255) 
win_width = 600
win_height = 500
#window = создать экран((win_width, win_height))
#закрасить window цветом (back)

game = True
finish = False
#clock = создать игровые часы
FPS = 60

racket1 = Player('racket.png', 30, 200, 4, 50, 150) 
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
#font = создать шрифт(None, 35)
#lose1 = создать надпись('PLAYER 1 LOSE!', True, (180, 0, 0))
#lose2 = создать надпись('PLAYER 2 LOSE!', True, (180, 0, 0))


speed_x = 3
speed_y = 3


while game:
    #пробежаться по списку событий:
        #если тип события равен QUIT:
            game = False
  
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y


        #сли if столкнулись (racket1, ball) ИЛИ столкнулись(racket2, ball):
            #speed_x умножить на -1
            #speed_y умножить на  1
        #если ball.rect.y > win_height-50 or ball.rect.y < 0:
            #speed_y умножить на -1

        #если ball.rect.x < 0:
            #finish присвоить значение True
            #отобразить на окне (lose1, (200, 200))
            #game_over присвоить значение True
        #если ball.rect.x > win_width:
            #finish присвоить значение True
            #отобразить на окне (lose2, (200, 200))
            #game_over присвоить значение True
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
