import turtle
import random
def randcolor(turt):
	turt.pencolor(random.randint(0.0,1.0),random.randint(0.0,1.0),random.randint(0.0,1.0))
def shape(turtle,loopcount):
	for i in range(loopcount):
        	turtle.forward(100)
        	turtle.right(90)
def newrow(turtle,length):
	turtle.right(90)
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(length*100)
	turtle.right(180)
	randcolor(turtle)
window = turtle.Screen()
window.screensize(1200,900)
alex = turtle.Turtle()
for i in range(4):
	for i in range(4):
        	shape(alex,4)
		alex.forward(100)
		randcolor(alex)
	newrow(alex,4)
turtle.mainloop()                   
