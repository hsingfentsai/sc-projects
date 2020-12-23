"""
File: my_drawing.py
Name: Fenny
----------------------
TODO: This picture presents a pumpkin smiling happily at the night of Halloween,
      The shinning moon, which flies high up in the sky, peacefully watching at the pumpkin.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLine, GLabel
from campy.graphics.gwindow import GWindow

window = GWindow(700, 450)

def main():
    """
    This picture presents a pumpkin smiling happily at the night of Halloween,
    The shinning moon, which flies high up in the sky, peacefully watching at the pumpkin.
    """
    set_up_night()
    set_up_moon()
    set_up_pumpkin()


def set_up_night():
    """
    The function will set up a black background, and 4 moons on the top of the drawing
    """
    night = GRect(700, 450)
    night.filled = True
    night.color = 'black'
    night.fill_color = 'black'
    window.add(night)


    cloud1 = GOval(100,70)
    cloud1.filled = True
    cloud1.color = 'gray'
    cloud1.fill_color = 'gray'
    window.add(cloud1, 210, 50)

    cloud2 = GOval(120, 100)
    cloud2.filled = True
    cloud2.color = 'gray'
    cloud2.fill_color = 'gray'
    window.add(cloud2, 230, 20)

    cloud3 = GOval(90, 100)
    cloud3.filled = True
    cloud3.color = 'gray'
    cloud3.fill_color = 'gray'
    window.add(cloud3, 260, 50)

    cloud4 = GOval(100, 80)
    cloud4.filled = True
    cloud4.color = 'gray'
    cloud4.fill_color = 'gray'
    window.add(cloud4, 300, 50)

    cloud5 = GOval(80, 50)
    cloud5.filled = True
    cloud5.color = 'gray'
    cloud5.fill_color = 'gray'
    window.add(cloud5, 550, 100)

    cloud6 = GOval(100, 60)
    cloud6.filled = True
    cloud6.color = 'gray'
    cloud6.fill_color = 'gray'
    window.add(cloud6, 500, 110)

    cloud7 = GOval(100, 50)
    cloud7.filled = True
    cloud7.color = 'gray'
    cloud7.fill_color = 'gray'
    window.add(cloud7, 580, 110)

    cloud8 = GOval(80, 80)
    cloud8.filled = True
    cloud8.color = 'gray'
    cloud8.fill_color = 'gray'
    window.add(cloud8, 550, 100)


def set_up_moon():
    """
    The function will set up a moon with blushes on the cheek and some whole on its face at the upper left part of the drawing
    and it will emits lights toward the pumpkin
    :return:
    """
    light = GLine(140, 100, 230, 205)
    light.color = 'lemonchiffon'
    window.add(light)

    light = GLine(130, 110, 220, 220)
    light.color = 'lemonchiffon'
    window.add(light)

    light = GLine(120, 120, 210, 235)
    light.color = 'lemonchiffon'
    window.add(light)

    light = GLine(110, 130, 200, 250)
    light.color = 'lemonchiffon'
    window.add(light)

    light = GLine(100, 140, 190, 265)
    light.color = 'lemonchiffon'
    window.add(light)

    light = GLine(90, 150, 180, 275)
    light.color = 'lemonchiffon'
    window.add(light)

    label = GLabel('HAPPY' + '  ' + 'HALLOWEEN')
    label.color = 'yellow'
    label.font = 'Times New Roman-40-bold'
    window.add(label, 220, 100)

    moon = GOval(100, 100)
    moon.filled = True
    moon.color = 'lemonchiffon'
    moon.fill_color = 'lemonchiffon'
    window.add(moon, 30, 30)

    moon_mouth1 = GOval(20, 20)
    moon_mouth1.filled = True
    moon_mouth1.color = 'black'
    moon_mouth1.fill_color = 'black'
    window.add(moon_mouth1, 75, 80)

    moon_mouth2 = GOval(20, 20)
    moon_mouth2.filled = True
    moon_mouth2.color = 'lemonchiffon'
    moon_mouth2.fill_color = 'lemonchiffon'
    window.add(moon_mouth2, 75, 78)

    moon_Leye1 = GOval(20, 20)
    moon_Leye1.filled = True
    moon_Leye1.color = 'black'
    moon_Leye1.fill_color = 'black'
    window.add(moon_Leye1, 60, 58)

    moon_Leye2 = GOval(20, 20)
    moon_Leye2.filled = True
    moon_Leye2.color = 'lemonchiffon'
    moon_Leye2.fill_color = 'lemonchiffon'
    window.add(moon_Leye2, 60, 56)

    moon_Reye1 = GOval(20, 20)
    moon_Reye1.filled = True
    moon_Reye1.color = 'black'
    moon_Reye1.fill_color = 'black'
    window.add(moon_Reye1, 90, 58)

    moon_Reye2 = GOval(20, 20)
    moon_Reye2.filled = True
    moon_Reye2.color = 'lemonchiffon'
    moon_Reye2.fill_color = 'lemonchiffon'
    window.add(moon_Reye2, 90, 56)

    hole1 = GOval(15, 10)
    hole1.filled = True
    hole1.color = 'wheat'
    hole1.fill_color = 'wheat'
    window.add(hole1, 50, 50)

    hole2 = GOval(8, 6)
    hole2.filled = True
    hole2.color = 'wheat'
    hole2.fill_color = 'wheat'
    window.add(hole2, 40, 65)

    hole3 = GOval(7, 5)
    hole3.filled = True
    hole3.color = 'wheat'
    hole3.fill_color = 'wheat'
    window.add(hole3, 115, 60)

    hole4 = GOval(15, 10)
    hole4.filled = True
    hole4.color = 'wheat'
    hole4.fill_color = 'wheat'
    window.add(hole4, 95, 110)

    hole5 = GOval(5, 5)
    hole5.filled = True
    hole5.color = 'wheat'
    hole5.fill_color = 'wheat'
    window.add(hole5, 55, 40)

    hole6 = GOval(5, 5)
    hole6.filled = True
    hole6.color = 'wheat'
    hole6.fill_color = 'wheat'
    window.add(hole6, 85, 120)

    blushL = GOval(10, 10)
    blushL.filled = True
    blushL.color = 'lightcoral'
    blushL.fill_color = 'lightcoral'
    window.add(blushL, 55, 80)

    blushR = GOval(10, 10)
    blushR.filled = True
    blushR.color = 'lightcoral'
    blushR.fill_color = 'lightcoral'
    window.add(blushR, 105, 80)


def set_up_pumpkin():
    """
    The function will set up a happy pumpkin
    """
    shadow = GOval(280, 50)
    shadow.filled = True
    shadow.color = 'gainsboro'
    shadow.fill_color = 'gainsboro'
    window.add(shadow, 300, 380)

    leaf = GPolygon()
    leaf.add_vertex((370,150))
    leaf.add_vertex((400,150))
    leaf.add_vertex((300,300))
    leaf.filled = True
    leaf.color = 'forestgreen'
    leaf.fill_color = 'forestgreen'
    window.add(leaf)

    pumpkin_dark = GOval(200,200)
    pumpkin_dark.filled = True
    pumpkin_dark.color = 'darkorange'
    pumpkin_dark.fill_color = 'darkorange'
    window.add(pumpkin_dark, 200, 200)

    pumpkin_dark = GOval(200, 200)
    pumpkin_dark.filled = True
    pumpkin_dark.color = 'darkorange'
    pumpkin_dark.fill_color = 'darkorange'
    window.add(pumpkin_dark, 300, 200)

    pumpkin_light = GOval(180, 200)
    pumpkin_light.filled = True
    pumpkin_light.color = 'orange'
    pumpkin_light.fill_color = 'orange'
    window.add(pumpkin_light, 230, 200)

    pumpkin_light = GOval(180, 200)
    pumpkin_light.filled = True
    pumpkin_light.color = 'orange'
    pumpkin_light.fill_color = 'orange'
    window.add(pumpkin_light, 290, 200)

    pumpkin_dark = GOval(200, 200)
    pumpkin_dark.filled = True
    pumpkin_dark.color = 'darkorange'
    pumpkin_dark.fill_color = 'darkorange'
    window.add(pumpkin_dark, 250, 200)

    mouth = GOval(170, 150)
    mouth.filled = True
    mouth.color = 'burlywood'
    mouth.fill_color = 'burlywood'
    window.add(mouth, 268, 240)

    mouth_shadow = GOval(150, 130)
    mouth_shadow.filled = True
    mouth_shadow.color = 'sienna'
    mouth_shadow.fill_color = 'sienna'
    window.add(mouth_shadow, 275, 250)

    pumpkin_dark = GOval(160, 150)
    pumpkin_dark.filled = True
    pumpkin_dark.color = 'darkorange'
    pumpkin_dark.fill_color = 'darkorange'
    window.add(pumpkin_dark, 270, 200)

    mouth_reck1 = GRect(20,30)
    mouth_reck1.filled = True
    mouth_reck1.color = 'darkorange'
    mouth_reck1.fill_color = 'darkorange'
    window.add(mouth_reck1, 280, 312)

    mouth_reck2 = GRect(18, 25)
    mouth_reck2.filled = True
    mouth_reck2.color = 'darkorange'
    mouth_reck2.fill_color = 'darkorange'
    window.add(mouth_reck2, 400, 315)

    mouth_reck3 = GRect(20, 20)
    mouth_reck3.filled = True
    mouth_reck3.color = 'darkorange'
    mouth_reck3.fill_color = 'darkorange'
    window.add(mouth_reck3, 325, 370)

    mouth_reck4 = GRect(20, 20)
    mouth_reck4.filled = True
    mouth_reck4.color = 'darkorange'
    mouth_reck4.fill_color = 'darkorange'
    window.add(mouth_reck4, 375, 370)

    Leye_back = GPolygon()
    Leye_back.add_vertex((280, 250))
    Leye_back.add_vertex((340, 280))
    Leye_back.add_vertex((270, 270))
    Leye_back.filled = True
    Leye_back.color = 'burlywood'
    Leye_back.fill_color = 'burlywood'
    window.add(Leye_back)

    Leye = GPolygon()
    Leye.add_vertex((290, 255))
    Leye.add_vertex((340, 280))
    Leye.add_vertex((280, 270))
    Leye.filled = True
    Leye.fill_color = 'black'
    window.add(Leye)

    Reye_back = GPolygon()
    Reye_back.add_vertex((420, 240))
    Reye_back.add_vertex((370, 275))
    Reye_back.add_vertex((430, 270))
    Reye_back.filled = True
    Reye_back.color = 'burlywood'
    Reye_back.fill_color = 'burlywood'
    window.add(Reye_back)

    Reye = GPolygon()
    Reye.add_vertex((410, 245))
    Reye.add_vertex((370, 275))
    Reye.add_vertex((420, 270))
    Reye.filled = True
    Reye.fill_color = 'black'
    window.add(Reye)


    nose_back = GPolygon()
    nose_back.add_vertex((355, 299))
    nose_back.add_vertex((335, 325))
    nose_back.add_vertex((375, 325))
    nose_back.filled = True
    nose_back.color = 'burlywood'
    nose_back.fill_color = 'burlywood'
    window.add(nose_back)

    nose = GPolygon()
    nose.add_vertex((350, 300))
    nose.add_vertex((340, 320))
    nose.add_vertex((370, 320))
    nose.filled = True
    nose.fill_color = 'black'
    window.add(nose)


if __name__ == '__main__':
    main()
