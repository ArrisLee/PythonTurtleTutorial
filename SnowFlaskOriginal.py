import turtle
myPen = turtle.Turtle()
myPen.shape("turtle")
myPen.speed(10)
myPen.color("blue")
myPen.left(90)

for i in range(1, 7):
  myPen.forward(100)
  myPen.forward(-30)
  myPen.left(60)
  myPen.forward(30)
  myPen.forward(-30)
  myPen.right(120)
  myPen.forward(30)
  myPen.forward(-30)
  myPen.left(60)
  myPen.forward(-70)
  myPen.left(60)

turtle.done()
