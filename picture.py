"""
picture.py
Author: Katie Naughton
Credit: I worked alone. 

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# colors, no transparency
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
yellow = Color(0xffff00,1.0)
lightblue = Color(0X00ffff,1.0)
darkgreen = Color(0x006400, 1.0)
darkblue = Color(0x483D8B, 1.0)
white = Color(0xf8f8ff, 1.0)


#line
thinline=LineStyle(1, black)

#line 2
thinline2=LineStyle(1, darkblue)

#sky day
rectangle4=RectangleAsset (475, 1000, thinline, lightblue)
Sprite(rectangle4, (0, 0))

#sky night
rectangle6=RectangleAsset (460, 1000, thinline, darkblue)
Sprite(rectangle6, (475, 0))

#house
rectangle=RectangleAsset (250, 250, thinline, black)
Sprite(rectangle,(350, 150))

#grass day
rectangle2=RectangleAsset (475, 300, thinline, green)
Sprite(rectangle2, (0, 400))

#grass night
rectangle5=RectangleAsset (460, 350, thinline, darkgreen)
Sprite(rectangle5, (475, 400))

#door
rectangle3=RectangleAsset (100, 100, thinline, red)
Sprite(rectangle3, (400, 300))

#doorknob
ellipse=EllipseAsset (5, 10, thinline, blue)
Sprite(ellipse, (425, 350))

#roof
triangle=PolygonAsset([(1,100),(200,1),(400, 100)], thinline, black)
Sprite(triangle, (275,75))

#sun
circle=CircleAsset(50, thinline, yellow)
Sprite(circle, (0,0))

#moonwhite
circle2=CircleAsset(50, thinline, white)
Sprite(circle2, (800,0))

#moondarkblue
circle3=CircleAsset(40, thinline2, darkblue)
Sprite(circle3, (800,0))








myapp = App()
myapp.run()
