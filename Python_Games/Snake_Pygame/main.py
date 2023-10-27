import math, random, pygame, tkinter as tk
from tkinter import messagebox

# Intialize the pygame

pygame.init()
pygame.joystick.init()

# background
backgroundImg = pygame.image.load('Python_Games/Snake_Pygame/Resources/background.png')


class Cube(object):
    rows = 20
    w = 500

    def __init__(self, start, dir_nx=1, dir_ny=0, color=(255, 50, 50)):
        self.pos = start
        self.dir_nx = 1
        self.dir_ny = 0
        self.color = color

    def move(self, dir_nx, dir_ny):
        self.dir_nx = dir_nx
        self.dir_ny = dir_ny
        self.pos = (self.pos[0] + self.dir_nx, self.pos[1] + self.dir_ny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(surface, self.color, ((i * dis), (j * dis), dis - 1, dis - 1))
        # pygame.draw.rect(surface, self.color, ((i * dis + 1), (j * dis + 1), dis - 2, dis - 2))
        if eyes:
            center = dis // 2
            radius = 3
            circle_middle = ((i * dis) + center - radius, (j * dis) + 8)
            circle_middle2 = ((i * dis) + dis - (radius * 2), (j * dis) + 8)
            head = ((i * dis) + center - radius + 3, (j * dis) + 13)
            pygame.draw.circle(surface, self.color, head, 17)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle2, radius)


class Snake(object):
    body = []  # no of block of snake
    turns = {}  # where the snake turns, because we have can have multiple snake block

    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        # move one direction at a time
        self.dir_nx = 0
        self.dir_ny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # exit the game red cross
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT] and self.dir_nx != 1:
                    self.dir_nx = -1
                    self.dir_ny = 0
                    self.turns[self.head.pos[:]] = [self.dir_nx, self.dir_ny]  # to remember where we turn
                elif keys[pygame.K_RIGHT] and self.dir_nx != -1:
                    self.dir_nx = 1
                    self.dir_ny = 0
                    self.turns[self.head.pos[:]] = [self.dir_nx, self.dir_ny]

                elif keys[pygame.K_UP] and self.dir_ny != 1:
                    self.dir_nx = 0
                    self.dir_ny = -1
                    self.turns[self.head.pos[:]] = [self.dir_nx, self.dir_ny]

                elif keys[pygame.K_DOWN] and self.dir_ny != -1:
                    self.dir_nx = 0
                    self.dir_ny = 1
                    self.turns[self.head.pos[:]] = [self.dir_nx, self.dir_ny]

            # joystick
            joystick_count = pygame.joystick.get_count()
            pygame.joystick.init()
            for i in range(joystick_count):
                joystick = pygame.joystick.Joystick(i)
                joystick.init()
                if event.type == pygame.JOYAXISMOTION:
                    axis = joystick.get_axis(0)
                    if axis < -0.5 and self.dir_nx != 1:
                        self.dir_nx = -1
                        self.dir_ny = 0
                        self.turns[self.head.pos[:]] = [self.dir_nx, self.dir_ny]
                    elif axis > 0.5 and self.dir_nx != -1:
                        self.dir_nx = 1
                        self.dir_ny = 0
                        self.turns[self.head.pos[:]] = [self.dir_nx, self.dir_ny]
                if event.type == pygame.JOYAXISMOTION:
                    axis = joystick.get_axis(1)
                    if axis < -0.5 and self.dir_ny != 1:
                        self.dir_nx = 0
                        self.dir_ny = -1
                        self.turns[self.head.pos[:]] = [self.dir_nx, self.dir_ny]
                    elif axis > 0.5 and self.dir_ny != -1:
                        self.dir_nx = 0
                        self.dir_ny = 1
                        self.turns[self.head.pos[:]] = [self.dir_nx, self.dir_ny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.dir_nx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows - 1, c.pos[1])
                elif c.dir_nx == 1 and c.pos[0] >= c.rows - 1:
                    c.pos = (0, c.pos[1])
                elif c.dir_ny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows - 1)
                elif c.dir_ny == 1 and c.pos[1] >= c.rows - 1:
                    c.pos = (c.pos[0], 0)
                else:
                    c.move(c.dir_nx, c.dir_ny)

    def reset(self, pos):
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dir_nx = 0
        self.dir_ny = 1

    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.dir_nx, tail.dir_ny
        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] + 1)))
        self.body[-1].dir_nx = dx
        self.body[-1].dir_ny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


def draw_grid(width, rows, surface):
    size_bwn = width // rows
    x = 0
    y = 0
    for li in range(rows):
        x += size_bwn
        y += size_bwn
        # pygame.draw.line(surface, (255, 50, 255, 0.2), (x, 0), (x, width))
        # pygame.draw.line(surface, (255, 50, 255, 0.2), (0, y), (width, x))


def redraw_window(width, win, rows, s, snack):
    win.fill((0, 0, 0))
    # background image
    win.blit(backgroundImg, (0, 0))
    s.draw(win)
    snack.draw(win)
    draw_grid(width, rows, win)
    pygame.display.update()


def random_snack(rows, items):
    positions = items.body
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break
    return x, y


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = Snake((255, 200, 100), (10, 10))
    snack = Cube(random_snack(rows, s), color=(255, 255, 0))
    flag = True
    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redraw_window(width, win, rows, s, snack)
        s.move()
        if s.body[0].pos == snack.pos:
            s.add_cube()
            snack = Cube(random_snack(rows, s), color=(255, 255, 0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                message_box('Game Over', 'Your Score is ' + str(len(s.body)))
                s.reset((10, 10))
                break

        redraw_window(width, win, rows, s, snack)


main()
