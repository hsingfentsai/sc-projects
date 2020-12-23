"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random


BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 120      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.

class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING, lives = 0, score = 0,
                 title='Breakout'):
        self.lives = lives
        self.score = score

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create Score Label
        self.score_label = GLabel('SCORE: '+ str(self.score))
        self.score_label.font ='Dialog-30-bold'
        self.window.add(self.score_label, 0, self.score_label.height)

        self.win_label = GLabel('YOU WIN!!')
        self.win_label.font = 'Times New Roman-40-bold'

        self.lose_label = GLabel('YOU LOSE!!')
        self.lose_label.font = 'Times New Roman-40-bold'

        #Create lives label
        self.lives_label = GLabel('lives left: ' + str(self.lives))
        self.lives_label.font = 'Dialog-20-bold'
        self.window.add(self.lives_label, self.window.width-self.lives_label.width, self.window.height-self.lives_label.height)


        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width) / 2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.paddle.color = 'navy'
        self.paddle.fill_color = 'navy'
        self.window.add(self.paddle)
        self.paddle_offset = PADDLE_OFFSET

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius, ball_radius)
        self.ball.filled = True
        self.window.add(self.ball, (window_width-self.ball.width)/2, (window_height-self.ball.height)/2)

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

        # Initialize our mouse listeners.
        onmousemoved(self.on_paddle_move)
        onmouseclicked(self.tap)
        self.tap_to_start = False


        # Draw bricks.
        self.brick_width = BRICK_WIDTH
        self.brick_height = BRICK_HEIGHT
        self.brick_rows = BRICK_ROWS
        self.brick_cols = BRICK_COLS
        self.brick_offset = PADDLE_OFFSET
        self.brick_spacing = BRICK_SPACING
        self.brick_maker()
        self.brick_bottom = self.brick_offset + (self.brick_height + self.brick_spacing) * self.brick_rows
        self.brick_num = self.brick_rows * self.brick_cols



    def tap(self, mouse):
        """
        This function determines whether the user clicks in the window area
        pre-condition: self.tap_to_start = False
        post-condition: self.tap_to_start = True
        :param mouse: float, information of the mouse
        """
        ball_pos = self.window.get_object_at(self.window.width / 2, self.window.height / 2)
        if ball_pos is not None:
            if self.lives > 0:
                self.tap_to_start = True
                # self.lives -= 1
                # self.lives_label.text = 'lives left: ' + str(self.lives)


    def check_object(self):
        """
        This function determine whether the ball bump into any object(such as paddle and bricks)
        :return: boolean, whether the ball bumped into any object (None, not None)
        """
        o = self.window.get_object_at(self.ball.x, self.ball.y)
        if o is not None:
            return o
        else:
            o = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
            if o is not None:
                return o
            else:
                o = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)
                if o is not None:
                    return o
                else:
                    o = self.window.get_object_at(self.ball.x+ self.ball.width, self.ball.y + self.ball.height)
                    if o is not None:
                        return o
                    else:
                        return None


    def check_pad_or_bric(self, o):
        """
        This function determines whether the ball bump in to paddle or brick.
        Pre-condition: bumped into either paddle or brick
        Post-condition: if is paddle, the ball will bounce back;  if it is a brick, the brick will be removed then the ball will bounce back
        :param o: boolean, whether the ball bumped into any object (None, not None)
        """
        if o is not None and o is not self.paddle:  # is brick(need to remove, then bounce)

            if o is not self.score_label and o is not self.win_label and o is not self.lives_label:
                self.window.remove(o)
                self.__dy = - self.__dy
                self.score += 1
                self.score_label.text = 'SCORE: ' + str(self.score)
                if self.score == self.brick_num:
                    self.window.remove(self.ball)
                    self.window.add(self.win_label, (self.window.width-self.win_label.width)/2, (self.window.height-self.win_label.height)/2)
        elif o is not None and o is self.paddle:  # is paddle(just bounce)
            self.__dy = - self.__dy


    def bounce(self):
        """
        The function makes the ball stays in the window area. If it touch the width of the window, it will bounce toward the other direction
        """
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy
        if self.ball.y > self.window.height:
            if self.lives > 0:
                self.lives -= 1
                self.lives_label.text = 'lives left: ' + str(self.lives)
                self.window.add(self.ball, (self.window.width-self.ball.width)/2, (self.window.height-self.ball.height)/2)
                self.tap_to_start = False
            else:
                self.window.add(self.lose_label, (self.window.width-self.lose_label.width)/2, (self.window.height-self.lose_label.height)/2)


    def get__dx(self):
        """
        get the horizontal speed of the ball
        :return: float, horizontal speed
        """
        return self.__dx


    def get__dy(self):
        """
        get the vertical speed of the ball
        :return: float, vertical speed
        """
        return self.__dy


    def on_paddle_move(self, mouse):
        """
        This function will locate the position of the paddle according to the location of the mouse
        :param mouse: float, information of the mouse
        """
        if mouse.x <= 0:
            self.paddle.x = 0
            self.paddle.y = self.window.height - self.paddle_offset

        elif mouse.x >= 0 + self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
            self.paddle.y = self.window.height - self.paddle_offset

        else:
            self.paddle.x = mouse.x - self.paddle.width / 2
            self.paddle.y = self.window.height - self.paddle_offset


    def brick_maker(self):
        """
        This function will create bricks according to the number of BRICK_ROWS and BRICK_COLS.
        """
        self_brick = GRect(self.brick_width, self.brick_height)
        brick_bottom = self.brick_offset + (self.brick_height + self.brick_spacing) * self.brick_rows

        for i in range(0, self.window.width, self_brick.width + self.brick_spacing):
            for j in range(self.brick_offset, brick_bottom, self_brick.height + self.brick_spacing):
                cal = ((j - self.brick_offset) // (self.brick_height + self.brick_spacing)) % self.brick_rows

                if 0 <= cal <= 1:
                    brick = GRect(self.brick_width, self.brick_height)
                    brick.filled = True
                    brick.color = 'darkred'
                    brick.fill_color = 'darkred'
                    self.window.add(brick, i, j)

                if 2 <= cal <= 3:
                    brick = GRect(self.brick_width, self.brick_height)
                    brick.filled = True
                    brick.color = 'red'
                    brick.fill_color = 'red'
                    self.window.add(brick, i, j)

                if 4 <= cal <= 5:
                    brick = GRect(self.brick_width, self.brick_height)
                    brick.filled = True
                    brick.color = 'darkorange'
                    brick.fill_color = 'darkorange'
                    self.window.add(brick, i, j)


                if 6 <= cal <= 7:
                    brick = GRect(self.brick_width, self.brick_height)
                    brick.filled = True
                    brick.color = 'orange'
                    brick.fill_color = 'orange'
                    self.window.add(brick, i, j)

                if 8 <= cal <= 9:
                    brick = GRect(self.brick_width, self.brick_height)
                    brick.filled = True
                    brick.color = 'blanchedalmond'
                    brick.fill_color = 'blanchedalmond'
                    self.window.add(brick, i, j)

                if 10 <= cal <= 11:
                    brick = GRect(self.brick_width, self.brick_height)
                    brick.filled = True
                    brick.color = 'yellow'
                    brick.fill_color = 'yellow'
                    self.window.add(brick, i, j)

                if 12 <= cal <= 13:
                    brick = GRect(self.brick_width, self.brick_height)
                    brick.filled = True
                    brick.color = 'greenyellow'
                    brick.fill_color = 'greenyellow'
                    self.window.add(brick, i, j)

                if 14 <= cal <= 15:
                    brick = GRect(self.brick_width, self.brick_height)
                    brick.filled = True
                    brick.color = 'limegreen'
                    brick.fill_color = 'limegreen'
                    self.window.add(brick, i, j)

                if 16 <= cal <= 17:
                    brick = GRect(self.brick_width, self.brick_height)
                    brick.filled = True
                    brick.color = 'skyblue'
                    brick.fill_color = 'skyblue'
                    self.window.add(brick, i, j)

                if 18 <= cal <= 19:
                    brick = GRect(self.brick_width, self.brick_height)
                    brick.filled = True
                    brick.color = 'dodgerblue'
                    brick.fill_color = 'dodgerblue'
                    self.window.add(brick, i, j)

                if 20 <= cal <= 21:
                    brick = GRect(self.brick_width, self.brick_height)
                    brick.filled = True
                    brick.color = 'navy'
                    brick.fill_color = 'navy'
                    self.window.add(brick, i, j)

                if 22 <= cal <= 23:
                    brick = GRect(self.brick_width, self.brick_height)
                    brick.filled = True
                    brick.color = 'purple'
                    brick.fill_color = 'purple'
                    self.window.add(brick, i, j)

                if 24 <= cal <= 25:
                    brick = GRect(self.brick_width, self.brick_height)
                    brick.filled = True
                    brick.color = 'darkviolet'
                    brick.fill_color = 'darkviolet'
                    self.window.add(brick, i, j)

                if 26 <= cal <= 27:
                    brick = GRect(self.brick_width, self.brick_height)
                    brick.filled = True
                    brick.color = 'blueviolet'
                    brick.fill_color = 'blueviolet'
                    self.window.add(brick, i, j)

