"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

To Do:
This program is a game that there will be a ball bouncing between bricks and paddle.
After the user click on the designated area, the game will start. User need to move the paddle to bounce back the ball.
If the ball bump into a brick, the brick will get removes and the user will get a point.
If the ball drops underneath the paddle area, the game will restart.
There will be 3 attempts for the user to play.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3




def main():

    graphics = BreakoutGraphics(lives = NUM_LIVES, score = 0)
    # Add animation loop here!
    while True:
        pause(FRAME_RATE)
        if graphics.tap_to_start:
            graphics.ball.move(graphics.get__dx(), graphics.get__dy())
            graphics.bounce()
            o = graphics.check_object()
            graphics.check_pad_or_bric(o)
            if graphics.score == graphics.brick_num:
                graphics.window.remove(graphics.ball)
                graphics.window.add(graphics.win_label, (graphics.window.width - graphics.win_label.width) / 2,
                                (graphics.window.height - graphics.win_label.height) / 2)
                break




if __name__ == '__main__':
    main()
