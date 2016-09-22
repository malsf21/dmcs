import turtle 
import random
ninja = turtle.Turtle()

ninja.speed(10)

for i in range(180):
	ninja.pencolor(random.randint(0.0,1.0),random.randint(0.0,1.0),random.randint(0.0,1.0))
	ninja.forward(100)
	ninja.right(30)
	ninja.forward(20)
	ninja.left(60)
	ninja.forward(50)
	ninja.right(30)

	ninja.penup()	
	ninja.setposition(0, 0)
	ninja.pendown()

	ninja.right(2)
    
turtle.mainloop
