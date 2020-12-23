"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

This program will present curve lines regarding the rank of names with in years from 1900 to 2010
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    interval = (width - (2*GRAPH_MARGIN_SIZE)) // len(YEARS)
    x_cord = GRAPH_MARGIN_SIZE + (interval*year_index)
    return x_cord


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for x in range(len(YEARS)):
        x_cord = get_x_coordinate(CANVAS_WIDTH, x)
        canvas.create_line(x_cord, 0, x_cord, CANVAS_HEIGHT)
        canvas.create_text(x_cord, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[x], anchor=tkinter.NW, font='times 15')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    ratio = (CANVAS_HEIGHT - (2*GRAPH_MARGIN_SIZE)) / MAX_RANK
    count = -1
    for i in range(len(lookup_names)):
        search_name = lookup_names[i]
        count += 1
        color_i = COLORS[count % 4]
        if search_name in name_data:
            for j in range(len(YEARS)):
                year = str(YEARS[j])
                x = get_x_coordinate(CANVAS_WIDTH, j)
                if year in name_data[search_name]:
                    y = GRAPH_MARGIN_SIZE + (ratio * (int(name_data[search_name][year])))
                    canvas.create_text(x+TEXT_DX, y, text=search_name + ' ' + str(name_data[search_name][year]),
                                       anchor=tkinter.SW, fill=color_i)
                else:
                    y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                    canvas.create_text(x+TEXT_DX, y, anchor=tkinter.SW, text=search_name +' *' , fill=color_i)
                if j == 0:
                    x_pre = x
                    y_pre = y
                else:
                    x_later = x
                    y_later = y
                    canvas.create_line(x_pre, y_pre, x_later, y_later, fill=color_i)
                    x_pre = x_later
                    y_pre = y_later

                # else:
                #     if year in name_data[search_name]:
                #         x_2 = get_x_coordinate(CANVAS_WIDTH, j)
                #         y_2 = GRAPH_MARGIN_SIZE + (y * (int(name_data[search_name][year])))
                #         canvas.create_line(x_1, y_1, x_2, y_2, width=LINE_WIDTH)
                #         canvas.create_text(x_1+TEXT_DX, y_1, text=search_name + ' ' + name_data[search_name][year])
                #         x_1 = x_2
                #         y_1 = y_2
                #
                #     else:
                #         x_2 = get_x_coordinate(CANVAS_WIDTH, j)
                #         y_2 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                #         canvas.create_line(x_1, y_1, x_2, y_2, width=LINE_WIDTH)
                #         canvas.create_text(x_1+TEXT_DX, y_1, text=search_name +' *')
                #         x_1 = x_2
                #         y_1 = y_2






# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
