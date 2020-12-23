"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(old):
    """
    :param img: str, the image to be blurred
    :return: SimpleImage, blurred image
    """
    new = SimpleImage.blank(old.width, old.height)
    for y in range(old.height):
        for x in range(old.width):
            old_pixel = old.get_pixel(x,y)
            new_pixel = new.get_pixel(x,y)

            if x==0 and y==0:
                old_pixel_right = old.get_pixel(x + 1, y)
                old_pixel_downright = old.get_pixel(x + 1, y + 1)
                old_pixel_down = old.get_pixel(x, y + 1)

                new_pixel.red = (old_pixel.red + old_pixel_right.red + old_pixel_down.red + old_pixel_downright.red) / 4
                new_pixel.green = (old_pixel.green + old_pixel_right.green + old_pixel_down.green + old_pixel_downright.green) / 4
                new_pixel.red = (old_pixel.blue + old_pixel_right.blue + old_pixel_down.blue + old_pixel_downright.blue) / 4

            elif x==old.width-1 and y==0:
                old_pixel_left = old.get_pixel(x - 1, y)
                old_pixel_downleft = old.get_pixel(x - 1, y + 1)
                old_pixel_down = old.get_pixel(x, y + 1)

                new_pixel.red = (old_pixel.red + old_pixel_left.red + old_pixel_downleft.red + old_pixel_down.red) / 4
                new_pixel.green = (old_pixel.green + old_pixel_left.green + old_pixel_downleft.green + old_pixel_down.green) / 4
                new_pixel.red = (old_pixel.blue + old_pixel_left.blue + old_pixel_downleft.blue + old_pixel_down.blue) / 4

            elif x==0 and y==old.height-1:

                old_pixel_upmiddle = old.get_pixel(x, y - 1)
                old_pixel_upright = old.get_pixel(x + 1, y - 1)
                old_pixel_right = old.get_pixel(x + 1, y)

                new_pixel.red = (old_pixel.red + old_pixel_upmiddle.red + old_pixel_upright.red + old_pixel_right.red) / 4
                new_pixel.green = (old_pixel.green + old_pixel_upmiddle.green + old_pixel_upright.green + old_pixel_right.green) / 4
                new_pixel.red = (old_pixel.blue + old_pixel_upmiddle.blue + old_pixel_upright.blue + old_pixel_right.blue) / 4

            elif x==old.width-1 and y==old.height-1:
                old_pixel_upleft = old.get_pixel(x - 1, y - 1)
                old_pixel_upmiddle = old.get_pixel(x, y - 1)
                old_pixel_left = old.get_pixel(x - 1, y)

                new_pixel.red = (old_pixel.red + old_pixel_upmiddle.red + old_pixel_upleft.red + old_pixel_left.red) / 4
                new_pixel.green = (old_pixel.green + old_pixel_upmiddle.green + old_pixel_upleft.green + old_pixel_left.green) / 4
                new_pixel.red = (old_pixel.blue + old_pixel_upmiddle.blue + old_pixel_upleft.blue + old_pixel_left.blue) / 4

            elif y==0:

                old_pixel_left = old.get_pixel(x - 1, y)
                old_pixel_right = old.get_pixel(x + 1, y)
                old_pixel_downleft = old.get_pixel(x - 1, y + 1)
                old_pixel_down = old.get_pixel(x, y + 1)
                old_pixel_downright = old.get_pixel(x + 1, y + 1)

                new_pixel.red = (old_pixel.red + old_pixel_left.red + old_pixel_right.red
                                 + old_pixel_downleft.red + old_pixel_down.red + old_pixel_downright.red) / 6
                new_pixel.green = (old_pixel.green + old_pixel_left.green + old_pixel_right.green
                                   + old_pixel_downleft.green + old_pixel_down.green + old_pixel_downright.green) / 6
                new_pixel.blue = (old_pixel.blue + old_pixel_left.blue + old_pixel_right.blue
                                  + old_pixel_downleft.blue + old_pixel_down.blue + old_pixel_downright.blue) / 6

            elif y == old.height-1:
                old_pixel_upleft = old.get_pixel(x - 1, y - 1)
                old_pixel_upmiddle = old.get_pixel(x, y - 1)
                old_pixel_upright = old.get_pixel(x + 1, y - 1)
                old_pixel_left = old.get_pixel(x - 1, y)
                old_pixel_right = old.get_pixel(x + 1, y)

                new_pixel.red = (old_pixel.red + old_pixel_upleft.red + old_pixel_upmiddle.red
                                 + old_pixel_upright.red+ old_pixel_left.red + old_pixel_right.red)  / 6
                new_pixel.green = (old_pixel.green + old_pixel_upleft.green + old_pixel_upmiddle.green
                                   + old_pixel_upright.green+ old_pixel_left.green + old_pixel_right.green) / 6
                new_pixel.blue = (old_pixel.blue + old_pixel_upleft.blue + old_pixel_upmiddle.blue
                                  + old_pixel_upright.blue+ old_pixel_left.blue + old_pixel_right.blue) / 6

            elif x == 0:

                old_pixel_upmiddle = old.get_pixel(x, y - 1)
                old_pixel_upright = old.get_pixel(x + 1, y - 1)
                old_pixel_right = old.get_pixel(x + 1, y)
                old_pixel_down = old.get_pixel(x, y + 1)
                old_pixel_downright = old.get_pixel(x + 1, y + 1)

                new_pixel.red = (old_pixel.red + old_pixel_upmiddle.red + old_pixel_upright.red
                                 + old_pixel_right.red + old_pixel_down.red + old_pixel_downright.red) / 6
                new_pixel.green = (old_pixel.green + old_pixel_upmiddle.green + old_pixel_upright.green
                                   + old_pixel_right.green+ old_pixel_down.green + old_pixel_downright.green) / 6
                new_pixel.blue = (old_pixel.blue + old_pixel_upmiddle.blue + old_pixel_upright.blue
                                  + old_pixel_right.blue + old_pixel_down.blue + old_pixel_downright.blue) / 6

            elif x == old.width-1:
                old_pixel_upleft = old.get_pixel(x - 1, y - 1)
                old_pixel_upmiddle = old.get_pixel(x, y - 1)
                old_pixel_left = old.get_pixel(x - 1, y)
                old_pixel_downleft = old.get_pixel(x - 1, y + 1)
                old_pixel_down = old.get_pixel(x, y + 1)

                new_pixel.red = (old_pixel.red + old_pixel_upleft.red + old_pixel_upmiddle.red
                                 + old_pixel_left.red + old_pixel_downleft.red + old_pixel_down.red ) / 6
                new_pixel.green = (old_pixel.green + old_pixel_upleft.green + old_pixel_upmiddle.green
                                + old_pixel_left.green+ old_pixel_downleft.green + old_pixel_down.green) / 6
                new_pixel.blue = (old_pixel.blue + old_pixel_upleft.blue + old_pixel_upmiddle.blue
                                + old_pixel_left.blue + old_pixel_downleft.blue + old_pixel_down.blue) / 6

            else:
                old_pixel_upleft = old.get_pixel(x - 1, y - 1)
                old_pixel_upmiddle = old.get_pixel(x, y - 1)
                old_pixel_upright = old.get_pixel(x + 1, y - 1)
                old_pixel_left = old.get_pixel(x - 1, y)
                old_pixel_right = old.get_pixel(x + 1, y)
                old_pixel_downleft = old.get_pixel(x - 1, y + 1)
                old_pixel_down = old.get_pixel(x, y + 1)
                old_pixel_downright = old.get_pixel(x + 1, y + 1)

                new_pixel.red = (old_pixel.red + old_pixel_upleft.red + old_pixel_upmiddle.red + old_pixel_upright.red
                             +old_pixel_left.red + old_pixel_right.red + old_pixel_downleft.red + old_pixel_down.red + old_pixel_downright.red) / 9
                new_pixel.green = (old_pixel.green + old_pixel_upleft.green + old_pixel_upmiddle.green + old_pixel_upright.green
                               +old_pixel_left.green + old_pixel_right.green + old_pixel_downleft.green + old_pixel_down.green + old_pixel_downright.green) / 9
                new_pixel.blue = (old_pixel.blue + old_pixel_upleft.blue + old_pixel_upmiddle.blue + old_pixel_upright.blue
                               +old_pixel_left.blue + old_pixel_right.blue + old_pixel_downleft.blue + old_pixel_down.blue + old_pixel_downright.blue) / 9
    return new


def main():
    """
    The program will make the image blur
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
