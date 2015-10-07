import turtle
import time
wn = turtle.Screen()
turtle.register_shape("yoda.gif")


def setup(x,y):
	wn.screensize(400,400)	
	#turtle.up()
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.width(2)
	turtle.turtlesize(2)
	turtle.color("green")
	turtle.shape("yoda.gif")
	#turtle.down()
	#time.sleep(1)
	wn.listen()
	wn.onkey(home,"t")
	wn.onkey(up, "Up")
	wn.onkey(down, "Down")
	wn.onkey(right, "Right")
	wn.onkey(left, "Left")
	wn.onkey(escaper, "Escape")

def checkxbound():
	if turtle.xcor() > (wn.screensize()[0]/2):
		return 1
	elif turtle.xcor() < (wn.screensize()[0]/-2):
		return 2
	else:
		return 0
	time.sleep(1)
def checkybound():
	if turtle.ycor() > (wn.screensize()[0]/2):
		return 3
	elif turtle.ycor() < (wn.screensize()[0]/-2):
		return 4
	else:
		return 0
	time.sleep(1)
#Event handlers
def left():
	checkxbound()
	if checkxbound != 2:
		turtle.backward(50)

def right():
	checkxbound()
	if checkxbound != 1:
		turtle.forward(50)

def up():
	checkybound()
	if checkybound != 3:
		turtle.left(90)
		turtle.forward(50)
		turtle.right(90)

def down():
	checkybound()
	if checkybound != 4:
		turtle.left(90)
		turtle.backward(50)
		turtle.right(90)
	
def quitTurtles():
	wn.bye()

def home():
	turtle.goto(-200,200)

def escaper():
	wn.bye()
     
# Send the arguments to setup
setup(-200,200)
i = 1
'''while (i == 1):
	time.sleep(1)
	#wn.listen()
	wn.onkey(home,"t")
	wn.onkey(up, "Up")
	wn.onkey(down, "Down")
	wn.onkey(right, "Right")
	wn.onkey(left, "Left")
	wn.onkey(escaper, "Escape")
	wn.listen()'''


# Run the mainloop!
turtle.mainloop()
