import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                left = self.left + (j * self.cell_size)
                top = self.top + (i * self.cell_size)
                pygame.draw.rect(screen, (0, 0, 0), (left, top, self.cell_size, self.cell_size), 1)


pygame.init()
size = width, height = 1024, 640
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill((255, 255, 255))
        board = Board(28, 31)
        board.set_view(232, 10, 20)
        board.render()
    pygame.display.flip()
pygame.quit()
