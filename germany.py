#Erik Hansen
#9/26/2017
#germany.py - making German flag
from ggame import * 

red = Color(0xFF0000,1)
yellow = Color(0xFFFF00,1)
black = Color(0x000000,1)
blackoutline = LineStyle(1,black)
yellowoutline = LineStyle(1,yellow)
redoutline = LineStyle(1,red)

blackrectangle = RectangleAsset(700,150,blackoutline,black)
yellowrectangle = RectangleAsset(700,150,yellowoutline,yellow)
redrectangle = RectangleAsset(700,150,redoutline,red)

Sprite(blackrectangle)
Sprite(yellowrectangle, (0,150))
Sprite(redrectangle, (0,300))

App().run()
