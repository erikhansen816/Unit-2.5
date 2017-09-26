#Erik Hansen
#9/26/2017
#warmup5.py

from ggame import *

yellow = Color(0xFFFF00,1)
yellow_outline = LineStyle(1,yellow)
blue = Color(0x0000FF,1)

yellowdiamond = PolygonAsset([(100,50),(175,150),(100,250),(25,150)],yellow_outline,yellow)
text = TextAsset('Erik',fill=blue, style='bold 30pt Times')

Sprite(yellowdiamond)
Sprite(text, (60,125))
App().run()