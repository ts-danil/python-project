import pygame
import random


class Menu(pygame.sprite.Sprite):
    def __init__(self, num, name):
        super().__init__(menu_sprites)
        self.num = num
        self.name = name
        self.width = sc_width / 2
        self.height = sc_height / 8
        self.left = sc_width / 4
        self.top = sc_height / 8 * num + 10 * num + 200
        self.rect = pygame.Rect((self.left, self.top), (self.width, self.height))
        self.image = pygame.Surface((self.width, self.height))
        self.print = menu_font.render(name, 5, BLACK)

    def render(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image.fill(GREEN)
        else:
            self.image.fill(BLUE)
        self.image.blit(self.print, (self.width / 4, self.height / 8))


class Status_bar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(menu_sprites)
        self.width = 6 * (sc_width / 8)
        self.height = 3 * (sc_height / 8)
        self.left = sc_width / 8
        self.top = 22
        self.rect = pygame.Rect((self.left, self.top), (self.width, self.height))
        self.image = pygame.Surface((self.width, self.height))
        self.color = WHITE

    def render(self, text1, text2, color1, color2):
        self.image.fill(self.color)
        if self.color == color1:
            self.color = color2
        else:
            self.color = color1
        self.print1 = sb_font.render(text1, 5, self.color)
        self.print2 = sb_font.render(text2, 5, self.color)
        self.image.blit(self.print1, (self.width / 4, self.height / 8))
        self.image.blit(self.print2, (self.width / 4, self.height / 8 + 50))


class Board(pygame.sprite.Sprite):
    def __init__(self, width, height, cell_size):
        super().__init__(game_sprites)
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.left = (sc_width - (width * cell_size)) / 2
        self.top = (sc_height - (height * cell_size)) / 2
        self.rect = pygame.Rect((self.left, self.top), (self.width * self.cell_size, self.height * self.cell_size))
        self.image = pygame.Surface((self.width * self.cell_size, self.height * self.cell_size))

    def render(self):
        self.image.fill(GREEN)
        for i in range(self.height):
            for j in range(self.width):
                left = j * self.cell_size
                top = i * self.cell_size
                pygame.draw.rect(self.image, BLACK, (left, top, self.cell_size, self.cell_size), 1)


class Wall(pygame.sprite.Sprite):
    def __init__(self, Board, left, top, height, width):
        super().__init__(Walls, game_sprites)
        self.cell_size = Board.cell_size
        self.height = height * self.cell_size
        self.width = width * self.cell_size
        if left == 1:
            self.left = Board.left
        else:
            self.left = Board.left + (left - 1) * self.cell_size
        if top == 1:
            self.top = Board.top
        else:
            self.top = Board.top + (top - 1) * self.cell_size
        self.rect = pygame.Rect((self.left, self.top), (self.height, self.width))
        self.image = pygame.Surface((self.height, self.width))


class Player(pygame.sprite.Sprite):
    def __init__(self, Board, x, y):
        super().__init__(game_sprites)
        self.cell_size = Board.cell_size
        self.left = Board.left + x * self.cell_size
        self.top = Board.top + y * self.cell_size
        self.way = " "
        self.rect = pygame.Rect((self.left, self.top), (self.cell_size, self.cell_size))
        self.image = pygame.Surface((self.cell_size, self.cell_size))
        self.image.fill(RED)

    def move(self, new_way):
        global try_way
        global running
        old_way = self.way
        if try_way % 2 == 1:
            self.way = new_way
            try_way = 1
        if self.way == "up":
            self.rect.move_ip(0, -11)
            if pygame.sprite.spritecollideany(self, Walls):
                self.rect.move_ip(0, 11)
                self.way = old_way
        elif self.way == "down":
            self.rect.move_ip(0, 11)
            if pygame.sprite.spritecollideany(self, Walls):
                self.rect.move_ip(0, -11)
                self.way = old_way
        elif self.way == "left":
            self.rect.move_ip(-11, 0)
            if pygame.sprite.spritecollideany(self, Walls):
                self.rect.move_ip(11, 0)
                self.way = old_way
        elif self.way == "right":
            self.rect.move_ip(11, 0)
            if pygame.sprite.spritecollideany(self, Walls):
                self.rect.move_ip(-11, 0)
                self.way = old_way
        try_way += 1


class Virus(pygame.sprite.Sprite):
    def __init__(self, Board, x, y):
        super().__init__(Viruses, game_sprites)
        self.cell_size = Board.cell_size
        self.left = Board.left + x * self.cell_size
        self.top = Board.top + y * self.cell_size
        self.rect = pygame.Rect((self.left, self.top), (self.cell_size, self.cell_size))
        self.image = pygame.Surface((self.cell_size, self.cell_size))
        self.image.fill(BLUE)
        self.way = " "

    def move(self):
        way_list = ['up', 'down', 'left', 'right']
        for wp in way_point:
            if self.rect.collidepoint(field.left + wp[0] * 22, field.top + wp[1] * 22):
                if self.way == "up":
                    way_list.remove("down")
                elif self.way == "down":
                    way_list.remove("up")
                elif self.way == "left":
                    way_list.remove("right")
                elif self.way == "right":
                    way_list.remove("left")
                self.way = random.choice(way_list)
        if self.way == "up":
            self.rect.move_ip(0, -11)
            if pygame.sprite.spritecollideany(self, Walls):
                self.rect.move_ip(0, 11)
        elif self.way == "down":
            self.rect.move_ip(0, 11)
            if pygame.sprite.spritecollideany(self, Walls):
                self.rect.move_ip(0, -11)
        elif self.way == "left":
            self.rect.move_ip(-11, 0)
            if pygame.sprite.spritecollideany(self, Walls):
                self.rect.move_ip(11, 0)
        elif self.way == "right":
            self.rect.move_ip(11, 0)
            if pygame.sprite.spritecollideany(self, Walls):
                self.rect.move_ip(-11, 0)


class Loot(pygame.sprite.Sprite):
    def __init__(self, Board, x, y):
        super().__init__(Lot_loot, game_sprites)
        self.cell_size = 4
        self.left = Board.left + x * Board.cell_size
        self.top = Board.top + y * Board.cell_size
        self.rect = pygame.Rect((self.left, self.top), (self.cell_size, self.cell_size))
        self.image = pygame.Surface((self.cell_size, self.cell_size))
        self.image.fill(WHITE)


def Score_counter():
    global lvl, lvl_score, total_score, start_game, next_lvl
    if pygame.sprite.spritecollide(player, Lot_loot, dokill=True):
        lvl_score += 1 * lvl
    score_surface.fill(RED)
    lvl_print = score_font.render('Уровень: ' + str(lvl), 5, BLACK)
    score_print = score_font.render('Счет: ' + str(total_score + lvl_score), 5, BLACK)
    score_surface.blit(lvl_print, (10, 0))
    score_surface.blit(score_print, (10, 30))
    screen.blit(score_surface, (0, 12))


def Respawn():
    global player, new_way, virus_list
    player.rect = pygame.Rect(player.left, player.top, player.cell_size, player.cell_size)
    player.way = " "
    new_way = " "
    for i in range(lvl):
        virus_list[i].rect = pygame.Rect((virus_list[i].left, virus_list[i].top),
                                         (virus_list[i].cell_size, virus_list[i].cell_size))
    for i in range(field.height):
        for j in range(field.width):
            Loot(field, j, i)
    pygame.sprite.groupcollide(Walls, Lot_loot, dokilla=False, dokillb=True)


def game_over_screen():
    global start_game, game_over
    screen.fill(WHITE)
    button1.print = menu_font.render('Вернуться в меню', 5, BLACK)
    start_game = False
    game_over = True


def lvl_up():
    global lvl, lvl_score, total_score, start_game, next_lvl
    total_score += lvl_score
    virus_list.append(Virus(field, 15, 16))
    lvl += 1
    lvl_score = 0
    button1.print = menu_font.render('Следующий уровень', 5, BLACK)
    start_game = False
    next_lvl = True


'''Шрифты'''
pygame.font.init()
menu_font = pygame.font.SysFont('Comic Sans MS', 30)
score_font = pygame.font.SysFont('Comic Sans MS', 24)
sb_font = pygame.font.SysFont('Comic Sans MS', 50)

'''Цвета'''
BLACK, WHITE, RED, GREEN, BLUE = (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)

'''Параметры окна'''
sc_size = sc_width, sc_height = 1024, 640
screen = pygame.display.set_mode(sc_size)
pygame.display.set_caption("COVIDMAN")

'''Частота обновления'''
clock = pygame.time.Clock()
fps = 60

'''Таймеры'''
sb_update_event = pygame.USEREVENT + 1
virus_update_event = pygame.USEREVENT + 2
pygame.time.set_timer(sb_update_event, 500)
pygame.time.set_timer(virus_update_event, 25)

'''Группы спрайтов'''
menu_sprites = pygame.sprite.Group()
game_sprites = pygame.sprite.Group()
Walls = pygame.sprite.Group()
Viruses = pygame.sprite.Group()
Lot_loot = pygame.sprite.Group()

'''Список стен'''
wall_list = {(6, 2, 2, 2), (6, 23, 5, 2), (1, 1, 1, 28), (9, 25, 2, 2), (6, 23, 5, 2),
             (6, 26, 2, 2), (9, 17, 2, 5), (9, 14, 5, 2), (9, 8, 2, 5), (4, 20, 4, 2),
             (3, 17, 2, 10), (6, 11, 2, 8), (3, 14, 5, 2), (27, 3, 3, 4), (24, 3, 2, 4),
             (18, 1, 5, 6), (12, 1, 5, 6), (9, 3, 2, 2), (6, 5, 5, 2), (4, 8, 4, 2),
             (3, 3, 2, 10), (6, 2, 2, 2), (1, 28, 31, 1), (31, 1, 1, 28), (1, 1, 31, 1),
             (12, 8, 5, 2), (12, 11, 2, 8), (12, 20, 5, 2), (12, 23, 5, 6), (15, 11, 1, 8),
             (16, 11, 3, 1), (16, 18, 3, 1), (18, 8, 8, 2), (19, 11, 1, 3), (19, 16, 1, 3),
             (18, 20, 8, 2), (18, 23, 5, 6), (21, 17, 2, 3), (21, 10, 2, 3), (21, 14, 3, 2),
             (24, 11, 2, 8), (24, 23, 2, 4), (27, 23, 3, 4), (27, 17, 3, 5), (27, 14, 4, 2), (27, 8, 3, 5)}

'''Точки, в которых можно поменять маршрут'''
way_point = {(1, 1), (1, 12), (1, 15), (1, 26),
             (4, 1), (4, 3), (4, 6), (4, 9), (4, 12), (4, 15), (4, 18), (4, 21), (4, 24), (4, 26),
             (7, 1), (7, 3), (7, 6), (7, 9), (7, 12), (7, 15), (7, 18), (7, 21), (7, 24), (7, 26),
             (10, 1), (10, 6), (10, 9), (10, 12), (10, 15), (10, 18), (10, 21), (10, 26),
             (13, 6), (13, 9), (13, 18), (13, 21),
             (15, 11), (15, 13), (15, 14), (15, 16),
             (16, 1), (16, 6), (16, 9), (16, 18), (16, 21), (16, 26),
             (17, 11), (17, 13), (17, 14), (17, 16),
             (19, 6), (19, 9), (19, 12), (19, 13), (19, 14), (19, 15), (19, 18), (19, 21),
             (22, 1), (22, 6), (22, 9), (22, 12), (22, 15), (22, 18), (22, 21), (22, 26),
             (25, 1), (25, 6), (25, 9), (25, 12), (25, 15), (25, 18), (25, 21), (25, 26),
             (29, 1), (29, 6), (29, 12), (29, 15), (29, 21), (29, 26)}

'''Создание объектов:'''

'''Меню'''
button1 = Menu(1, 'Новая игра')
button2 = Menu(2, 'Управление')
button3 = Menu(3, 'Выход')
sb = Status_bar()

'''Игровое поле:'''
screen.fill(WHITE)
field = Board(31, 28, 22)
field.image.fill(GREEN)
#field.image.set_alpha(150)

'''Стены:'''
for w in wall_list:
    Wall(field, w[0], w[1], w[2], w[3])

'''Игрок: '''
player = Player(field, 13, 13)
new_way = " "
try_way = 1

'''Вирусы: '''
virus_list = [Virus(field, 15, 16)]

'''Лут:'''
for i in range(field.height):
    for j in range(field.width):
        Loot(field, j, i)
pygame.sprite.groupcollide(Walls, Lot_loot, dokilla=False, dokillb=True)

'''Счетчик очков'''
score_surface = pygame.Surface((171, 70))
total_score = 0
lvl_score = 0
lvl = 1

menu = True
start_game = False
next_lvl = False
game_over = False
running = True
while running:
    if menu:
        button1.render()
        button2.render()
        button3.render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == sb_update_event:
                sb.render('COVIDMAN', '2019-2020', WHITE, BLACK)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button1.rect.collidepoint(pygame.mouse.get_pos()) and event.button == 1:
                    menu = False
                    total_score = 0
                    lvl_score = 0
                    lvl = 1
                    Respawn()
                    start_game = True
                elif button3.rect.collidepoint(pygame.mouse.get_pos()) and event.button == 1:
                    running = False
        menu_sprites.draw(screen)

    if start_game:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and lvl != 0:
                if event.key == pygame.K_w:
                    new_way = "up"
                elif event.key == pygame.K_s:
                    new_way = "down"
                elif event.key == pygame.K_a:
                    new_way = "left"
                elif event.key == pygame.K_d:
                    new_way = "right"
            elif event.type == virus_update_event:
                for i in range(lvl):
                    virus_list[i].move()
                player.move(new_way)
        Score_counter()
        if pygame.sprite.spritecollide(player, Viruses, dokill=False):
            game_over_screen()
        if lvl_score == 318 * lvl:
            lvl_up()
        game_sprites.draw(screen)

    if next_lvl:
        screen.fill(WHITE)
        button1.render()
        button3.render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == sb_update_event:
                sb.render('Уровень ' + str(lvl-1), 'пройден', WHITE, GREEN)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button1.rect.collidepoint(pygame.mouse.get_pos()) and event.button == 1:
                    Respawn()
                    next_lvl = False
                    start_game = True
                elif button3.rect.collidepoint(pygame.mouse.get_pos()) and event.button == 1:
                    running = False
        menu_sprites.draw(screen)

    if game_over:
        screen.fill(WHITE)
        button1.render()
        button2.render()
        button3.render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == sb_update_event:
                sb.render('Произошло заражение', 'Вы набрали ' + str(total_score + lvl_score) + ' очков', WHITE, RED)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button1.rect.collidepoint(pygame.mouse.get_pos()) and event.button == 1:
                    game_over = False
                    menu = True
                    button1.print = menu_font.render('Новая игра', 5, BLACK)
                elif button3.rect.collidepoint(pygame.mouse.get_pos()) and event.button == 1:
                    running = False
        menu_sprites.draw(screen)
    clock.tick(fps)
    pygame.display.flip()
pygame.quit()
