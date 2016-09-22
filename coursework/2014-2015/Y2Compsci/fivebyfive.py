'''
Heyo! This is Matthew Wang's version of the colour wall . py algorithm, which has customizable colours and wall lengths to draw.
November 17 2014
'''
#imports
import turtle
import random
#defs
def randocolour(turtle):
	red = random.randint(0,255)
	green = random.randint(0,255)
	blue = random.randint(0,255)
	turtle.pencolor(red,green,blue)
	turtle.fillcolor(red,green,blue)

def shape(turtle,sides,angle):
	randocolour(turtle)
	for i in range(sides):
		turtle.forward(100)
		turtle.right(angle)

def newrow(turtle,length):
	turtle.right(90)
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(length*100)
	turtle.right(180)

# main () now
#windows
window = turtle.Screen()
window.screensize(1280,900)

#set colormode to RGB
turtle.colormode(255)

#turtlesetup
drawer = turtle.Turtle()
drawer.penup()
drawer.setpos(-250,250)
drawer.pendown()

#looptime
for i in range(5):
	for i in range(5):
		drawer.begin_fill()
		shape(drawer,4,90)
		drawer.end_fill()
		drawer.forward(100)
	drawer.penup()
	newrow(drawer,5)
	drawer.down()
turtle.mainloop()
