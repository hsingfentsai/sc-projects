"""
File: bouncing_ball.py
Name: Fenny
-------------------------
TODO:This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
VY = 2
DELAY = 10
GRAVITY = 0.5
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
CLICK = 0

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
ball.color = 'black'
ball.fill_color = 'black'
window.add(ball)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(bounce)


def bounce(m):
    """
    pre-condition: The ball is at(30, 40), waiting for the user to click, then the ball wil start bouncing to the floor
    post-condition: After 3 clicks, the ball will be at (30, 40), the ball will have no response to anymore clicks

    """
    global VX, VY, CLICK
    check_ball = window.get_object_at(START_X + SIZE / 2, START_Y + SIZE / 2)
    if check_ball is not None:
        CLICK += 1
        if CLICK <= 3:
            while True:
                ball.move(VX, VY)
                VY = VY + GRAVITY
                if ball.y+SIZE >= window.height:
                    VY = -VY*REDUCE
                pause(DELAY)
                if ball.x >= window.width:
                    ball.x = START_X
                    ball.y = START_Y
                    break


if __name__ == "__main__":
    main()
