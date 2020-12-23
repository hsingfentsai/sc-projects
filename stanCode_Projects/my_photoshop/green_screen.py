"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background, figure):
    """
    :param background_img: str, the background image to be put behind the character
    :param figure_img: str, the image with the character which has green screen at the back
    :return: SimpleImage, combined image
    """
    for y in range(background.height):
        for x in range(background.width):
            pixel_figure = figure.get_pixel(x,y)
            pixel_background = background.get_pixel(x,y)
            bigger =max(pixel_figure.red, pixel_figure.blue)
            if pixel_figure.green > bigger*2:
                pixel_figure.red = pixel_background.red
                pixel_figure.green = pixel_background.green
                pixel_figure.blue = pixel_background.blue
    return figure


def main():
    """
    The program will make image-MillenniumFalcon as the background(green screen part) of image-ReyGreenScreen
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
