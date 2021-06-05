from colors import PURPLE, ORANGE, YELLOW, CYAN, GREY
import random
# level 0 means not alive, level 4 means unbreakable; 5 means changing
# powerup 0: none, 1: enlarge, 2: shrink, 3: speed, 4: capture, 5: thru


class brick:
    def __init__(self, x, y, level):
        self.x = x
        self.y = y
        self.level = level
        self.powerup = 0
        self.phit = 0

        if random.random() > 0.6:
            self.powerup = random.randint(1, 5)

        if self.level == 0:
            self.color = PURPLE
        elif self.level == 1:
            self.color = ORANGE
        elif self.level == 2:
            self.color = YELLOW
        elif self.level == 3:
            self.color = CYAN
        else:
            self.color = GREY

    def hit(self):
        if self.level == 5:
            self.level = random.randint(2, 4)
            if self.level == 4:
                self.color = CYAN
        self.level -= 1
        if self.level < 1:
            self.color = PURPLE
        elif self.level == 1:
            self.color = ORANGE
        elif self.level == 2:
            self.color = YELLOW

    def thruhit(self):
        self.level = 0
        self.color = PURPLE

    def powerhit(self, x, y):
        if self.powerup != 0:
            self.phit = 1
            self.hitx = x
            self.hity = y

    def powerupdate(self, left, len):
        self.hity += 1
        if self.hitx >= left and self.hitx < (left + len) and self.hity == 20:
            self.phit = 0
            return self.powerup

        if self.hity > 20:
            self.phit = 0

        return 0

    def multiupdate(self):
        if self.level == 5:
            if self.color == GREY:
                self.color = ORANGE
            elif self.color == ORANGE:
                self.color = YELLOW
            elif self.color == YELLOW:
                self.color = CYAN
            else:
                self.color = ORANGE

    def movedown(self):
        self.y += 1
