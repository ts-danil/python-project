import pygame


class Board(pygame.sprite.Sprite):
    def __init__(self, width, height, cell_size):
        super().__init__()
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.left = (sc_width - (width * cell_size)) / 2
        self.top = (sc_height - (height * cell_size)) / 2
        self.Surface = pygame.Surface((self.width * self.cell_size, self.height * self.cell_size))

    def render(self):
        self.Surface.fill(GREEN)
        for i in range(self.height):
            for j in range(self.width):
                left = j * self.cell_size
                top = i * self.cell_size
                pygame.draw.rect(self.Surface, GREEN, (left, top, self.cell_size, self.cell_size), 1)
        if self.width == 31 and self.height == 28:
            Walls.draw(board.Surface)


class Wall(pygame.sprite.Sprite):
    def __init__(self, Board, left, top, height, width):
        super().__init__(Walls)
        self.add(Walls)
        self.cell_size = Board.cell_size
        self.height = height * self.cell_size
        self.width = width * self.cell_size
        if left == 1:
            self.left = 0
        else:
            self.left = (left - 1) * self.cell_size
        if top == 1:
            self.top = 0
        else:
            self.top = (top - 1) * self.cell_size
        self.rect = pygame.Rect((self.left, self.top), (self.height, self.width))
        self.image = pygame.Surface((self.height, self.width))


class Player(pygame.sprite.Sprite):
    def __init__(self, cell_size, x, y):
        super().__init__()
        self.cell_size = cell_size
        self.left = x * self.cell_size
        self.top = y * self.cell_size
        self.rect = pygame.Rect((self.left, self.top), (self.cell_size, self.cell_size))
        self.Surface = pygame.Surface((self.cell_size, self.cell_size))

    def render(self, Surface):
        self.Surface.fill(RED)
        Surface.blit(self.Surface, self.rect)

    def move(self, motion):
        if motion == "up":
            self.rect.move_ip(0, -self.cell_size)
            if pygame.sprite.spritecollideany(self, Walls):
                self.rect.move_ip(0, self.cell_size)
        elif motion == "down":
            self.rect.move_ip(0, self.cell_size)
            if pygame.sprite.spritecollideany(self, Walls):
                self.rect.move_ip(0, -self.cell_size)
        elif motion == "left":
            self.rect.move_ip(-self.cell_size, 0)
            if pygame.sprite.spritecollideany(self, Walls):
                self.rect.move_ip(self.cell_size, 0)
        elif motion == "right":
            self.rect.move_ip(self.cell_size, 0)
            if pygame.sprite.spritecollideany(self, Walls):
                self.rect.move_ip(-self.cell_size, 0)


sc_size = sc_width, sc_height = 1024, 640
screen = pygame.display.set_mode(sc_size)

clock = pygame.time.Clock()
fps = 24

BLACK, WHITE, RED, GREEN, BLUE = (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)
board = Board(31, 28, 22)

player = Player(board.cell_size, 13, 13)
motion = "stop"

Walls = pygame.sprite.Group()
wall_list = {(6, 2, 2, 2), (6, 23, 5, 2), (1, 1, 1, 28), (9, 25, 2, 2), (6, 23, 5, 2),
             (6, 26, 2, 2), (9, 17, 2, 5), (9, 14, 5, 2), (9, 8, 2, 5), (4, 20, 4, 2),
             (3, 17, 2, 10), (6, 11, 2, 8), (3, 14, 5, 2), (27, 3, 3, 4), (24, 3, 2, 4),
             (18, 1, 5, 6), (12, 1, 5, 6), (9, 3, 2, 2), (6, 5, 5, 2), (4, 8, 4, 2),
             (3, 3, 2, 10), (6, 2, 2, 2), (1, 28, 36, 1), (31, 1, 1, 28), (1, 1, 36, 1),
             (12, 8, 5, 2), (12, 11, 2, 8), (12, 20, 5, 2), (12, 23, 5, 6), (15, 11, 1, 8),
             (16, 11, 3, 1), (16, 18, 3, 1), (18, 8, 8, 2), (19, 11, 1, 3), (19, 16, 1, 3),
             (18, 20, 8, 2), (18, 23, 5, 6), (21, 17, 2, 3), (21, 10, 2, 3), (21, 14, 3, 2),
             (24, 11, 2, 8), (24, 23, 2, 4), (27, 23, 3, 4), (27, 17, 3, 5), (27, 14, 4, 2), (27, 8, 3, 5)}
for w in wall_list:
    Wall(board, w[0], w[1], w[2], w[3])

running = True
while running:
    screen.fill(WHITE)
    board.render()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                motion = "up"
            elif event.key == pygame.K_s:
                motion = "down"
            elif event.key == pygame.K_a:
                motion = "left"
            elif event.key == pygame.K_d:
                motion = "right"
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]:
                motion = "stop"
    player.move(motion)
    player.render(board.Surface)
    screen.blit(board.Surface, (board.left, board.top))
    clock.tick(fps)
    pygame.display.flip()
pygame.quit()
