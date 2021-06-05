import numpy
from brick import brick
from colors import PURPLE, RED, GREEN, BLUE, BLACK, YELLOW
import random


class brickpipe:
    def __init__(self):
        self.bricks = numpy.empty(40, dtype=object)

        x = 0
        for i in range(5):
            for j in range(4):
                self.bricks[x] = brick((j*5)+5, i+3, random.randint(0, 5))
                x += 1

        for i in range(5):
            for j in range(4):
                self.bricks[x] = brick(41-(j*5), i+3, self.bricks[x-20].level)
                x += 1

        self.score = 0

    def print(self, x, y):
        for i in range(40):
            if x == self.bricks[i].x and y == self.bricks[i].y:
                print(self.bricks[i].color, end='')
            if self.bricks[i].phit == 1:
                if x == self.bricks[i].hitx and y == self.bricks[i].hity:
                    if self.bricks[i].powerup == 1:
                        print(RED, end='')
                    elif self.bricks[i].powerup == 2:
                        print(GREEN, end='')
                    elif self.bricks[i].powerup == 3:
                        print(BLUE, end='')
                    elif self.bricks[i].powerup == 4:
                        print(BLACK, end='')
                    else:
                        print(YELLOW, end='')

    def clear(self, x, y):
        for i in range(40):
            if x == self.bricks[i].x + 4 and y == self.bricks[i].y:
                print(PURPLE, end='')
            if self.bricks[i].phit == 1:
                if x == self.bricks[i].hitx and y == self.bricks[i].hity:
                    print(PURPLE, end='')

    def finalsolution(self):
        for i in range(40):
            self.bricks[i].movedown()
            if self.bricks[i].level != 0 and self.bricks[i].y == 21:
                return 1
        return 0

    def collide(self, x, y, vx, vy, tpp):
        count = 0
        for i in range(40):
            level = self.bricks[i].level
            if level != 4:
                count += level
            if level > 0:
                self.bricks[i].multiupdate()
                XX = self.bricks[i].x
                YY = self.bricks[i].y
                if x + vx >= XX and x + vx < XX + 5 and y + vy == YY:
                    if x >= XX and x < XX + 5 and y >= YY - 1 and y < YY + 2:
                        if tpp == 0:
                            if level < 4 or level == 5:
                                self.bricks[i].hit()
                                self.score += 1
                                if level == 1:
                                    self.bricks[i].powerhit(x + vx, y + vy)
                            return vx, -vy      # bottom and top surface of brick
                        if tpp == 1:
                            self.bricks[i].thruhit()
                            self.score += 1
                            if level == 1:
                                self.bricks[i].powerhit(x + vx, y + vy)
                            return vx, vy
                    elif x == XX - 1 or x == XX + 5:
                        if y == YY:
                            if tpp == 0:
                                if level < 4 or level == 5:
                                    self.bricks[i].hit()
                                    self.score += 1
                                    if level == 1:
                                        self.bricks[i].powerhit(x + vx, y + vy)
                                return -vx, vy  # side surfaces of brick
                            if tpp == 1:
                                self.bricks[i].thruhit()
                                self.score += 1
                                if level == 1:
                                    self.bricks[i].powerhit(x + vx, y + vy)
                                return vx, vy
                        elif y >= YY - 1 and y < YY + 2:
                            if tpp == 0:
                                if level < 4 or level == 5:
                                    self.bricks[i].hit()
                                    self.score += 1
                                    if level == 1:
                                        self.bricks[i].powerhit(x + vx, y + vy)
                                return -vx, -vy  # corners of the brick
                            if tpp == 1:
                                self.bricks[i].thruhit()
                                self.score += 1
                                if level == 1:
                                    self.bricks[i].powerhit(x + vx, y + vy)
                                return vx, vy
        if count == 0:
            return -100, 0                  # bricks over
        return vx, vy                       # ball not in proximity of brick
