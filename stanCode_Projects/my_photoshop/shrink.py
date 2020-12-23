"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(big):
    """
    :param filename: str, the original image that is going to be shrink
    :return img: SimpleImage, the shrink image
    """
    big = SimpleImage(big)
    small = SimpleImage.blank(big.width // 2, big.height // 2)
    for y in range(small.height):
        for x in range(small.width):
            small_pixel = small.get_pixel(x,y)
            big_pixel = big.get_pixel(x*2, y*2)
            small_pixel.red = big_pixel.red
            small_pixel.green = big_pixel.green
            small_pixel.blue = big_pixel.blue
    return small


def main():
    """
    The program will shrink the designated image
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
