import turtle
import random

colorList = ["blue", "black", "green", "magenta", "red"]

turtle_army = []
for i in range (1, 100):
  new_turtle = turtle.Turtle()
  new_turtle.shape("turtle")
  turtle_army.append(new_turtle)

for turtle in turtle_army:
  turtle.speed(20)
  turtle.color(random.choice(colorList))
  turtle.left(random.randint(10,361))
  turtle.forward(random.randint(10,200))
