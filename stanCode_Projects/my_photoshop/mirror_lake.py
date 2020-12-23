"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original image
    :return: SimpleImage, the reflected image
    """
    original = SimpleImage(filename)
    new =  SimpleImage.blank(original.width, original.height*2)
    for y in range(original.height):
        for x in range(original.width):
            original_pixel = original.get_pixel(x,y)
            upper_pixel = new.get_pixel(x,y)
            lower_pixel = new.get_pixel(x,new.height-y-1)

            upper_pixel.red = original_pixel.red
            upper_pixel.green = original_pixel.green
            upper_pixel.blue = original_pixel.blue

            lower_pixel.red = original_pixel.red
            lower_pixel.green = original_pixel.green
            lower_pixel.blue = original_pixel.blue
    return new


def main():
    """
    The program will flip the image upside down and present a mirror-liked image
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
