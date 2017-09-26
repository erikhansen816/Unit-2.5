#Erik Hansen
#9/26/2017
#house.py - making a house

from ggame import *

blue = Color(0x0000FF,1)
black = Color(0x000000,1)
blackoutline = LineStyle(1,black)
bluesquare = RectangleAsset(200,200,blackoutline,blue)
bluetriangle = PolygonAsset([(25,150),(175,250),(325,150)],blackoutline,blue)


Sprite(bluesquare)
Sprite(bluetriangle)
App().run()
