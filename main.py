import pygame


class Board:
    def __init__(self, left, top, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.left = left
        self.top = top
        self.Surface = pygame.Surface((self.width * self.cell_size, self.height * self.cell_size))

    def render(self):
        self.Surface.fill(GREEN)
        for i in range(self.height):
            for j in range(self.width):
                left = j * self.cell_size
                top = i * self.cell_size
                pygame.draw.rect(self.Surface, BLACK, (left, top, self.cell_size, self.cell_size), 1)


class Player:
    def __init__(self, Board):
        self.Board = Board
        self.cell_size = Board.cell_size
        self.rect = pygame.Rect((0, 0), (self.cell_size, self.cell_size))
        self.Surface = pygame.Surface((self.cell_size, self.cell_size))

    def render(self):
        self.Board.Surface.blit(self.Surface, self.rect)
        self.Surface.fill(RED)

    def move(self):
        if event.key == pygame.K_w:
            self.rect.move_ip(0, -self.cell_size)
        elif event.key == pygame.K_s:
            self.rect.move_ip(0, self.cell_size)
        elif event.key == pygame.K_a:
            self.rect.move_ip(-self.cell_size, 0)
        elif event.key == pygame.K_d:
            self.rect.move_ip(self.cell_size, 0)


pygame.init()
sc_size = width, height = 1024, 640
clock = pygame.time.Clock()
fps = 60
BLACK, WHITE, RED, GREEN, BLUE = (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)
sc = pygame.display.set_mode(sc_size)
board = Board(171, 12, 31, 28, 22)
player = Player(board)
running = True
while running:
    sc.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            player.move()

    board.render()
    player.render()
    sc.blit(board.Surface, (board.left, board.top))
    pygame.display.flip()
pygame.quit()
