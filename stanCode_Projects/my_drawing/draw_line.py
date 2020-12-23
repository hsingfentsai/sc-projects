"""
File: draw_line.py
Name: Fenny
-------------------------
TODO:This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow()
SIZE = 5
click = 0       # to record down which click is it
first_x = 0     # to record down the x-axis of the first click
first_y = 0     # to record down the y-axis of the first click


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    onmouseclicked(draw)


def draw(mouse):
    """
    The function will response to the clicks from the user.
    The first click, there will be a circle under the mouse.
    The second click, there will be a line connecting the first circle and the position of second click.
    :param mouse: the position of the mouse
    """
    global click, first_x, first_y

    if click == 0:
        circle = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        circle.filled = True
        circle.fill_color = 'white'
        window.add(circle)
        first_x = circle.x + SIZE / 2
        first_y = circle.y + SIZE / 2
        click += 1

    maybe_click = window.get_object_at(mouse.x, mouse.y)
    circle_1 = window.get_object_at(first_x, first_y)

    if click == 1 and maybe_click is None:
        line = GLine(first_x, first_y, mouse.x, mouse.y)
        window.add(line)
        window.remove(circle_1)
        click -= 1


if __name__ == "__main__":
    main()
