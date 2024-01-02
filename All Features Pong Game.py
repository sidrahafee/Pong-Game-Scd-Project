import turtle
import cProfile

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

root = turtle.Screen()
root.bgcolor("light blue")
root.title("Pong Game By Sidra")
root.setup(width=850, height=650)
root.tracer(2)

# paddle_a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle_b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

score_a = 0
score_b = 0

# Keyboard binding
root.listen()
root.onkeypress(paddle_a_up, "w")
root.onkeypress(paddle_a_down, "x")
root.onkeypress(paddle_b_up, "o")
root.onkeypress(paddle_b_down, "k")

# Main game loop
def update():
    global score_a, score_b
    root.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # When_ball_Touch_the_border_hit_the_ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    assert -290 <= ball.ycor() <= 290, "Ball y-coordinate out of bounds"

    if (
        ball.xcor() < -340
        and ball.ycor() < paddle_a.ycor() + 40
        and ball.ycor() > paddle_a.ycor() - 40
    ):
        ball.dx *= -1
    elif (
        ball.xcor() > 340
        and ball.ycor() < paddle_b.ycor() + 40
        and ball.ycor() > paddle_b.ycor() - 40
    ):
        ball.dx *= -1

    root.ontimer(update, 10)

def main():
    update()

# Run the profiler on the main function
cProfile.run("main()", sort="cumulative")

# Run the main event loop
root.mainloop()

