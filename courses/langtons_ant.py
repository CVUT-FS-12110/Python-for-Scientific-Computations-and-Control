import pygame

class Ant():

    def __init__(self, origin):
        self.loc = origin
        self.heading = 3

    def move_ant(self, board):
        if board[self.loc]:
            self.heading = (self.heading - 1) % 4
            board[self.loc] = False
        else:
            self.heading = (self.heading + 1) % 4
            board[self.loc] = True

        moves = [
            (0, -1), # up
            (1, 0), # right
            (0, 1), # down
            (-1, 0), # left
        ]

        self.loc = (self.loc[0] + moves[self.heading][0], self.loc[1] + moves[self.heading][1])

        return board

    def draw(self):
        offset_x = self.loc[0] * step
        offset_y = self.loc[1] * step
        pygame.draw.circle(screen, ANT_COLOR1, (offset_x + side // 2, offset_y + side // 2), side // 2)
        if self.heading == 0:
            hx, hy = (0.5, 0.25)
        elif self.heading == 1:
            hx, hy = (0.75, 0.5)
        elif self.heading == 2:
            hx, hy = (0.5, 0.75)
        elif self.heading == 3:
            hx, hy = (0.25, 0.5)

        pygame.draw.circle(screen, ANT_COLOR2, (offset_x + int(side * hx), offset_y + int(side * hy)), side // 4)





N = 50
SIZE = 500
LIGHT = (180, 180, 180)
DARK = (20, 20, 20)
BORDER_COLOR = (0, 50, 0)
ANT_COLOR1 = (0, 0, 250)
ANT_COLOR2 = (255, 100, 100)
FPS = 3




pygame.init()
clock = pygame.time.Clock()

# false is light, true is dark
board = {(x, y) : False for x in range(N) for y in range(N)}


screen = pygame.display.set_mode([SIZE, SIZE])
step = SIZE / N
side = int(round(step))

origin = (N // 2, N // 2)
ant = Ant(origin)


running = True
while running:

    screen.fill(LIGHT)

    board = ant.move_ant(board)

    for key, value in board.items():
        if value:
            x = int(step * key[0])
            y = int(step * key[1])
            pygame.draw.rect(screen, DARK, (x, y, side, side))

    for n_int in range(0, N + 1):
        n = int(round(n_int * step))
        pygame.draw.line(screen, BORDER_COLOR, (n, 0), (n, SIZE), width=1)
        pygame.draw.line(screen, BORDER_COLOR, (0, n), (SIZE, n), width=1)

    ant.draw()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS)

pygame.quit()