# import package
import turtle


pen = turtle.Turtle()
pen.speed(0)
# method to draw square with dots
# space --> distance between dots
# x     --> side of square
def draw(length, width, xcoordinates, ycoordinates):
    pen.goto(-length/2, -width/2)
    pen.pendown()
    pen.forward(length)
    pen.left(90)
    pen.forward(width)
    pen.left(90)
    pen.forward(length)
    pen.left(90)
    pen.forward(width)
    pen.left(90)
    pen.penup()
    for i in xcoordinates:
        for j in ycoordinates:
            pen.goto(i-length/2, j-width/2)
            pen.dot()


# Main Section

xcoordinates = [10, 20, 40, 70, 100]
ycoordinates = [10, 30, 50, 70, 90]
pen.penup()
draw(120, 120, xcoordinates, ycoordinates)

# hide the turtle
pen.hideturtle()

# exit from the screen
# if and only if
# mouse is clicked
turtle.exitonclick()
turtle.done()
turtle.bye()