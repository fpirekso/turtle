from turtle import *

rat = Turtle()

rat.color("green")
rat.pensize(4)
rat.speed(4)
rat.shape("turtle")

cow = Turtle()

cow.color("purple")
cow.pensize(4)
cow.speed(4)
cow.shape("turtle")


for x in range(3):
	rat.forward(150)
	rat.left(120)

cow.circle(100)


mainloop()