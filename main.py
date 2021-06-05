import os
import numpy
from time import sleep
from collections import deque
from getch import user_input
from pad import pad
from ball import ball
from brickpipe import brickpipe
from colors import YELLOW, PURPLE, RESET, CLEAR, RED, GREEN, BLUE, GREY


os.system("stty echo")
grid = numpy.full((21, 51), '\u2588')
pad = pad(20, 11)
ball = ball(25, 19, -1, -1, 3)
brickpipe = brickpipe()
powerups = 0
powerq = deque()
timeq = deque()
timepop = 0
catchPU = 0
tpp = 0
key = ""
time = 0
millitime = 0
leveltime = 0
speed = 0.1
nextlevel = False
netlevel = 1

os.system('cls' if os.name == 'nt' else 'clear')

print(RESET)

# dashboard
print("                   Breaking Bad")
print("X: exit\tA: \u2190\tD: \u2192\tSpace: \u2191\t.:nxt lvl")
print(RED, "\u2588: enlarge", GREEN, "\u2588: small", BLUE,
      "\u2588: speed", GREY, "\u2588: catch", YELLOW, "\u2588: thru")
print("Score:\t\tLives:\t\tTime:\t     Level:")

print(PURPLE, end='')

while(key != "x"):
    os.system("stty -echo")

    millitime += 0.3
    if millitime >= 1:
        millitime = 0
        time += 1
        leveltime += 1
    print(YELLOW, brickpipe.score, "\t\t", ball.lives,
          "\t\t", time, "\t\t", netlevel, PURPLE)

    if ball.lives == 0:
        break

    # render loop
    i = 0
    while i < 21:
        j = 0
        while j < 51:

            # begin changing color
            brickpipe.print(j, i)
            if i == ball.y and j == ball.x:
                print(RESET, end='')
            if i == 20 and j == pad.left:
                print(RESET, end='')

            print(grid[i, j], end='')

            # begin reseting color
            brickpipe.clear(j, i)
            if i == ball.y and j == ball.x:
                print(PURPLE, end='')
            if i == 20 and j == (pad.left + pad.len - 1):
                print(PURPLE, end='')

            j += 1
        print('')
        i += 1

    for i in range(40):
        if brickpipe.bricks[i].powerup > 0 and brickpipe.bricks[i].phit == 1:
            powerups = brickpipe.bricks[i].powerupdate(pad.left, pad.len)
            if powerups == 1:
                pad.inc(5)
            elif powerups == 2:
                pad.inc(-5)
            elif powerups == 3:
                speed *= 0.5
            elif powerups == 4:
                catchPU = 1
            elif powerups == 5:
                tpp = 1
            if powerups > 0:
                powerq.append(powerups)
                timeq.append(time + 15)

    if len(timeq) > 0:
        if timeq[-1] == time:
            timeq.popleft()
            powdown = powerq.popleft()
            if powdown == 1:
                pad.inc(-5)
            elif powdown == 2:
                pad.inc(5)
            elif powdown == 3:
                speed *= 2
            elif powdown == 4:
                catchPU = 0
            elif powdown == 5:
                tpp = 0

    # input tree
    key = user_input()
    if key.startswith("x"):
        break
    elif key.startswith("d"):
        pad.mov(2)
    elif key.startswith("a"):
        pad.mov(-2)
    elif key.startswith("."):
        nextlevel = True
    elif key.startswith(" "):
        ball.toLaunch = False

    vx, vy = brickpipe.collide(ball.x, ball.y, ball.vx, ball.vy, tpp)
    if vx == -100:
        nextlevel = True
    else:
        ball.blockupdate(vx, vy)

    if nextlevel == True:
        netlevel += 1
        leveltime = 0
        nextlevel = False
        brickpipe.__init__()
        ball.toLaunch = True
        if netlevel == 4:
            break
        while len(timeq) > 0:
            timeq.popleft()
            powdown = powerq.popleft()
            if powdown == 1:
                pad.inc(-5)
            elif powdown == 2:
                pad.inc(5)
            elif powdown == 3:
                speed *= 2
            elif powdown == 4:
                catchPU = 0
            elif powdown == 5:
                tpp = 0

    if ball.toLaunch == True:
        ball.startstate(pad.left, pad.len)
    else:
        ball.autoupdate(pad.left, pad.len, catchPU)

    if leveltime > 10 and millitime == 0:
        if (brickpipe.finalsolution() == 1):
            break

    sleep(speed)
    print(CLEAR, end='')

print(RESET, end='')
os.system("stty echo")
print("---------------------GAME OVER---------------------")
