from turtle import *

rat = Turtle()

rat.color("green")
rat.pensize(4)
rat.speed(4)
rat.shape("turtle")

for x in range(4):
	rat.forward(150)
	rat.left(90)


mainloop()