'''

Heyo! This is Matthew Wang's version of the hexagon wall . py algorithm, which has customizable colours and wall lengths to draw.
November 21  2014
'''
#imports
import turtle
import random
#defs
def randocolour(turtle):
	red = random.randint(0,255)
	green = random.randint(0,255)
	blue = random.randint(0,255)
	turtle.pencolor(0,0,0)
	turtle.fillcolor(red,green,blue)

def shape(turtle,sides,angle):
	randocolour(turtle)
	for i in range(sides):
		turtle.forward(50)
		turtle.right(angle)

def newrow(turtle,length):
	turtle.right(90)
	turtle.forward(85)
	turtle.right(90)
	turtle.forward(length*100)
	turtle.right(180)

# main () now
#windows
window = turtle.Screen()
window.title = ("This isn't that fun.")
window.screensize(1280,900)

#set colormode to RGB
turtle.colormode(255)

#turtlesetup
drawer = turtle.Turtle()
drawer.penup()
drawer.speed(50)
drawer.setpos(-250,250)
drawer.pendown()

#looptime
for i in range(5):
	for i in range(5):
		drawer.begin_fill()
		shape(drawer,6,60)
		drawer.end_fill()
		drawer.penup()
		drawer.forward(100)
		drawer.pendown()
	drawer.penup()
	newrow(drawer,5)
	drawer.down()
turtle.mainloop()
