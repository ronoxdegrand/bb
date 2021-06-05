class ball:
    def __init__(self, x, y, vx, vy, lives):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.toLaunch = True
        self.lives = lives

    def blockupdate(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def autoupdate(self, padleft, padlen, catchPU):
        nx = self.x + self.vx
        ny = self.y + self.vy

        # if next frame is beyond, flip -> recalculate -> print

        if nx > 50 or nx < 0:  # for side walls
            self.vx = -self.vx
            nx = self.x + self.vx
        if ny < 0:             # for top wall
            self.vy = -self.vy
            ny = self.y + self.vy
        if nx >= padleft and nx < (padleft + padlen) and ny == 20:  # for paddle
            if catchPU == 0:
                if nx < (padleft + round(padlen/5)):
                    self.vx = -2
                elif nx < (padleft + round(2*padlen/5)):
                    self.vx = -1
                elif nx < (padleft + round(3*padlen/5)):
                    self.vx = 0
                elif nx < (padleft + round(4*padlen/5)):
                    self.vx = 1
                else:
                    self.vx = 2
                self.vy = -self.vy
                nx = self.x + self.vx
                ny = self.y + self.vy
            elif catchPU == 1:
                self.toLaunch = True
                nx = self.x
                ny = self.y
        if ny > 21:            # for bottom wall
            self.toLaunch = True
            self.lives -= 1

        self.x = nx
        self.y = ny

    def startstate(self, padleft, padlen):
        self.x = padleft + padlen//2
        self.y = 19
        self.vx = 0
        self.vy = -1
