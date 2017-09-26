#Erik Hansen
#9/26/2017
#germany.py - making German flag
from ggame import * 

red = Color(0xFF0000,1)
yellow = Color(0xFFFF00,1)
black = Color(0x000000,1)
blackOutline = LineStyle(1,black)
yellowOutline = LineStyle(1,yellow)
redOutline = LineStyle(1,red)

blackrectangle = RectangleAsset(400,100,blackoutline,black)
yellowrectangle = RectangleAsset(400,100,yellowoutline,yellow)
redrectangle = RectangleAsset(400,100,redoutline,red)

Sprite(blackrectangle)
Sprite(yellowrectangle, (0,100))
Sprite(redrectangle, (0,200))

App().run()
