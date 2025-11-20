import pygame
import sys
import random

pygame.init()


class Snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = black

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % WIDTH), (cur[1] + (y * GRID_SIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, black, r, 1)

    def handle_keys(self,food_pos):
        head=self.get_head_position()
        distance=(head[0]-food_pos[0],head[1]-food_pos[1])

        left_gap = 100
        right_gap = 100
        top_gap = 100
        bot_gap = 100

        for i in range(1, int(GRID_WIDTH)):
            if (head[0], head[1] - (i * GRID_SIZE)) in self.positions:
                if top_gap < i:
                    top_gap = i
            if (head[0], head[1] + (i * GRID_SIZE)) in self.positions:
                if bot_gap < i:
                    bot_gap = i
            if (head[0] - (i * GRID_SIZE), head[1]) in self.positions:
                if left_gap < i:
                    left_gap = i
            if (head[0] + (i * GRID_SIZE), head[1]) in self.positions:
                if right_gap < i:
                    right_gap = i
        colliding=''
        if self.direction==DOWN and (head[0],head[1]+GRID_SIZE) in self.positions:
            colliding='down'
        if self.direction==UP and (head[0],head[1]-GRID_SIZE) in self.positions:
            colliding='up'
        if self.direction==LEFT and (head[0]-GRID_SIZE,head[1]) in self.positions:
            colliding='left'
        if self.direction==RIGHT and (head[0]+GRID_SIZE,head[1]) in self.positions:
            colliding='right'

        if (distance[0]>0 or ((colliding=='up' or colliding=='down') and left_gap>=right_gap)) and (head[0]-GRID_SIZE,head[1]) not in self.positions:
            self.turn(LEFT)
        if (distance[0]<0 or ((colliding=='up' or colliding=='down') and right_gap>left_gap)) and (head[0]+GRID_SIZE,head[1]) not in self.positions:
            self.turn(RIGHT)
        if (distance[1] > 0 or ((colliding=='left' or colliding=='right') and top_gap>=bot_gap)) and (head[0],head[1]-GRID_SIZE) not in self.positions:
            self.turn(UP)
        if (distance[1] < 0 or ((colliding=='left' or colliding=='right') and bot_gap>top_gap)) and (head[0],head[1]+GRID_SIZE) not in self.positions:
            self.turn(DOWN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
             # elif event.type == pygame.KEYDOWN:
             #    if event.key == pygame.K_UP:
             #        self.turn(UP)
             #    elif event.key == pygame.K_DOWN:
             #        self.turn(DOWN)
             #    elif event.key == pygame.K_LEFT:
             #        self.turn(LEFT)
             #    elif event.key == pygame.K_RIGHT:
             #        self.turn(RIGHT)


class Food(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = red
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, black, r, 1)


def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if ((x + y) % 2) == 0:
                r = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, gray1, r)
            else:
                rr = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, gray2, rr)


WIDTH = 480
HEIGHT = 480
gray1 = (120, 120, 120)
gray2 = (170, 170, 170)
red = (200, 40, 40)
green = (20, 200, 50)
black = (0, 0, 0)
GRID_SIZE = 20
GRID_WIDTH = WIDTH / GRID_SIZE
GRID_HEIGHT = HEIGHT / GRID_SIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
font = pygame.font.Font('freesansbold.ttf', 30)


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()

    score = 0
    while True:
        clock.tick(15)
        snake.handle_keys(food.position)
        drawGrid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 0))
        text = font.render("Score {0}".format(score), True, black)
        screen.blit(text, (5, 10))
        pygame.display.update()


main()