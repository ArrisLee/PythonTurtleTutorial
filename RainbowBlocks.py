import turtle
import random

colorList = ["blue", "green", "magenta", "red", "orange", "yellow", "purple"]
pen = turtle.Turtle()
# pen.shape("arrow")
pen.speed("fastest")

def draw_block(color, size):
  pen.down()
  pen.fillcolor(color)
  pen.begin_fill()
  for i in range(1,5):
    pen.color(color)
    pen.forward(size)
    pen.left(90)
  pen.end_fill()


for i in range (1, 91):
  color = random.choice(colorList)
  pen.up()
  pen.goto(random.randint(-300,301), random.randint(-300,301))
  draw_block(color,random.randint(20,81))


turtle.done()
