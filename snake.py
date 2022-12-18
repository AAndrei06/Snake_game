# Snake game
# Snake Head 20x20
# Snake parts 20x20
# Screen 600x600

import turtle
import time
import random
import tkinter

# Screen setup

error = False

try:

	wn=turtle.Screen()
	wn.setup(600,600)
	wn.bgcolor("green")
	wn.tracer(0)
	wn.title("Snake Game")
	try:
		img = tkinter.Image("photo", file="snake.png")
		turtle._Screen._root.iconphoto(True, img)
	except:
		if error == False:
			error = True
		else:
			error = False

	# Snake Head

	head=turtle.Turtle()
	head.color("black")
	head.shape("square")
	head.penup()
	head.shapesize(1.2,1.2,1)
	head.speed(0)
	head.setposition(0,0)
	head_direction="stop"

	# Snake Food

	food=turtle.Turtle()
	food.color("red")
	food.shape("circle")
	food.shapesize(1.2,1.2,1)
	food.penup()
	x_f=random.randint(-290,290)
	y_f=random.randint(-290,290)
	food.setposition(x_f,y_f)
	food.speed(0)

	# Snake parts

	parts=[]

	# Border Line

	pen=turtle.Turtle()
	pen.penup()
	pen.color("black")
	pen.setposition(-298,298)
	pen.width(6)
	pen.pendown()
	for line in range(4):
		pen.forward(588)
		pen.right(90)
	pen.hideturtle()


	# Variables
	distance=20
	time_pause=0.1
	score=0
	high_score=0

	# Score Pen

	pen2=turtle.Turtle()
	pen2.penup()
	pen2.hideturtle()
	pen2.color("black")
	pen2.setposition(-150,260)
	pen2.write("Score: {}   High Score: {}".format(score,high_score),font=("Arial Black",22))

	# Functions

	def down():
		global head_direction
		if head_direction!="up":
			head_direction="down"

	def up():
		global head_direction
		if head_direction != "down":
			head_direction="up"

	def right():
		global head_direction
		if head_direction != "left":
			head_direction="right"

	def left():
		global head_direction
		if head_direction != "right":
			head_direction="left"

	# Keyboard

	turtle.listen()
	turtle.onkeypress(down,"Down")
	turtle.onkeypress(up,"Up")
	turtle.onkeypress(right,"Right")
	turtle.onkeypress(left,"Left")
		
	while True:


		wn.update()

		if (head.xcor() > 290) or (head.xcor() < -290) or (head.ycor() < -290) or (head.ycor() > 290):
			head.setposition(0,0)
			for part in parts:
				part.hideturtle()
				part.setposition(350,350)
			parts.clear()
			head_direction="stop"
			pen2.clear()
			score = 0
			pen2.write("Score: {}   High Score: {}".format(score,high_score),font=("Arial Black",22))


		if head_direction=="stop":
			head.setposition(0,0)


		if head_direction=="up":
			y=head.ycor()
			y+=distance
			head.sety(y)
			time.sleep(time_pause)

		if head_direction=="down":
			y=head.ycor()
			y-=distance
			head.sety(y)
			time.sleep(time_pause)

		if head_direction=="right":
			x=head.xcor()
			x+=distance
			head.setx(x)
			time.sleep(time_pause)

		if head_direction=="left":
			x=head.xcor()
			x-=distance
			head.setx(x)
			time.sleep(time_pause)

		if head.distance(food) < 20:
			x=random.randint(-290,290)
			y=random.randint(-290,290)
			food.setposition(x,y)
			score+=1
			pen2.clear()
			pen2.write("Score: {}   High Score: {}".format(score,high_score),font=("Arial Black",22))

			if score >= high_score:
				high_score=score

			part=turtle.Turtle()
			part.color("lightgreen")
			part.penup()
			part.shape("square")
			part.speed(0)
			parts.append(part)


		for index in range(len(parts)-1,0,-1):
			x=parts[index-1].xcor()
			y=parts[index-1].ycor()
			parts[index].goto(x,y)

		if len(parts)>0:
			x=head.xcor()
			y=head.ycor()
			parts[0].goto(x,y)

		

	turtle.mainloop()

except:
	error = True

