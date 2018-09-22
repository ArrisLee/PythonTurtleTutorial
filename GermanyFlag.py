import turtle

pen = turtle.Turtle()
pen.speed(10)

def draw_block(color):
  pen.down()
  pen.fillcolor(color)
  pen.begin_fill()
  pen.forward(200)
  pen.left(90)
  pen.forward(35)
  pen.left(90)
  pen.forward(200)
  pen.left(90)
  pen.forward(35)
  pen.left(90)
  pen.forward(200)
  pen.end_fill()
  pen.up()
  pen.backward(200)
  pen.right(90)
  pen.forward(35)
  pen.left(90)


draw_block("black")
draw_block("red")
draw_block("yellow")

pen.done()
