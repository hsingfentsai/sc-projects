"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

THRESHOLD = 1.3
BLACK = 200
def main():
    """
    The program will combine the two image.
    When Fenny saw the extinct T-rex, she looks extremely surprised and excited.
    """
    me = SimpleImage("images/me.JPG")
    dinosaur = SimpleImage("images/dinosaur.jpg")

    dinosaur.make_as_big_as(me)
    combine = magic(me, dinosaur)
    combine.show()


def magic(me, dino):
    for y in range(dino.height):
        for x in range(dino.width):
            me_pixel = me.get_pixel(x,y)
            dino_pixel = dino.get_pixel(x,y)
            avg = (me_pixel.red+me_pixel.green+me_pixel.blue) / 3
            total = (me_pixel.red+me_pixel.green+me_pixel.blue)
            if me_pixel.green > avg*THRESHOLD and total>BLACK:
                me_pixel.red = dino_pixel.red
                me_pixel.green = dino_pixel.green
                me_pixel.blue = dino_pixel.blue
    return me





if __name__ == '__main__':
    main()
